# Classification performance for fasttext on yubi-benchmark-dataset-v2

- Dataset coverage (sentences in supported languages): 80144 (100.00%)
- **Aggregated accuracy: 37.97%**

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
|  7 | mal               | Malayalam         |              3992 |       0.986 |    0.998 | 0.985 | 3986 |    57 | 76095 |    6 |
|  8 | mar_Latn          | Marathi (Latin)   |              3915 |     nan     |    0.000 | 0.000 |    0 |     0 | 76229 | 3915 |
|  9 | guj_Latn          | Gujarati (Latin)  |              3749 |     nan     |    0.000 | 0.000 |    0 |     0 | 76395 | 3749 |
| 10 | kan               | Kannada           |              3431 |       0.982 |    0.998 | 0.981 | 3424 |    64 | 76649 |    7 |
| 11 | ben               | Bangla            |              3387 |       0.967 |    0.985 | 0.960 | 3335 |   114 | 76643 |   52 |
| 12 | tam               | Tamil             |              3344 |       0.998 |    1.000 | 0.998 | 3344 |     7 | 76793 |    0 |
| 13 | tel               | Telugu            |              2881 |       0.999 |    1.000 | 0.998 | 2880 |     4 | 77259 |    1 |
| 14 | ori_Latn          | Odia (Latin)      |              2798 |     nan     |    0.000 | 0.000 |    0 |     0 | 77346 | 2798 |
| 15 | nep_Latn          | Nepali (Latin)    |              2765 |     nan     |    0.000 | 0.000 |    0 |     0 | 77379 | 2765 |
| 16 | hin               | Hindi             |              2583 |       0.762 |    0.887 | 0.726 | 2290 |   716 | 76845 |  293 |
| 17 | mar               | Marathi           |              2411 |       0.864 |    0.851 | 0.803 | 2052 |   324 | 77409 |  359 |
| 18 | guj               | Gujarati          |              2283 |       1.000 |    0.998 | 0.998 | 2278 |     1 | 77860 |    5 |
| 19 | nep               | Nepali            |              2089 |       0.942 |    0.611 | 0.725 | 1276 |    78 | 77977 |  813 |
| 20 | pan_Latn          | Punjabi (Latin)   |              2085 |     nan     |    0.000 | 0.000 |    0 |     0 | 78059 | 2085 |
| 21 | asm_Latn          | Assamese (Latin)  |              1731 |     nan     |    0.000 | 0.000 |    0 |     0 | 78413 | 1731 |
| 22 | eng               | English           |              1564 |       0.047 |    0.998 | 0.047 | 1561 | 31983 | 46597 |    3 |
| 23 | ori               | Odia              |              1450 |       0.999 |    0.995 | 0.996 | 1443 |     2 | 78692 |    7 |
| 24 | pan               | Punjabi           |              1213 |       0.999 |    0.998 | 0.998 | 1210 |     1 | 78930 |    3 |
| 25 | urd_Latn          | Urdu (Latin)      |               993 |     nan     |    0.000 | 0.000 |    0 |     0 | 79151 |  993 |
| 26 | asm               | Assamese          |               925 |       0.981 |    0.912 | 0.937 |  844 |    16 | 79203 |   81 |
| 27 | urd               | Urdu              |               811 |       0.898 |    0.630 | 0.711 |  511 |    58 | 79275 |  300 |