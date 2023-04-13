
### Model Main Version 
__version__ = "04.23"


### Cernunnos base path constant
import pathlib
#BASE_PATH = pathlib.Path(__file__).parent.absolute()
BASE_PATH = pathlib.Path.home().joinpath(".cache", "yubiai").absolute()


### Hosted Model List
model_list = {
    "yulan-e8-v2" : 
                    {"url":"https://drive.google.com/file/d/1XFJTHM8MWag4QbHJ0p5vSnAGZq4iWmS8/view?usp=share_link", 
                    "filename":"yulan-e8-v2.zip"},
    "yulan-e4-v2" : 
                    {"url":"https://drive.google.com/file/d/17EEAdasvj7jIKRMMaq4YxCaetgvsVuON/view?usp=share_link", 
                    "filename":"yulan-e4-v2.zip"},
    "yulan-e4-v1" : 
                    {"url":"https://drive.google.com/file/d/1Kjn6-XOxHw9mouenbtXSp7QU95D_G-eC/view?usp=share_link", 
                    "filename":"yulan-e4-v1.zip"},
    "yubibert_e8_small" : 
                    {"url":"https://drive.google.com/file/d/1HlBQDxplP2sJU-zHQfDnM1PFuMFXit9I/view?usp=share_link", 
                    "filename":"yubibert_e8_small.zip"},
    "yubibert_e4_micro" : 
                    {"url":"https://drive.google.com/file/d/1LxpI4AerxHMV5xxA4Wcs19XwHX-7ohxA/view?usp=share_link", 
                    "filename":"yubibert_e4_micro.zip"},
    "yubi_fintech_bpe_text_tokenizer" : 
                    {"url":"https://drive.google.com/file/d/1-hBwyJzY3tx1HzqrSfo1N17sGyrC07Li/view?usp=share_link", 
                    "filename":"yubi_fintech_bpe_text_tokenizer.zip"},
    "yubi_fintech_bpe_text_tokenizer_huggingface" : 
                    {"url":"https://drive.google.com/file/d/1UPBjD_Csj-Mqhb6ujp0VisEADyCYxsWl/view?usp=share_link", 
                    "filename":"yubi_fintech_bpe_text_tokenizer_huggingface.zip"},
    "yubi_document_segmentation_v1" : 
                    {"url":"https://drive.google.com/file/d/1KFK_HdXqzVaR8B4ADO26x396c606mlPP/view?usp=share_link", 
                    "filename":"yubi_document_segmentation_v1.zip"},
    "yubi_document_segmentation_aug_v1" : 
                    {"url":"https://drive.google.com/file/d/1Z3V8nzUau3K1HozI7fYP19RxQkTdnq4f/view?usp=share_link", 
                    "filename":"yubi_document_segmentation_aug_v1.zip"},
    "yubi_document_segmentation_v2" : 
                    {"url":"https://drive.google.com/file/d/1dDt_w30P09V9VTeme1ZxKxtjg2aM4kdx/view?usp=share_link", 
                    "filename":"yubi_document_segmentation_v2.zip"},
    "TrueCaser_transformer_wmt_en_de_big_t2t" : 
                    {"url":"https://drive.google.com/file/d/1VNXrYw7eE4R5hz-rhV0ZACR_e7jOMuJL/view?usp=share_link", 
                    "filename":"TrueCaser_transformer_wmt_en_de_big_t2t.zip"},
    "SkewDetection_ResNet101V2_45-135" : 
                    {"url":"https://drive.google.com/file/d/1sVoOsDiQSbkB9E-_FhFbcvNJficGQsT-/view?usp=share_link", 
                    "filename":"SkewDetection_ResNet101V2_45-135.zip"},
    "SkewDetection_ResNet101V2_0-90" : 
                    {"url":"https://drive.google.com/file/d/1JMOU4GdP3PpubeO_oMlxNpLA811lo5Dr/view?usp=share_link", 
                    "filename":"SkewDetection_ResNet101V2_0-90.zip"},
    "Quad4Detection_ResNet101V2_45-135" : 
                    {"url":"https://drive.google.com/file/d/1LvzalJAKwQ8RA0OAg343D6rBtIqy3zin/view?usp=share_link", 
                    "filename":"Quad4Detection_ResNet101V2_45-135.zip"},
    "Quad4Detection_ResNet101V2_0-90" : 
                    {"url":"https://drive.google.com/file/d/1jmkB4tk8D5i2-LF0vuaIfcR-Pa7quX2t/view?usp=share_link", 
                    "filename":"Quad4Detection_ResNet101V2_0-90.zip"},
    "character2text_transformer_wmt_en_de_big_t2t" : 
                    {"url":"https://drive.google.com/file/d/1r3VqG4fzoq6fAGHrwCXQEpFkRJxx8RZw/view?usp=share_link", 
                    "filename":"character2text_transformer_wmt_en_de_big_t2t.zip"}
}


### Download from Public Shared Yubiai google drive folder
import gdown
import os

def set_model_info(model_name):
    """
    Generic model zip and folder naming along with their paths
    """
    model_folder_name = model_name
    model_folder_path = "%s/models/%s" % (BASE_PATH, model_folder_name)
    model_zip_path = "%s/models/" % BASE_PATH
    model_zip_name = "%s.zip" % model_folder_name
    return model_folder_path, model_folder_name, model_zip_path, model_zip_name
    

def download_model_zip(model_name):
    if model_name in model_list:
        model_url = model_list[model_name]['url']
        model_file_name = model_list[model_name]['filename']
        model_output_path = "%s/models/%s" % (BASE_PATH, model_file_name)
        gdown.download(model_url, model_output_path, quiet=False, fuzzy=True)
    else:
        print("Please check and correct 'model_name' parameter!")
    return

def verify_model_path(model_folder_path, model_folder_name, model_zip_path, model_zip_name):
    """
    Verify if model folder exists at default path.
    If not then download the same from default ftp location
    """
    if os.path.exists(model_folder_path):
        print("Model Path exist !!")
    elif os.path.exists(f"{model_zip_path}/{model_zip_name}"):
        print("Model Path exist(ZIP format) !!")
        os.system("cd %s; unzip %s; rm -f %s; cd -;" % (model_zip_path, model_zip_name, model_zip_name))
    else:
        print("Model Path do not exist !!")
        download_model_zip(model_folder_name)
        os.system("cd %s; unzip %s; rm -f %s; cd -;" % (model_zip_path, model_zip_name, model_zip_name))
