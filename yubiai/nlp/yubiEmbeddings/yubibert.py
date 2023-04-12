###
### Author : Swapnil Ashok Jadhav (github:swapaj)
### Created Date : 28th Oct. 2022
### Credit for the training library: https://github.com/facebookresearch/fairseq/blob/main/examples/roberta/README.md
### 


from yubiai import set_model_info,  verify_model_path
import os
from fairseq.models.roberta import RobertaModel
import numpy as np
import re
import torch


class YubiBERT:
    def __init__(self, use_gpu=False, model_type="yubibert_e4_micro"):
        self.use_gpu = use_gpu

        self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name = set_model_info(model_type)
        verify_model_path(self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name)
        self.model = self.load_model()

    def load_model(self):
        """
        Load model from default path
        """
        model = RobertaModel.from_pretrained(self.model_folder_path, checkpoint_file="checkpoint_best.pt", data_name_or_path="./bin_data", bpe="sentencepiece")
        model.eval()
        if self.use_gpu == True:
            model.cuda()
        return model

    def getEmbeddings(self, text, normalize=True):
        """
        Returns vector of size 512
        If you set normalize to True .. it will return unit normalized vector else the the raw vector
        Normalize set to True is recommended
        """
        token_outmap = self.getTokens(text)
        tokens = token_outmap['encoded_tokens']
        if self.use_gpu == True:
            last_layer_features = self.model.extract_features(tokens[:511]).detach().cpu().numpy()
        else:
            last_layer_features = self.model.extract_features(tokens[:511]).detach().numpy()
        avg_feature = np.mean(last_layer_features[0], axis=0)
        if normalize is True:
            avg_feature = avg_feature / np.linalg.norm(avg_feature)
        outmap = {}
        outmap['encoded_tokens'] = tokens
        outmap['decoded_tokens'] = token_outmap['decoded_tokens']
        outmap['normalize'] = normalize
        outmap['embedding'] = avg_feature
        return outmap

    def getEmbeddings_last_n_layers(self, text, last_n_layers=1):
        """
        Returns vector of size 512*n for last n layers .. concatenated
        Here layers mean .. embedding layer after each transformer/encoder block
        In many SOTA Glue tasks Google has used last 4 layers concatenated.
        """
        token_outmap = self.getTokens(text)
        tokens = token_outmap['encoded_tokens']
        all_layers = self.model.extract_features(tokens, return_all_hiddens=True)
        nlayer_vector_map = {}
        concatenated_vector = []
        for i in range(0, last_n_layers*-1, -1):
            if self.use_gpu == True:
                avg_feature = np.mean(all_layers[i-1].detach().cpu().numpy()[0], axis=0)
            else:
                avg_feature = np.mean(all_layers[i-1].detach().numpy()[0], axis=0)
            nlayer_vector_map[i-1] = avg_feature
            concatenated_vector = concatenated_vector + list(avg_feature)
        outmap = {}
        outmap['encoded_tokens'] = tokens
        outmap['decoded_tokens'] = token_outmap['decoded_tokens']
        outmap['nlayer_vector_map'] = nlayer_vector_map
        outmap['concatenated_vector'] = concatenated_vector
        return outmap

    def getTokens(self, text):
        """
        Tokenize given text and also decode individually to return text token slices
        """
        text = re.sub("\s+", " ", text.lower()).strip()
        etokens = self.model.encode(text)
        dtokens = [self.model.decode(torch.as_tensor(np.array([tkn]))) for tkn in etokens]
        outmap = {"encoded_tokens": etokens, "decoded_tokens": dtokens}
        return outmap

    def roberta_fill_in_the_blank_task(self, text, topk=10):
        """
        Given a <mask> to fill in .. returns output array with possible replacable words and their scores.
        Please add only one entry of <mask>
        """
        text = re.sub("\s+", " ", text.lower()).strip()
        if "<mask>" in text:
            return self.model.fill_mask(text, topk=topk)
        return []

