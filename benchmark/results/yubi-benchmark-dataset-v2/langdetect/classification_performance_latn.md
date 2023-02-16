# Classification performance for langdetect on yubi-benchmark-dataset-v2

- Dataset coverage (sentences in supported languages): 80144 (100.00%)
- **Aggregated accuracy: 35.69%**

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
| 11 | ben               | Bangla            |              3387 |       0.785 |    1.000 | 0.785 | 3387 |  927 | 75830 |    0 |
| 12 | tam               | Tamil             |              3344 |       1.000 |    1.000 | 1.000 | 3344 |    0 | 76800 |    0 |
| 13 | tel               | Telugu            |              2881 |       1.000 |    1.000 | 1.000 | 2881 |    0 | 77263 |    0 |
| 14 | ori_Latn          | Odia (Latin)      |              2798 |     nan     |    0.000 | 0.000 |    0 |    0 | 77346 | 2798 |
| 15 | nep_Latn          | Nepali (Latin)    |              2765 |     nan     |    0.000 | 0.000 |    0 |    0 | 77379 | 2765 |
| 16 | hin               | Hindi             |              2583 |       0.864 |    0.797 | 0.778 | 2059 |  325 | 77236 |  524 |
| 17 | mar               | Marathi           |              2411 |       0.802 |    0.898 | 0.767 | 2164 |  535 | 77198 |  247 |
| 18 | guj               | Gujarati          |              2283 |       1.000 |    1.000 | 1.000 | 2283 |    0 | 77861 |    0 |
| 19 | nep               | Nepali            |              2089 |       0.712 |    0.789 | 0.650 | 1649 |  666 | 77389 |  440 |
| 20 | pan_Latn          | Punjabi (Latin)   |              2085 |     nan     |    0.000 | 0.000 |    0 |    0 | 78059 | 2085 |
| 21 | asm_Latn          | Assamese (Latin)  |              1731 |     nan     |    0.000 | 0.000 |    0 |    0 | 78413 | 1731 |
| 22 | eng               | English           |              1564 |       0.344 |    0.984 | 0.343 | 1539 | 2932 | 75648 |   25 |
| 23 | ori               | Odia              |              1450 |     nan     |    0.000 | 0.000 |    0 |    0 | 78694 | 1450 |
| 24 | pan               | Punjabi           |              1213 |       0.654 |    1.000 | 0.654 | 1213 |  642 | 78289 |    0 |
| 25 | urd_Latn          | Urdu (Latin)      |               993 |     nan     |    0.000 | 0.000 |    0 |    0 | 79151 |  993 |
| 26 | asm               | Assamese          |               925 |     nan     |    0.000 | 0.000 |    0 |    0 | 79219 |  925 |
| 27 | urd               | Urdu              |               811 |       1.000 |    0.820 | 0.901 |  665 |    0 | 79333 |  146 |