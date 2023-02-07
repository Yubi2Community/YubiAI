###
### Author : Sanprit Nayan (github:sanprit)
### Created Date : 27 Sept 2022
### Modification Date : 2 Feb 2022 (github:navin-kumar-k)
###

import numpy as np
import cv2
from PIL import Image
from scipy import ndimage

class image_preprocessing():
    
    def get_multiple_rotated_images(self):
        self.rotate_random = True
        np.random.seed(self.seed)
        if not self.n_rotated:
            print("Enter No. of rotated_images to genrate")
        for i in range(self.n_rotated):
            yield self.get_rotated_image(), self.img_info
    
    def get_multiple_random_crop(self, img):
        np.random.seed(self.seed)
        if not self.n_random:
            print("Enter No. of random_images to genrate")
        for i in range(self.n_random):
            yield self.get_random_crop(img), self.img_info
            
    def get_multiple_rotated_random_crop(self):
        np.random.seed(self.seed)
        self.rotate_random = True
        for i in range(self.n_rotated):
            self.new_img = self.get_rotated_image()
            for i in range(self.n_random):
                yield self.get_random_crop(self.new_img), self.img_info
                    
    def get_resized_image(self):
        '''
        @input image : array of image eg: image= numpy.array(Image.open(<image_path>))
        @input cimage_height : height of desired crop image
        @input image_width : width of desired crop image=
        @process : selects only mentioned portion of image
        @output : returns array of final image
        '''
        if(self.resize_image_width <=0) or (self.resize_image_width > self.image.shape[0]):
            print('select desired resize width in range(0, {image_width})'.format(image_width=str(self.image.shape[1])))
            return
        if(self.resize_image_height <=0) or (self.resize_image_height > self.image.shape[1]):
            print('select desired resize height in range(0, {image_height})'.format(image_height=str(self.image.shape[0])))
            return
        self.image = cv2.resize(self.image, (self.resize_image_width, self.resize_image_height),interpolation = cv2.INTER_AREA)

        return self.image

    def get_flipped_image(self):
        '''
        @input image : array of image eg: image= numpy.array(Image.open(<image_path>))
        @input horizontal : whether image to flipped horizontally or not
        @input vertical : whether image to flipped vertically or not
        @output : returns array of flipped image
        '''
        if self.flip_vertical and self.flip_horizontal:
            return cv2.flip(self.image,-1)
        elif self.flip_horizontal:
            return cv2.flip(self.image,1)
        elif self.flip_vertical:
            return cv2.flip(self.image,0)
        else:
            return self.image

    def get_rotated_image(self):        
        '''
        @input image : array of image eg: image= numpy.array(Image.open(<image_path>))
        @rotate skew : degree of clockwise rotation
        @rotate random : whether to take random rotate skew or not
        @process: rotate the image in clockwise direction with respect to orignal skew of image and genrate a genral frame to fit
        all types of angle
        @output: return array of rotated image
        '''
        skew = self.rotate_skew
        if self.rotate_random:
            skew = np.random.randint(0, 360)     
        rotate_img = ndimage.rotate(self.image, -skew, reshape=self.rotate_reshape, cval=255)
        self.img_info['skew'] = skew
        
        return rotate_img
   
    def check_white_pixels(self,im):
        '''
        @input image : array of image eg: image= numpy.array(Image.open(<image_path>))
        @process : calculate the white pixels percentage in image
        @output : return float value of white pixel percentage
        '''
        ret, im = cv2.threshold(im,120,255,cv2.THRESH_BINARY)
        n_pixels = np.sum(im >= 0)
        n_white_pix = np.sum(im == 255)
        percentage = (n_white_pix/n_pixels) * 100
        return percentage    
     
    def get_random_crop(self,img):   
        '''
        @input image : array of image eg: image= numpy.array(Image.open(<image_path>))
        @input cimage_height : height of desired crop image
        @input image_width : width of desired crop image
        @process : selects only mentioned portion of image
        @output : returns array of final image
        '''
        max_x = img.shape[1] - self.cropped_image_width
        max_y = img.shape[0] - self.cropped_image_height
        if max_x <= 0 or max_y <= 0:
            print("Original Image is smaller than desired crop size")
            return 0
        threshold = self.random_crop_white_percent
        count = 0
        percentage = 100
        while percentage > threshold and threshold < 99:
            x = np.random.randint(0, max_x)
            y = np.random.randint(0, max_y)
            crop = img[y: y + self.cropped_image_height, x: x + self.cropped_image_width]
            percentage = self.check_white_pixels(crop)
            count +=1
            self.img_info['random_crop_white_pix'] = percentage
            self.img_info['random_crop_coordinates'] = (x,y)
            
            if count == 15 and self.random_crop_white_increment:
                threshold += 3
                count = 0
            elif count == 15:
                print("Generated random_crop of more than specified percentage, Max Tries reached")
                return crop
    
        if threshold >= 99:
            print("Generated random_crop of More than 99% white pixels")
            return crop        
        else:
            return crop
            
    def preprocess(self,
                 image_path,
                 seed = 0,
                 random_crop = False, 
                 resize_image = False,
                 flip_image = False,
                 rotate_image = False,
                 print_white_pix_precent = False,  
                 cropped_image_height=256,
                 cropped_image_width=256,
                 flip_horizontal=False, 
                 flip_vertical= False,
                 resize_image_height=256, 
                 resize_image_width=256,
                 rotate_skew = 0,
                 rotate_random = False,
                 random_crop_white_percent = 98,
                 random_crop_white_increment = False,
                 rotate_reshape = True
                 ):
        '''
        image_path: Path of image (Type=str)
        random_crop: Create a random crop of desired height and width (Type=Boolean)
            cropped_image_height: height of desired image height, defalut=256 (Type=Int)
            cropped_image_width: width of desired image width, default = 256  (Type=Int)
            random_crop_white_percent: threshold value of white percent in cropped image (Type=Int)
            random_crop_white_increment: increase the value of threshold by 3 after 15 unsuccessful tries max 98 (Type=Boolean)
        resize_image: Create a resized image of desired height and width (Type=Boolean)
            resize_image_height: height of desired image height, defalut=256 (Type=Int)
            resize_image_width:  width of desired image width, default = 256  (Type=Int)
        flip_image: Create a fliped image based on desired axis
            flip_horizontal: whether image to flipped horizontally or not
            flip_vertical: whether image to flipped vertically or not
        rotate_image: Create a rotated image on the desired skew from original (Type=Boolean)
            rotate_skew: angle to be rotated in clockwise direction (Type=Int)
            rotate_random: randomly rotate the image (Type=Boolean)
        print_white_pix_precent: Print the white pixel percentage in image (Type=Boolean)
        '''
        self.image = np.array(Image.open(image_path))
        self.rotate_reshape = rotate_reshape
        self.resize_image = resize_image
        self.flip_image = flip_image
        self.rotate_image = rotate_image
        self.random_crop = random_crop
        self.flip_horizontal = flip_horizontal
        self.flip_vertical = flip_vertical
        self.resize_image_height = resize_image_height
        self.resize_image_width = resize_image_width
        self.rotate_skew = rotate_skew
        self.rotate_random = rotate_random
        self.cropped_image_height = cropped_image_height
        self.cropped_image_width = cropped_image_width
        self.random_crop_white_percent = random_crop_white_percent
        self.print_white_pix_precent = print_white_pix_precent
        self.random_crop_white_increment = random_crop_white_increment
        self.random_crop_white_percent = random_crop_white_percent
        self.seed = seed
        self.img_info = {'random_crop_white_pix': 0, 'random_crop_coordinates':(0,0), 'skew':0}

        if self.flip_image:
            self.image = self.get_flipped_image()
        if self.rotate_image:
            np.random.seed(self.seed)
            self.image = self.get_rotated_image()
        if self.random_crop:
            np.random.seed(self.seed)
            self.image = self.get_random_crop(self.image)
        if self.resize_image:
            self.image = self.get_resized_image()
        if self.print_white_pix_precent:
            print(self.check_white_pixels(self.image))

        return self.image
        
    def image_generator(self,image_path,
                 seed = 0, 
                 multiple_rotated_images = False,
                 multiple_random_crops = False,
                 cropped_image_height=256,
                 cropped_image_width=256,
                 random_crop_white_percent = 98,
                 random_crop_white_increment = False,
                 rotate_random = True,
                 n_random = 50,
                 n_rotated = 50,
                 rotate_skew = 0,
                 rotate_reshape = True       
                  ):
        '''
        multiple_rotate: Genrate multiple random rotation of the image (Type=Boolean)
            n_rotated: No. of rotated images to genrate, defalut=50 (Type=Int) 
        multiple_random: Genrate multiple random crops of the image (Type=Boolean)
            cropped_image_height: height of desired image height, defalut=256 (Type=Int)
            cropped_image_width: width of desired image width, default = 256  (Type=Int)
            n_random: No. of random crop of images to genrate, defalut=50 (Type=Int)
        random_crop_white_percent: threshold value of white percent in cropped image (Type=Int)
        random_crop_white_increment: increase the value of threshold by 3 after 15 unsuccessful tries max 98 (Type=Boolean)
        seed: seed value for random generators to replicate the results 
        @Note 
        multiple_rotate and multiple_random will output genrator instead of image which can iterated using next(output_gen)
        '''
        self.image = np.array(Image.open(image_path))
        self.seed = seed
        self.rotate_skew = rotate_skew
        self.rotate_reshape = rotate_reshape
        self.rotate_random = rotate_random
        self.cropped_image_height = cropped_image_height
        self.cropped_image_width = cropped_image_width
        self.random_crop_white_percent = random_crop_white_percent
        self.random_crop_white_increment = random_crop_white_increment
        self.n_random = n_random
        self.n_rotated = n_rotated
        self.multiple_rotated_images = multiple_rotated_images
        self.multiple_random_crops = multiple_random_crops
        self.new_img = None
        self.img_info = {'random_crop_white_pix': 0, 'random_crop_coordinates':(0,0), 'skew':0}
         
        if self.multiple_rotated_images and self.multiple_random_crops:
            return self.get_multiple_rotated_random_crop()
        if self.multiple_rotated_images:
            return self.get_multiple_rotated_images()
        self.image = self.get_rotated_image()
        
        if self.multiple_random_crops:
            return self.get_multiple_random_crop(self.image)

            