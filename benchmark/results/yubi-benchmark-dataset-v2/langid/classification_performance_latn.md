# Classification performance for langid on yubi-benchmark-dataset-v2

- Dataset coverage (sentences in supported languages): 80144 (100.00%)
- **Aggregated accuracy: 36.90%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben_Latn          | Bangla (Latin)    |              5954 |     nan     |    0.000 | 0.000 |    0 |    0 | 74190 | 5954 |
|  2 | mal_Latn          | Malayalam (Latin) |              5374 |     nan     |    0.000 | 0.000 |    0 |    0 | 74770 | 5374 |
|  3 | kan_Latn          | Kannada (Latin)   |              5068 |     nan     |    0.000 | 0.000 |    0 |    0 | 75076 | 5068 |
|  4 | tam_Latn          | Tamil (Latin)     |              4706 |     nan     |    0.000 | 0.000 |    0 |    0 | 75438 | 4706 |
|  5 | hin_Latn          | Hindi (Latin)     |              4354 |     nan     |    0.000 | 0.000 |    0 |    0 | 75790 | 4354 |
|  6 | tel_Latn          | Telugu (Latin)    |              4288 |     nan     |    0.000 | 0.000 |    0 |    0 | 75856 | 4288 |
|  7 | mal               | Malayalam         |              3992 |       1.000 |    1.000 | 1.000 | 3992 |    0 | 76152 |    0 |
|  8 | mar_Latn          | Marathi (Latin)   |              3915 |     nan     |    0.000 | 0.000 |    0 |    0 | 76229 | 3915 |
|  9 | guj_Latn          | Gujarati (Latin)  |              3749 |     nan     |    0.000 | 0.000 |    0 |    0 | 76395 | 3749 |
| 10 | kan               | Kannada           |              3431 |       1.000 |    1.000 | 1.000 | 3431 |    0 | 76713 |    0 |
| 11 | ben               | Bangla            |              3387 |       0.908 |    0.953 | 0.888 | 3229 |  329 | 76428 |  158 |
| 12 | tam               | Tamil             |              3344 |       0.999 |    1.000 | 0.999 | 3344 |    2 | 76798 |    0 |
| 13 | tel               | Telugu            |              2881 |       1.000 |    1.000 | 1.000 | 2881 |    0 | 77263 |    0 |
| 14 | ori_Latn          | Odia (Latin)      |              2798 |     nan     |    0.000 | 0.000 |    0 |    0 | 77346 | 2798 |
| 15 | nep_Latn          | Nepali (Latin)    |              2765 |     nan     |    0.000 | 0.000 |    0 |    0 | 77379 | 2765 |
| 16 | hin               | Hindi             |              2583 |       0.719 |    0.771 | 0.650 | 1992 |  777 | 76784 |  591 |
| 17 | mar               | Marathi           |              2411 |       0.709 |    0.818 | 0.657 | 1973 |  810 | 76923 |  438 |
| 18 | guj               | Gujarati          |              2283 |       1.000 |    1.000 | 1.000 | 2283 |    1 | 77860 |    0 |
| 19 | nep               | Nepali            |              2089 |       0.770 |    0.565 | 0.594 | 1180 |  352 | 77703 |  909 |
| 20 | pan_Latn          | Punjabi (Latin)   |              2085 |     nan     |    0.000 | 0.000 |    0 |    0 | 78059 | 2085 |
| 21 | asm_Latn          | Assamese (Latin)  |              1731 |     nan     |    0.000 | 0.000 |    0 |    0 | 78413 | 1731 |
| 22 | eng               | English           |              1564 |       0.146 |    0.991 | 0.146 | 1550 | 9075 | 69505 |   14 |
| 23 | ori               | Odia              |              1450 |       1.000 |    1.000 | 1.000 | 1450 |    0 | 78694 |    0 |
| 24 | pan               | Punjabi           |              1213 |       1.000 |    1.000 | 1.000 | 1213 |    0 | 78931 |    0 |
| 25 | urd_Latn          | Urdu (Latin)      |               993 |     nan     |    0.000 | 0.000 |    0 |    0 | 79151 |  993 |
| 26 | asm               | Assamese          |               925 |       0.790 |    0.643 | 0.648 |  595 |  158 | 79061 |  330 |
| 27 | urd               | Urdu              |               811 |       1.000 |    0.570 | 0.726 |  462 |    0 | 79333 |  349 |