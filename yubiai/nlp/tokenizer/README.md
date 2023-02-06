# YubiTokenizer

* [SentencePiece](https://github.com/google/sentencepiece) Byte-Pair-Encoding tokenizer trained using fintech data.
* Support 14 most used Indian languages : `English, Indian-English, Hindi, Assamese, Bengali, Gujarati, Kannada, Malayalam, Oriya, Punjabi, Tamil, Telugu, Urdu, Nepali, Marathi`
* Data consists of : News, pdfs, reports, wiki, speech-2-text data & transliterated text
* Data size of
    * ~50Gb (Reduced from ~220Gb of original data)
    * ~384 million lines
    * ~46 billion characters
* Inference Speed of ~90-100 microseconds
* Where it can be useful ?
    * When we need to tokenise and index any fintech related text/document
    * Replacement of [GPT-tokenizer and BERT-tokenizer](https://huggingface.co/docs/transformers/main_classes/tokenizer) ... as it is specifically trained on FinTech data.
    * To process indian languages text or speech

<br>

## How to load and use YubiTokenizer

```python

import sys
sys.path.append("/parent/directory/path/of/yubiai/")

from yubiai.nlp.tokenizer.yubiTokenizer import YubiTokenizer
tokenizer = YubiTokenizer()

text = "CredAvenue is building India’s first and largest de-facto operating system for the discovery, investment, fulfilment, and collection of any debt solution."

tokenizer.get_tokens(text)
### ['▁cred', 'aven', 'ue', '▁is', '▁building', '▁india', '’', 's', '▁first', '▁and', '▁largest', '▁de', '-', 'fact', 'o', '▁operating', '▁system', '▁for', '▁the', '▁discovery', ',', '▁investment', ',', '▁fulfilment', ',', '▁and', '▁collection', '▁of', '▁any', '▁debt', '▁solution', '.']


```

## How to use YubiTokenizer with HuggingFace

We had to create HuggingFace supported version of our tokenizer using `sp2hf.py` as we realised SentencePiece has no direct support in training or fine-tuning models.
We can either `tokenizers` version of a model OR `transformers` version of model when needed in training accordingly.

```python

import sys
sys.path.append("/parent/directory/path/of/yubiai/")

from yubiai.nlp.tokenizer.yubiTokenizer import YubiTokenizerHF
tokenizer = YubiTokenizerHF()

text = "CredAvenue is building India’s first and largest de-facto operating system for the discovery, investment, fulfilment, and collection of any debt solution."

tokenizer.get_tokens(text)
### ['▁cred', 'aven', 'ue', '▁is', '▁building', '▁india', '’', 's', '▁first', '▁and', '▁largest', '▁de', '-', 'fact', 'o', '▁operating', '▁system', '▁for', '▁the', '▁discovery', ',', '▁investment', ',', '▁fulfilment', ',', '▁and', '▁collection', '▁of', '▁any', '▁debt', '▁solution', '.']

tokenizer.get_tokens_transformer(text)
### ['▁cred', 'aven', 'ue', '▁is', '▁building', '▁india', '’', 's', '▁first', '▁and', '▁largest', '▁de', '-', 'fact', 'o', '▁operating', '▁system', '▁for', '▁the', '▁discovery', ',', '▁investment', ',', '▁fulfilment', ',', '▁and', '▁collection', '▁of', '▁any', '▁debt', '▁solution', '.']

type(tokenizer.model)
### <class 'tokenizers.implementations.sentencepiece_bpe.SentencePieceBPETokenizer'>

type(tokenizer.transformer_model)
### <class 'transformers.tokenization_utils_fast.PreTrainedTokenizerFast'>

```