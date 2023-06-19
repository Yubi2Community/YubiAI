###
### Author : Sanprit Nayan
### Created Date : 31 March 2023
### Model Information
###     Text NSFW Detection Model Trained using pubilically avaliable comments on social media platforms.
###     Support 14 most used Indian languages + 13 Transliterated Versions of Indian Languages.
###     Data size : >1 cr comments

from yubiai import set_model_info,  verify_model_path
import os, re, torch
import numpy as np
from fairseq.models.roberta import RobertaModel
from fairseq.data.data_utils import collate_tokens
from torch.nn.functional import softmax
from yubiai.nlp.utility.file_handlers import load_json
from collections import Counter

class NSFWDetection():
    """
    Generic class to call yubibert finetuned models
    Should be noted that .. this will only work when - 
        1. Added task_name.zip file on ftp server /models/yubi/ folder and you have classifier head name handy
        2. keep following file names same 
            a. checkpoint_best.pt
            b. bin_data folder
                i. label folder
                ii. input0 folder
            c. sentencepiece.bpe.model, sentencepiece_vocab
    """
    def __init__(self, task_name="text_nsfw_detection", use_gpu=False):
        
        self.use_gpu = use_gpu
        self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name = set_model_info(task_name)
        verify_model_path(self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name)
        self.model = self.load_model()
        self.label_fn = lambda label: self.model.task.label_dictionary.string([label + self.model.task.label_dictionary.nspecial])

    def verify_model_path_ftp(self):
        """
        Verify if model folder exists at default path.
        If not then download the same from default ftp location
        """
        if os.path.exists(self.model_folder_path):
            print("Model Path exist !!")
        elif os.path.exists(f"{self.model_zip_path}/{self.model_zip_name}"):
            print("Model Path exist(ZIP format) !!")
            os.system("cd %s; unzip %s; rm -f %s; cd -;" % (self.model_zip_path, self.model_zip_name, self.model_zip_name))
        else:
            print("Model Path do not exist !!")
            os.system("wget %s -P %s" % (self.ftp_path, self.model_zip_path))
            os.system("cd %s; unzip %s; rm -f %s; cd -;" % (self.model_zip_path, self.model_zip_name, self.model_zip_name))

    def load_model(self):
        """
        Load model from default path
        """
        model = RobertaModel.from_pretrained(self.model_folder_path, checkpoint_file="checkpoint_best.pt", data_name_or_path="./bin_data", bpe="sentencepiece")
        model.eval()
        if self.use_gpu == True:
            model.cuda()
        return model

    def detect_NSFW(self,input_text):
        """
        Generic classfication function .. which returns classes with scores. 
        Higher the score is better.
        """
        input_text = re.sub("\s+", " ", input_text)
        input_text = input_text.lower().strip()
        tokens = self.model.encode(input_text)
        outprob = self.model.predict("comment_classifier", tokens[:510]).tolist()[0]
        min_prob = np.min(outprob)
        outprob_norm = [x-min_prob for x in outprob]
        sum_prob = np.sum(outprob_norm)
        outprob_norm = [x*1.0/sum_prob for x in outprob_norm]
        outclass = [self.label_fn(i) for i in range(len(outprob))]

        outmap_norm = dict(zip(outclass, outprob_norm))
        outmap_norm = {k: v for k, v in sorted(outmap_norm.items(), key=lambda item: item[1], reverse=True)}

        outmap_og = dict(zip(outclass, outprob))
        outmap_og = {k: v for k, v in sorted(outmap_og.items(), key=lambda item: item[1], reverse=True)}
        
        result =  dict(Counter(outmap_norm).most_common(2))
        
        total_score = np.sum(np.array(list(result.values())))
        result = {k:v/total_score for k,v in result.items()}
        out_result ={}
        out_result['sfw'] = int(result['0'])
        out_result['nsfw'] = int(result['1'])
        return out_result