###
### Author : Swapnil Ashok Jadhav
### Created Date : 1 Feb 2023
### Project Information
###     Two variations of models are prepared
###     Type 1 : Qudrant Detection (0-90-180-270-0 and 45-135-225-315-45)
###     Type 2 : Skew Angle Detection (0 to 90 float numbers)
###

from cernunnos import FTPHOST, FTPPORT, CERNUNNOS_PATH
import os, random
import PIL.Image
from tensorflow.keras.models import load_model
from YubiAI.vision.utility.preprocess import image_preprocessing
import numpy as np
import tensorflow as tf
from scipy import ndimage
from PIL import Image
from PIL import ImageOps


class YubiDocSkewDetector:
    def __init__(self, qudrant_model="Quad4Detection_ResNet101V2_0-90", skew_model="SkewDetection_ResNet101V2_0-90", use_gpu=False):
        ### Mention all default model variables
        self.use_gpu = use_gpu
        self.current_path = CERNUNNOS_PATH

        self.preprocessing_obj = image_preprocessing()

        ### Quadrant Detection Model
        self.qudrant_model_folder_name = qudrant_model
        self.qudrant_model_folder_path = "%s/models/%s" % (self.current_path, self.qudrant_model_folder_name)
        self.qudrant_model_zip_path = "%s/models/" % self.current_path
        self.qudrant_model_zip_name = "%s.zip" % self.qudrant_model_folder_name
        self.qudrant_model_ftp_path = "http://%s:%s/yubi_ds_capability/models/%s" % (FTPHOST, FTPPORT, self.qudrant_model_zip_name)
        self.verify_model_path_ftp(model_type="qudrant")
        self.qudrant_model = self.load_model(self.qudrant_model_folder_path)

        ### Skew/Rotation Detection Model
        self.skew_model_folder_name = skew_model
        self.skew_model_folder_path = "%s/models/%s" % (self.current_path, self.skew_model_folder_name)
        self.skew_model_zip_path = "%s/models/" % self.current_path
        self.skew_model_zip_name = "%s.zip" % self.skew_model_folder_name
        self.skew_model_ftp_path = "http://%s:%s/yubi_ds_capability/models/%s" % (FTPHOST, FTPPORT, self.skew_model_zip_name)
        self.verify_model_path_ftp(model_type="skew")
        self.skew_model = self.load_model(self.skew_model_folder_path)

    def verify_model_path_ftp(self, model_type="skew"):
        """
        Verify if model folder exists at default path.
        If not then download the same from default ftp location
        """
        if model_type == "skew":
            model_folder_path = self.skew_model_folder_path
            model_zip_path = self.skew_model_zip_path
            model_zip_name = self.skew_model_zip_name
            model_ftp_path = self.skew_model_ftp_path
        else: ### model_type == "qudrant"
            model_folder_path = self.qudrant_model_folder_path
            model_zip_path = self.qudrant_model_zip_path
            model_zip_name = self.qudrant_model_zip_name
            model_ftp_path = self.qudrant_model_ftp_path

        if os.path.exists(model_folder_path):
            print("Model Path exist - %s !!" % model_type)
        elif os.path.exists(f"{model_zip_path}/{model_zip_name}"):
            print("Model Path exist(ZIP format) - %s !!" % model_type)
            os.system("cd %s; unzip %s; rm -f %s; cd -;" % (model_zip_path, model_zip_name, model_zip_name))
        else:
            print("Model Path do not exist - %s !!" % model_type)
            os.system("wget %s -P %s" % (model_ftp_path, model_zip_path))
            os.system("cd %s; unzip %s; rm -f %s; cd -;" % (model_zip_path, model_zip_name, model_zip_name))

    def load_model(self, model_path):
        """
        Load model from given path
        """
        model = load_model(model_path)
        return model

    def correctH(self, img, min_size):
        """
        Keeping the aspect ratio same change height
        """
        x, y = img.size
        newx = max(x, min_size)
        wpercent = newx/float(x)
        newy = int(float(y)*float(wpercent))
        img = img.resize((newx,newy))
        return img
    
    def correctW(self, img, min_size):
        """
        Keeping the aspect ratio same change width
        """
        x, y = img.size
        newy = max(y, min_size)
        hpercent = newy/float(y)
        newx = int(float(x)*float(hpercent))
        img = img.resize((newx,newy))
        return img

    def correct_image_size(self, imagepath, resize=True):
        """
        Makes every image slightly bigger than 512x512 that is 520x520.
        So that crops can be taken out of it.
        """
        min_size = 515
        new_image = PIL.Image.open(imagepath)
        new_image = new_image.convert("RGB")
        if resize is True:
            new_image = self.correctH(new_image, min_size)
            new_image = self.correctW(new_image, min_size)
            new_image.save(imagepath)
        else:
            fill_color = (255, 255, 255, 0)
            x, y = new_image.size
            size = max(min_size, x, y)
            new_image = PIL.Image.new('RGB', (size, size), fill_color)
            new_image.paste(new_image, (int((size - x) / 2), int((size - y) / 2)))
            new_image.save(imagepath)

    def remove_extra_white_paddings(self, imagepath):
        """
        When we rotate the image we see that extra white space keeps getting added.
        Following code will remove that extra white padding.
        """
        image = Image.open(imagepath)
        image.load()
        invert_im = image.convert("RGB")
        invert_im = ImageOps.invert(invert_im)
        imageBox = invert_im.getbbox()
        cropped = image.crop(imageBox)
        cropped.save(imagepath)

    def generate_dataset(self, imagepath, num_crops=10, batch_size=32):
        """
        From given image generate random crops and tensor dataset with batch-size
        """
        self.correct_image_size(imagepath)
        self.remove_extra_white_paddings(imagepath)
        rseed = random.randint(0,9999)

        ### Generated "num_crops" images with random crop strategy
        output_image_gen = self.preprocessing_obj.image_generator(image_path=imagepath, multiple_rotated_images = False,
                                                                  multiple_random_crops = True, cropped_image_height=512,
                                                                  cropped_image_width=512, random_crop_white_percent = 70,
                                                                  random_crop_white_increment = True, n_random = num_crops,
                                                                  n_rotated = 0, rotate_random = False, seed = rseed)
        crop_img_arr = []
        for i in range(num_crops):
            img, _ = next(output_image_gen)
            crop_img_arr.append(img)
        crop_img_arr = np.array(crop_img_arr)

        ### Create dataset with all above images to run in batches
        val_dataset = tf.data.Dataset.from_tensor_slices(crop_img_arr).batch(batch_size)
        reshape_layer = tf.keras.layers.experimental.preprocessing.Resizing(224, 224)
        norm_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1/255.)
        norm_val_dataset = val_dataset.map(lambda x: (norm_layer(reshape_layer(x))))
        return norm_val_dataset

    def predict_qudrant(self, imagepath, num_crops=10, batch_size=32):
        """
        Given an image predicts the Quadrant it belongs to.
        """
        norm_val_dataset = self.generate_dataset(imagepath, num_crops=num_crops, batch_size=batch_size)
        quad_predictions = self.qudrant_model.predict(norm_val_dataset)

        ### Get map of quadrants vs counts 
        outmap = {"Q1":0, "Q2":0, "Q3":0, "Q4":0}
        total = 0.0
        for outarr in quad_predictions:
            classindex = np.argmax(outarr)
            classprob = outarr[classindex]
            outmap["Q%d" % (classindex+1)] += classprob
            total += classprob
        outmap = [(k,v) for k, v in sorted(outmap.items(), key=lambda item: item[1], reverse=True)]
        detected_quadrant = outmap[0][0]
        quadrant_prob = outmap[0][1]*100.0/total

        results = {"detected_quadrant":detected_quadrant, "quadrant_prob":quadrant_prob}
        return results

    def rotate_to_first_qudrant(self, imagepath, detected_quadrant="Q1", saveimage=True):
        """
        Correct the quadrant of given image to Q1
        """
        imgarr = np.asarray(PIL.Image.open(imagepath))
        if detected_quadrant == "Q4": 
            imgarr = ndimage.rotate(imgarr, 270, reshape=True, cval=255)
        elif detected_quadrant == "Q3": 
            imgarr = ndimage.rotate(imgarr, 180, reshape=True, cval=255)
        elif detected_quadrant == "Q2": 
            imgarr = ndimage.rotate(imgarr, 90, reshape=True, cval=255)
        if saveimage is True:
            imgobj = PIL.Image.fromarray(imgarr)
            imgobj.save(imagepath)
        return imgarr

    def predict_angle(self, imagepath, num_crops=10, batch_size=32):
        """
        Given an image predicts the Angle it is rotated. 
        Either in -45 to 45  OR 0 to 90 depending upon the model chosen.
        Quadrant has to be corrected before this method
        """
        norm_val_dataset = self.generate_dataset(imagepath, num_crops=num_crops, batch_size=batch_size)
        angle_preds = [x[0] for x in self.skew_model.predict(norm_val_dataset)]
        average_angle = np.mean(angle_preds)
        median_angle = np.median(angle_preds)
        results = {"average_angle": average_angle, "angle_preds": angle_preds, "median_angle":median_angle}
        return results

    def rotate_to_correct_angle(self, imagepath, angle, saveimage=True):
        """
        Rotate and save given image with skew angle
        """
        imgarr = np.asarray(PIL.Image.open(imagepath))
        if self.skew_model_folder_name == "SkewDetection_ResNet101V2_45-135":
            angle = angle - 45
        imgarr = ndimage.rotate(imgarr, angle, reshape=True, cval=255)
        if saveimage is True:
            imgobj = PIL.Image.fromarray(imgarr)
            imgobj.save(imagepath)
        return imgarr

    def correct_image_skew_sample_code(self, imagepath, num_crops=10, batch_size=32):
        """
        Sample code given which works end-2-end
        Detects quadrant -> Corrects quadrant -> Predicts Angle -> Corrects Angle
        User should analyse and change the code according to their need.
        """
        quad_results = self.predict_qudrant(imagepath, num_crops, batch_size)
        print("quad_results : ", quad_results)
        detected_quadrant = quad_results['detected_quadrant']
        quad_correct_img = self.rotate_to_first_qudrant(imagepath, detected_quadrant, True)
        skew_results = self.predict_angle(imagepath, num_crops, batch_size)
        print("skew_results : ", skew_results)
        skew_correct_img = self.rotate_to_correct_angle(imagepath, skew_results['median_angle'], True)
        self.remove_extra_white_paddings(imagepath)
        return detected_quadrant, skew_results['median_angle']
