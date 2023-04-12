###
### Author : Swapnil Ashok Jadhav (github:swapaj)
### Created Date : 16 Dec 2022
###


from yubiai import set_model_info,  verify_model_path
from fairseq.models.transformer import TransformerModel
import os, re


class Seq2SeqFairseqWrapper:
    def __init__(self, use_gpu=False, model_type="TrueCaser_transformer_wmt_en_de_big_t2t"):
        self.use_gpu = use_gpu
        
        self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name = set_model_info(model_type)
        verify_model_path(self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name)
        self.model = self.load_model()
    
    def load_model(self):
        """
        Load model from default path
        """
        model = TransformerModel.from_pretrained(self.model_folder_path,
                                                checkpoint_file="checkpoint_best.pt", 
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
