###
### Author : Swapnil Ashok Jadhav (github:swapaj)
### Created Date : 16 Dec 2022
###

from fairseq.models.transformer import TransformerModel
from YubiAI import FTPHOST, FTPPORT, BASE_PATH 
import os, re


class Seq2SeqFairseqWrapper:
    def __init__(self, use_gpu=False, model_type="TrueCaser_transformer_wmt_en_de_big_t2t"):
        self.use_gpu = use_gpu
        self.model_type = model_type
        self.current_path = BASE_PATH
        self.model_folder_name = model_type
        self.model_folder_path = "%s/models/%s" % (self.current_path, self.model_folder_name)
        self.model_file_name = "checkpoint_best.pt"
        self.model_file_path = "%s/%s" % (self.model_folder_path, self.model_file_name)

        self.model_zip_path = "%s/models/" % self.current_path
        self.model_zip_name = "%s.zip" % self.model_folder_name
        self.ftp_path = "http://%s:%s/yubi_ds_capability/models/%s" % (FTPHOST, FTPPORT, self.model_zip_name)

        self.verify_model_path_ftp()
        self.model = self.load_model()

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
        model = TransformerModel.from_pretrained(self.model_folder_path,
                                                checkpoint_file=self.model_file_name, 
                                                data_name_or_path="./bin_data", 
                                                bpe="sentencepiece")
        model.eval()
        if self.use_gpu == True:
            model.cuda()
        return model

    def get_translation(self, text, to_lower=False, to_char=False):
        if to_lower == True:
            text = text.lower()
        if to_char == True:
            text = " ".join([ch for ch in text]).strip().lower()
        text = re.sub("\s+", " ", text)
        text = text.strip()
        translated_text = self.model.translate(text)
        return translated_text
