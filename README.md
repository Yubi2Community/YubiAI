# YubiAI

State-of-the-art models in AI,ML,NLP & Vision for FinTech community by Yubi Data Science Team.
<br>

## Environment
* Models files hosted on FTP server and are downloaded when constructor is called
* Curently tested on `Ubuntu 20.04`, `MacOS 12.3` and `python >=3.7`

## How to use package
* Clone the git repository or download zip/tar files and unzip
* You need to append the repo path using `sys`
* Remaining import & code would remain same.

```python

import sys
sys.path.append("/parent/directory/path/of/yubiai/")

from YubiAI.nlp.tokenizer.yubiTokenizer import YubiTokenizer
tokenizer = YubiTokenizer()

```

<br>
<details>
<summary>What's new in NLP</summary>
<p>

* Oct 2022
    * [YubiTokenizer trained on FinTech multilingual data](./nlp/tokenizer/)
    * [YubiBERT Micro Encoder4](./nlp/yubiEmbeddings/)
* Nov 2022
    * [YubiBERT Small Encoder8](./nlp/yubiEmbeddings/)
    * [HuggingFace Supported YubiTokenizers](./nlp/tokenizer/)
* Dec 2022
    * [Yubi Text Language Detection](./nlp/language_detection/)

</p>
</details>

</br>