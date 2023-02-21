###
### Author : Mettu Venkata Ramireddy
### Created Date : 27 December 2022
### Credit: https://github.com/facebookresearch/fairseq/blob/main/examples/xlmr/README.md
### Model Information
###     Language Detection Model Trained using News data of Indian News Papers.
###     Support 14 most used Indian languages + 13 Transliterated Versions of Indian Languages.
###     Data consists of : News
###     Data size of : >12Gb
###

import os, re, torch, json
from fairseq.models.roberta import RobertaModel
from fairseq.data.data_utils import collate_tokens
from torch.nn.functional import softmax
from yubiai.nlp.utility.file_handlers import load_json
from yubiai import FTPHOST, FTPPORT, BASE_PATH



class LanguageDetection():
    """
    Generic class to call yubibert finetuned models
    Should be noted that .. this will only work when - 
        1. Added task_name.zip file on ftp server /models/yubi/ folder and you have classifier head name handy
        2. Added s3 path in /models/yubi/ folder
        3. keep following file names same 
            a. checkpoint_best.pt
            b. bin_data folder
                i. label folder
                ii. input0 folder
            c. sentencepiece.bpe.model, sentencepiece_vocab
    """
    def __init__(self, task_name="e4_v2_language_detection", use_gpu=False):
        
        self.use_gpu = use_gpu
        self.current_path = BASE_PATH
        self.model_folder_name = task_name
        self.model_folder_path = "%s/models/%s" % (self.current_path, self.model_folder_name)
        self.model_file_name = "checkpoint_best.pt"
        self.languages_supported_file_name = "languages_supported.json"
        self.model_file_path = "%s/%s" % (self.model_folder_path, self.model_file_name)
        #self.s3_path = "%s/models/%s" % (S3BASEPATH, self.model_folder_name)

        self.model_zip_path = "%s/models/" % self.current_path
        self.model_zip_name = "%s.zip" % task_name
        self.languages_supported_file_path = "%s/%s" % (self.model_folder_path, self.languages_supported_file_name)
        self.ftp_path = "http://%s:%s/yubi_ds_capability/models/%s" % (FTPHOST, FTPPORT, self.model_zip_name)
        
        ### self.verify_model_path()
        self.verify_model_path_ftp()
        self.model = self.load_model()
        self.label_fn = lambda label: self.model.task.label_dictionary.string([label + self.model.task.label_dictionary.nspecial])
        self.languages_supported = load_json(self.languages_supported_file_path)

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

    def verify_model_path(self):
        """
        Verify if model folder exists at default path.
        If not then download the same from default s3 location
        """
        if not os.path.exists(self.model_folder_path):
            print("Model Path do not exist !!")
            print("Downloading from s3 path - %s" % self.model_folder_path)
            os.system("mkdir %s" % self.model_folder_path)
            s3_command = "aws s3 cp --recursive %s %s/" % (self.s3_path, self.model_folder_path)
            os.system(s3_command)

    def load_model(self):
        """
        Load model from default path
        """
        model = RobertaModel.from_pretrained(self.model_folder_path, checkpoint_file="checkpoint_best.pt", data_name_or_path="./bin_data", bpe="sentencepiece")
        model.eval()
        if self.use_gpu == True:
            model.cuda()
        return model

    def detect_language(self, input_text, top_k=5):
        """Detect Language function .. which returns classes with scores. 
        Higher the score is better.
        input_text: str
                    Sentence to predict the language.
        top_k: int
           Number(top) of predictions to return.
        """
        
        assert 1 <= top_k <= len(self.languages_supported), f"Expected k value between 1 and {len(self.languages_supported)}."
        input_text = re.sub("\s+", " ", input_text)
        input_text = input_text.lower().strip()
        tokens = self.model.encode(input_text)
        outprob = self.model.predict("language_detection", tokens[:510])
        #sft = softmax(outprob, dim=1)
        pred_log = softmax(outprob, dim=1)
        top_k_pred_log = torch.topk(input=pred_log, k=top_k, dim=1)
        top_det = []
        for lab_list, prob in list(zip(top_k_pred_log.indices.tolist(), top_k_pred_log.values.tolist())):
            pred_lab = list(map(self.label_fn, lab_list))
            top_det.append(list(zip(pred_lab, prob)))
        pred_langs = []
        for row in top_det:
            for lang, conf in row:
                pred_langs.append({"language": self.languages_supported[lang], "lang_code": lang, "confidence":conf})
        pred_response = {
            "input_text": input_text,
            "language": pred_langs[0]['language'], 
            "lang_code": pred_langs[0]['lang_code'], 
            "confidence":pred_langs[0]['confidence'], 
            "language_rank": pred_langs
        }
        return pred_response
    
    def detect_language_batch(self, input_text_list, top_k=5):
        """Detect Language function to predict language on batch .. which returns classes with scores. 
        Higher the score is better.
        input_text_list: list
                         List of sentences to detect languange.
        top_k: int
           Number(top) of predictions to return. 
        """
        
        assert 1 <= top_k <= len(self.languages_supported), f"Expected k value between 1 and {len(self.languages_supported)}."
        batch_data = [re.sub("\s+", " ", row).lower().strip() for row in input_text_list]
        batch_data = [self.model.encode(sen)[:510] for sen in batch_data]
        batch_data_col = collate_tokens(batch_data, pad_idx=1)
        outprob = self.model.predict("language_detection", batch_data_col)
        pred_log = softmax(outprob, dim=1)
        top_k_pred_log = torch.topk(input=pred_log, k=top_k, dim=1)
        top_det = []
        for lab_list, prob in list(zip(top_k_pred_log.indices.tolist(), top_k_pred_log.values.tolist())):
            pred_lab = list(map(self.label_fn, lab_list))
            top_det.append(list(zip(pred_lab, prob)))
        pred_langs = []
        for row in top_det:
            sin_lang=[]
            for lang, conf in row:
                sin_lang.append({"language": self.languages_supported[lang], "lang_code": lang, "confidence":conf})
            pred_langs.append(sin_lang)
        pred_response = [{"input_text":query, "language": lang_data[0]['language'], "lang_code": lang_data[0]['lang_code'], "confidence":lang_data[0]['confidence'], "language_rank": lang_data} for query, lang_data in zip(input_text_list, pred_langs)]
        return pred_response
