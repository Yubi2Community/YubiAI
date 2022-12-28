# Language Detection

## Yubi Languange Detection Model

* Using [YubiTokenzier](https://github.com/credavenue/yubi_ds_capability/tree/language_detection/cernunnos/nlp/tokenizer) Byte-Pair-Encoding tokenizer trained using fintech data.
* Support 14 most used Indian languages and Transliterated versions of these languages.
* Data consists of : News & transliterated text
* Data size of
    * >12Gb
* Inference Speed of ~10-50 microseconds
* [How it was trained ?](https://docs.google.com/document/d/1x_YxhRjAT4sFudmmTIdREqo7WNARf_cteeOYTNFAfdE/edit?usp=sharing)
* Where it can be useful ?
    * When we want to detect document/coversation language.

## How to import and use Yubi Languagae Detection

```python

from YubiAI.nlp.language_detection.yubiLanguageDetection import LanguageDetection

model = LanguageDetection()

### English text tokenisation
text = "CredAvenue is building India’s first and largest de-facto operating system for the discovery, investment, fulfilment, and collection of any debt solution."
print(model.detect_language(input_text=text, top_k=5))
### Output :   
#   {'input_text': 'credavenue is building india’s first and largest de-facto operating system for the discovery, investment, fulfilment, and collection of any debt solution.',
#  'language': 'English',
#  'lang_code': 'en',
#  'confidence': 0.9990460276603699,
#  'language_rank': [{'language': 'English',
#    'lang_code': 'en',
#    'confidence': 0.9990460276603699},
#   {'language': 'Gujarati',
#    'lang_code': 'gu',
#    'confidence': 0.00011310971603961661},
#   {'language': 'Transliterated Assamese',
#    'lang_code': 'tr_as',
#    'confidence': 9.215490717906505e-05},
#   {'language': 'Transliterated Telugu',
#    'lang_code': 'tr_te',
#    'confidence': 8.09595367172733e-05},
#   {'language': 'Transliterated Hindi',
#    'lang_code': 'tr_hi',
#    'confidence': 7.598803495056927e-05}]}

### Batch Pridiction
batch_text = [
                "A paragraph is a collection of words strung together to make a longer unit than a sentence.", 
                "पत्थरों के बीच छुपे मेंढक ने दिया आंखों को धोखा, चकमा देने वाली तस्वीर ने घुमा दिया दिमाग",
                "Meeru ela unnaru?",
                "Namaskaram, meeru lopaliki  ravachu."
            ]
print(model.detect_language_batch(input_text_list=batch_text, top_k=2))
### Output : 
# [{'input_text': 'A paragraph is a collection of words strung together to make a longer unit than a sentence.',
#   'language': 'English',
#   'lang_code': 'en',
#   'confidence': 0.9993940591812134,
#   'language_rank': [{'language': 'English',
#     'lang_code': 'en',
#     'confidence': 0.9993940591812134},
#    {'language': 'Hindi',
#     'lang_code': 'hi',
#     'confidence': 7.835876021999866e-05}]},
#  {'input_text': 'पत्थरों के बीच छुपे मेंढक ने दिया आंखों को धोखा, चकमा देने वाली तस्वीर ने घुमा दिया दिमाग',
#   'language': 'Hindi',
#   'lang_code': 'hi',
#   'confidence': 0.9999706745147705,
#   'language_rank': [{'language': 'Hindi',
#     'lang_code': 'hi',
#     'confidence': 0.9999706745147705},
#    {'language': 'Marathi',
#     'lang_code': 'mr',
#     'confidence': 1.7655293049756438e-05}]},
#  {'input_text': 'Meeru ela unnaru?',
#   'language': 'Transliterated Telugu',
#   'lang_code': 'tr_te',
#   'confidence': 0.9984096884727478,
#   'language_rank': [{'language': 'Transliterated Telugu',
#     'lang_code': 'tr_te',
#     'confidence': 0.9984096884727478},
#    {'language': 'Transliterated Tamil',
#     'lang_code': 'tr_ta',
#     'confidence': 0.0009650049032643437}]},
#  {'input_text': 'Namaskaram, meeru lopaliki  ravachu.',
#   'language': 'Transliterated Telugu',
#   'lang_code': 'tr_te',
#   'confidence': 0.9992443323135376,
#   'language_rank': [{'language': 'Transliterated Telugu',
#     'lang_code': 'tr_te',
#     'confidence': 0.9992443323135376},
#    {'language': 'Transliterated Tamil',
#     'lang_code': 'tr_ta',
#     'confidence': 0.00036794054904021323}]}]
```