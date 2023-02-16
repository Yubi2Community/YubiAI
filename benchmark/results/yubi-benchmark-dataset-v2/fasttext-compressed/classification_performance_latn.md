# Classification performance for fasttext-compressed on yubi-benchmark-dataset-v2

- Dataset coverage (sentences in supported languages): 80144 (100.00%)
- **Aggregated accuracy: 37.50%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |    fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|------:|------:|-----:|
|  1 | ben_Latn          | Bangla (Latin)    |              5954 |     nan     |    0.000 | 0.000 |    0 |     0 | 74190 | 5954 |
|  2 | mal_Latn          | Malayalam (Latin) |              5374 |     nan     |    0.000 | 0.000 |    0 |     0 | 74770 | 5374 |
|  3 | kan_Latn          | Kannada (Latin)   |              5068 |     nan     |    0.000 | 0.000 |    0 |     0 | 75076 | 5068 |
|  4 | tam_Latn          | Tamil (Latin)     |              4706 |     nan     |    0.000 | 0.000 |    0 |     0 | 75438 | 4706 |
|  5 | hin_Latn          | Hindi (Latin)     |              4354 |     nan     |    0.000 | 0.000 |    0 |     0 | 75790 | 4354 |
|  6 | tel_Latn          | Telugu (Latin)    |              4288 |     nan     |    0.000 | 0.000 |    0 |     0 | 75856 | 4288 |
|  7 | mal               | Malayalam         |              3992 |       0.994 |    0.996 | 0.992 | 3977 |    24 | 76128 |   15 |
|  8 | mar_Latn          | Marathi (Latin)   |              3915 |     nan     |    0.000 | 0.000 |    0 |     0 | 76229 | 3915 |
|  9 | guj_Latn          | Gujarati (Latin)  |              3749 |     nan     |    0.000 | 0.000 |    0 |     0 | 76395 | 3749 |
| 10 | kan               | Kannada           |              3431 |       0.999 |    0.997 | 0.997 | 3421 |     5 | 76708 |   10 |
| 11 | ben               | Bangla            |              3387 |       0.965 |    0.985 | 0.958 | 3336 |   121 | 76636 |   51 |
| 12 | tam               | Tamil             |              3344 |       1.000 |    1.000 | 1.000 | 3343 |     0 | 76800 |    1 |
| 13 | tel               | Telugu            |              2881 |       1.000 |    0.999 | 0.999 | 2877 |     1 | 77262 |    4 |
| 14 | ori_Latn          | Odia (Latin)      |              2798 |     nan     |    0.000 | 0.000 |    0 |     0 | 77346 | 2798 |
| 15 | nep_Latn          | Nepali (Latin)    |              2765 |     nan     |    0.000 | 0.000 |    0 |     0 | 77379 | 2765 |
| 16 | hin               | Hindi             |              2583 |       0.692 |    0.885 | 0.662 | 2286 |  1019 | 76542 |  297 |
| 17 | mar               | Marathi           |              2411 |       0.821 |    0.829 | 0.757 | 1999 |   436 | 77297 |  412 |
| 18 | guj               | Gujarati          |              2283 |       1.000 |    0.995 | 0.997 | 2271 |     1 | 77860 |   12 |
| 19 | nep               | Nepali            |              2089 |       0.964 |    0.506 | 0.656 | 1057 |    39 | 78016 | 1032 |
| 20 | pan_Latn          | Punjabi (Latin)   |              2085 |     nan     |    0.000 | 0.000 |    0 |     0 | 78059 | 2085 |
| 21 | asm_Latn          | Assamese (Latin)  |              1731 |     nan     |    0.000 | 0.000 |    0 |     0 | 78413 | 1731 |
| 22 | eng               | English           |              1564 |       0.055 |    0.996 | 0.055 | 1557 | 26694 | 51886 |    7 |
| 23 | ori               | Odia              |              1450 |       1.000 |    0.988 | 0.994 | 1433 |     0 | 78694 |   17 |
| 24 | pan               | Punjabi           |              1213 |       1.000 |    0.993 | 0.996 | 1204 |     0 | 78931 |    9 |
| 25 | urd_Latn          | Urdu (Latin)      |               993 |     nan     |    0.000 | 0.000 |    0 |     0 | 79151 |  993 |
| 26 | asm               | Assamese          |               925 |       0.993 |    0.871 | 0.925 |  806 |     6 | 79213 |  119 |
| 27 | urd               | Urdu              |               811 |       0.946 |    0.603 | 0.721 |  489 |    28 | 79305 |  322 |