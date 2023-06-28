# Text NSFW Detection


* Using [YubiTokenzier](https://github.com/credavenue/yubi_ds_capability/tree/language_detection/cernunnos/nlp/tokenizer) Byte-Pair-Encoding tokenizer trained using fintech data.
* Support 14 most used Indian languages and Transliterated versions of these languages.
* Data consists of : public comments on social media platform
* Data size of
    * > 10 million comments
* Inference Speed of ~10-50 microseconds
* Where it can be useful ?
    * When we want to detect NSFW text.

## How to import and use NSFW model

```python

from yubiai.nlp.nsfw_text.textNsfwDetection import NSFWDetection

model = NSFWDetection()

###Class - sfw -> Safe for Work
###Class - nsfw -> Not Safe for Work

### English text tokenisation
text = "good initiatative very nice."
print(model.detect_NSFW(input_text=text))
### OUTPUT :    {'sfw': 1.0, 'nsfw': 0.0}
text = 'ghar ke samne kutta bokata hain isko roti do chup ho jayega'
print(model.detect_NSFW(input_text=text))
### OUTPUT :    {'sfw': 0.0, 'nsfw': 1.0}
```