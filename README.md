# YubiAI

State-of-the-art models in AI,ML,NLP & Vision for FinTech community by Yubi's Data Science Team.
<br>
<br>

<details>
<summary>What's new in NLP</summary>
<p>

* Oct 2022
    * [YubiTokenizer trained on FinTech multilingual data](./yubiai/nlp/tokenizer/)
    * [YubiBERT Micro Encoder4](./yubiai/nlp/yubiEmbeddings/)
* Nov 2022
    * [YubiBERT Small Encoder8](./yubiai/nlp/yubiEmbeddings/)
    * [HuggingFace Supported YubiTokenizers](./yubiai/nlp/tokenizer/)
* Dec 2022
    * [YuLan V1 - Yubi's Text Language Detection](./yubiai/nlp/language_detection/)
    * [TrueCaser Model v1](./yubiai/nlp/seq2seq/)
    * [Character-2-Text generation Model v1](./yubiai/nlp/seq2seq/)
* Feb 2023
    * [YuLan V2 - Yubi's Text Language Detection](./yubiai/nlp/language_detection/)


</p>
</details>
</br>

<details><summary>What's new in Vision</summary><p>

* January 2023
    * [Image Augmentations (Random rotate & croppings)](./yubiai/vision/utility/)
    * [Document Skew Detection v1](./yubiai/vision/skew_detection/)
* March 2023
    * [Fintech Document Segmentation model v1](./yubiai/vision/document_segmentation/)

</p></details>
</br>
<br>


## Environment
* Models files hosted on FTP server and are downloaded when constructor is called
* Curently tested on `Ubuntu 20.04`, `MacOS 12.3` and `python >=3.7`

## How to install package
* Clone the git repository or download zip/tar files and unzip
```
cd /parent/directory/path/of/YubiAI/
```
* Install only NLP dependencies
```
pip install ".[nlp]"
```
* Install only Vision dependencies
```
pip install ".[cv]"
```
* Install both NLP & Vision dependencies
```
pip install ".[nlp,cv]"
```

## How to use package
* Clone the git repository or download zip/tar files and unzip
* You need to append the repo path using `sys`
* Remaining import & code would remain same.

```python

import sys
sys.path.append("/parent/directory/path/of/yubiai/")

from yubiai.nlp.tokenizer.yubiTokenizer import YubiTokenizer
tokenizer = YubiTokenizer()

```

<br>
