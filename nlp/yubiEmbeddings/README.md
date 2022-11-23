# YubiBERT

## YubiBERT (yubibert_e4_micro)
* In this version of pretrained RoBERTa model - 
    * Only 4 encoder have been used for quick training and so that model can fit in 16gb of gpu ram with enough batch size
    * Other parameters are set accordingly like attention-size, attention-heads, learning-rate etc
    * 230 Gb of raw text data used 
    * Our own [yubi sentence tokenization](../tokenizer/) is used during preprocess steps
## YubiBERT (yubibert_e8_small)
* In this version of pretrained RoBERTa model - 
    * 8 encoder have been used. We used `g5` instance with 4x gpu and each had 24gb vram.
    * 230 Gb of raw text data used 
    * Our own [yubi sentence tokenization](../tokenizer/) is used during preprocess steps

<br>

## How to load and use YubiBERT-Micro-Encoder4

You can define `model_type` parameter to load specific model.
Available model types are : `yubibert_e4_micro` and `yubibert_e8_small`

```python

import sys
sys.path.append("/parent/directory/path/of/yubiai/")

from YubiAI.nlp.yubiEmbeddings.yubibert import YubiBERT

ybert = YubiBERT(use_gpu=False, model_type='yubibert_e4_micro')

input_text = "CredAvenue is India’s fastest Fintech unicorn."

print(ybert.getEmbeddings(input_text))
### {'encoded_tokens': tensor([0,30371,9233,3026,18,61,33,15,5426,8605,41599,6,2]), 
###  'decoded_tokens': ['', 'cred', 'aven', 'ue', 'is', 'india', '’', 's', 'fastest', 'fintech', 'unicorn', '.', ''], 
###  'normalize': True, 
###  'embedding': array([-7.04746041e-03, -1.40993064e-02,  9.68784280e-03,  2.14456767e-03,
###        -3.47816362e-03,  1.25515764e-03, -2.40275939e-03,  3.57235223e-03,
###        ...
###        -1.16933743e-02, -5.76630747e-03,  9.58391698e-04,  1.34846689e-02],
###       dtype=float32)}


masked_text = "CredAvenue is <mask>’s fastest Fintech unicorn."
print(ybert.roberta_fill_in_the_blank_task(masked_text))
### [('credavenue is india’s fastest fintech unicorn.', 0.73644, ' india'),
### ('credavenue is world’s fastest fintech unicorn.', 0.17053, ' world'), 
### ('credavenue is america’s fastest fintech unicorn.', 0.03784, ' america'), 
### ('credavenue is asia’s fastest fintech unicorn.', 0.01167, ' asia'), 
### ('credavenue is australia’s fastest fintech unicorn.', 0.00319, ' australia'), 
### ('credavenue is europe’s fastest fintech unicorn.', 0.00307, ' europe'), 
### ('credavenue is china’s fastest fintech unicorn.', 0.00305, ' china'), 
### ('credavenue is singapore’s fastest fintech unicorn.', 0.00193, ' singapore'), 
### ('credavenue is canada’s fastest fintech unicorn.', 0.00161, ' canada'), 
### ('credavenue is britain’s fastest fintech unicorn.', 0.00148, ' britain')]

```

## How to finetune for classification and use example

Please check these two files for more details [finetuning shell script](./finetune_yubibert_classification_example.sh) and [sample python code](./finetune_yubibert_classification_example.py)