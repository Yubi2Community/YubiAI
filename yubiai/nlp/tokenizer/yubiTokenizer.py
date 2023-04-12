###
### Author : Swapnil Ashok Jadhav (github:swapaj)
### Created Date : 28th Oct. 2022
###
### Model Information
###     SentencePiece Byte-Pair-Encoding tokenizer trained using fintech data.
###     Support 14 most used Indian languages. 
###     Languages : English, Indian-English, Hindi, Assamese, Bengali, Gujarati, Kannada, Malayalam
###                 Oriya, Punjabi, Tamil, Telugu, Urdu, Nepali, Marathi
###     Data consists of : News, pdfs, reports, wiki, speech-2-text data
###     Data size of : >50Gb (Reduced from ~220Gb of original data)
###                  : >384 million lines
###                  : >46 billion characters
###     Inference Speed of ~90-100 microseconds
###


from yubiai import set_model_info, verify_model_path, BASE_PATH
import sentencepiece as spm
import os
from tokenizers.implementations import SentencePieceBPETokenizer
from transformers import PreTrainedTokenizerFast


class YubiTokenizer:
    def __init__(self):
        self.model_folder_name = "yubi_fintech_bpe_text_tokenizer"
        self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name = set_model_info(self.model_folder_name)
        verify_model_path(self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name)
        
        self.model_file_name = "fintech96k_model.txt"
        self.model_file_path = "%s/%s" % (self.model_folder_path,self.model_file_name)
        self.model = self.load_model()

    def load_model(self):
        """
        Load model from default path
        """
        sp = spm.SentencePieceProcessor()
        sp.load(self.model_file_path)
        return sp

    def get_tokens(self, text):
        """
        Break the given text in list of tokens
        """
        text = text.strip().lower()
        piece_list = self.model.encode_as_pieces(text)
        return piece_list

class YubiTokenizerHF:
    def __init__(self):
        self.model_folder_name = "yubi_fintech_bpe_text_tokenizer_huggingface"
        self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name = set_model_info(self.model_folder_name)
        verify_model_path(self.model_folder_path, self.model_folder_name, self.model_zip_path, self.model_zip_name)
        
        self.model_file_path_vacab = "%s/sentencepiece-vocab.json" % self.model_folder_path
        self.model_file_path_merges = "%s/sentencepiece-merges.txt" % self.model_folder_path
        self.model = self.load_model()
        self.transformer_model = self.load_transformer_model()

    def load_model(self):
        """
        Load model from default path
        """
        sp = SentencePieceBPETokenizer.from_file(vocab_filename=self.model_file_path_vacab, merges_filename=self.model_file_path_merges)
        return sp

    def load_transformer_model(self):
        """
        Load tokenizer models which can be used in transformer training module
        """
        tmodel = PreTrainedTokenizerFast(tokenizer_object=self.model)
        return tmodel

    def get_tokens(self, text):
        """
        Break the given text in list of tokens
        """
        text = text.strip().lower()
        piece_list = self.model._tokenizer.encode(text).tokens
        return piece_list

    def get_tokens_transformer(self, text):
        """
        Get list of tokens from transformer trainer tokenizer
        """
        text = text.strip().lower()
        piece_list = self.transformer_model.tokenize(text)
        return piece_list
        