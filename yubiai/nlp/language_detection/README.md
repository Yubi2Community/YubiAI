# Language Detection

## YuLan - Yubi Languange Detection Model

* Using [YubiTokenzier](../tokenizer/) Byte-Pair-Encoding tokenizer trained using fintech data.
* Support 14 most used Indian languages and Transliterated versions of these languages.
* Data consists of : News & transliterated text
* Data size of >12Gb
* Inference Speed of ~10-50 microseconds
* Where it can be useful ?
    * To detect document language
    * To detect chatbot conversation language
    * To detect speech-bot conversation language after speech-2-text
    * Differentiate between text vs roman-transliterated-text

## How to import and use YuLan model
* **LanguageDetection** calss takes two arguments **task_name** and **use_gpu**.
    * **task_name**: yulan model name (ex yulan-e4-v1, yulan-e4-v2 & yulan-e8-v2).
    * **use_gpu**: whether to use GPU or not.
* **detect_language** method takes two arguments **input_text** and  **top_k**.
    * **input_text**: input sentence.
    * **top_k**: returns top k languanges.
* **detect_language_batch** method takes two arguments **input_text_list** and  **top_k**.
    * **input_text_list**: input list of sentences.
    * **top_k**: returns top k languanges.

```python

from yubiai.nlp.language_detection.yubiLanguageDetection import LanguageDetection

model = LanguageDetection(task_name="yulan-e4-v2", use_gpu=False)

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