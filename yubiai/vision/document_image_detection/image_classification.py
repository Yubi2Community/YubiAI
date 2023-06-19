###
### Author : Swapnil Ashok Jadhav
### Created Date : 23 April 2023
### Project Information
###     Two variations of models are prepared
###     Type 1 : Document vs NonDocument classifier
###     Type 2 : NSFW classifiers with 6 class support 
###              'anime', 'docimage', 'explicit', 'gore_violence', 'non-explicit', 'sexy'
###

from yubiai import set_model_info,  verify_model_path
import os, random
from tensorflow.keras.models import load_model
from yubiai.vision.utility.preprocess import image_preprocessing
import numpy as np
import tensorflow as tf
import PIL.Image
from scipy import ndimage
from PIL import Image
from PIL import ImageOps

class DocDetection:
    def __init__(self, model_type="doc-vs-nondoc_Xception_block_12-14", use_gpu=False):
        ### Mention all default model variables
        self.use_gpu = use_gpu
        self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name = set_model_info(model_type)
        verify_model_path(self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name)

        self.model_folder_name = model_type
        if model_type == "doc-vs-nondoc_Xception_block_12-14":
            self.imgsize = 299
        elif model_type == "doc-vs-nondoc_vit-b16_layer15":
            self.imgsize = 384
        else:
            self.imgsize = 299

        self.model = self.load_model(self.model_folder_path)
        self.classes = ['document', 'nondocument']

    def load_model(self, model_path):
        """
        Load model from given path
        """
        model = load_model(model_path)
        return model

    def classify(self, image_path):
        """
        Classify images in documents vs non-documents
        """
        image = np.array(Image.open(image_path))
        val_dataset = tf.data.Dataset.from_tensor_slices([image]).batch(1)
        reshape_layer = tf.keras.layers.experimental.preprocessing.Resizing(self.imgsize, self.imgsize)
        norm_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1/255.)
        norm_val_dataset = val_dataset.map(lambda x: (norm_layer(reshape_layer(x))))
        output = [float("%4.2f"% v) for v in self.model.predict(norm_val_dataset)[0]*100.0]
        result = dict(zip(self.classes, output))
        return result


class NSFWDetection:
    def __init__(self, model_type="nsfw_detection_Xception_block_12-14", use_gpu=False):
        ### Mention all default model variables
        self.use_gpu = use_gpu
        self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name = set_model_info(model_type)
        verify_model_path(self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name)
        
        self.model_folder_name = model_type
        self.imgsize = 299
        if model_type == "nsfw_detection_ResNet101V2":
            self.imgsize = 224
        elif model_type == "nsfw_detection_Xception_block_12-14":
            self.imgsize == 299
        elif model_type == "nsfw_detection_Xception_block_13-14":
            self.imgsize = 299
        elif model_type == "nsfw_detection_vit-b16_layer16":
            self.imgsize = 384
        self.model = self.load_model(self.model_folder_path)
        self.classes = ['anime', 'docimage', 'explicit', 'gore_violence', 'non-explicit', 'sexy']

    def load_model(self, model_path):
        """
        Load model from given path
        """
        model = load_model(model_path)
        return model

    def classify(self, image_path):
        """
        Classify images in documents vs non-documents
        """
        image = np.array(Image.open(image_path))
        val_dataset = tf.data.Dataset.from_tensor_slices([image]).batch(1)
        reshape_layer = tf.keras.layers.experimental.preprocessing.Resizing(self.imgsize, self.imgsize)
        norm_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1/255.)
        norm_val_dataset = val_dataset.map(lambda x: (norm_layer(reshape_layer(x))))
        output = [float("%4.2f"% v) for v in self.model.predict(norm_val_dataset)[0]*100.0]
        result = dict(zip(self.classes, output))
        return result
