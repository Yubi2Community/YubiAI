# Classification performance for yubilangdetect-v1 on yubi-benchmark-dataset-v1

- Dataset coverage (sentences in supported languages): 60522 (100.00%)
- **Aggregated accuracy: 98.28%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben               | Bangla            |              4363 |       0.999 |    1.000 | 0.999 | 4363 |    6 | 56153 |    0 |
|  2 | ben_Latn          | Bangla (Latin)    |              4328 |       0.970 |    0.976 | 0.959 | 4224 |  129 | 56065 |  104 |
|  3 | hin_Latn          | Hindi (Latin)     |              3071 |       0.992 |    0.977 | 0.980 | 2999 |   25 | 57426 |   72 |
|  4 | hin               | Hindi             |              2971 |       0.997 |    0.999 | 0.997 | 2969 |    8 | 57543 |    2 |
|  5 | kan               | Kannada           |              2845 |       1.000 |    1.000 | 1.000 | 2845 |    0 | 57677 |    0 |
|  6 | kan_Latn          | Kannada (Latin)   |              2806 |       0.958 |    0.943 | 0.931 | 2645 |  116 | 57600 |  161 |
|  7 | mal_Latn          | Malayalam (Latin) |              2547 |       0.950 |    0.953 | 0.929 | 2428 |  127 | 57848 |  119 |
|  8 | eng               | English           |              2545 |       0.997 |    0.999 | 0.997 | 2542 |    7 | 57970 |    3 |
|  9 | mar_Latn          | Marathi (Latin)   |              2540 |       0.994 |    0.981 | 0.984 | 2492 |   16 | 57966 |   48 |
| 10 | guj               | Gujarati          |              2533 |       1.000 |    1.000 | 1.000 | 2533 |    0 | 57989 |    0 |
| 11 | guj_Latn          | Gujarati (Latin)  |              2510 |       0.931 |    0.951 | 0.909 | 2388 |  178 | 57834 |  122 |
| 12 | mar               | Marathi           |              2498 |       0.994 |    0.997 | 0.992 | 2490 |   15 | 58009 |    8 |
| 13 | mal               | Malayalam         |              2467 |       1.000 |    1.000 | 1.000 | 2467 |    0 | 58055 |    0 |
| 14 | tel               | Telugu            |              2376 |       1.000 |    1.000 | 1.000 | 2376 |    1 | 58145 |    0 |
| 15 | tel_Latn          | Telugu (Latin)    |              2296 |       0.929 |    0.929 | 0.897 | 2134 |  164 | 58062 |  162 |
| 16 | tam               | Tamil             |              2276 |       1.000 |    1.000 | 1.000 | 2276 |    0 | 58246 |    0 |
| 17 | tam_Latn          | Tamil (Latin)     |              2261 |       0.974 |    0.985 | 0.967 | 2227 |   60 | 58201 |   34 |
| 18 | ori               | Odia              |              2165 |       1.000 |    1.000 | 1.000 | 2165 |    0 | 58357 |    0 |
| 19 | ori_Latn          | Odia (Latin)      |              2137 |       0.963 |    0.964 | 0.945 | 2059 |   80 | 58305 |   78 |
| 20 | pan               | Punjabi           |              1508 |       1.000 |    1.000 | 1.000 | 1508 |    0 | 59014 |    0 |
| 21 | pan_Latn          | Punjabi (Latin)   |              1463 |       0.950 |    0.957 | 0.931 | 1400 |   73 | 58986 |   63 |
| 22 | asm               | Assamese          |              1412 |       1.000 |    0.996 | 0.998 | 1406 |    0 | 59110 |    6 |
| 23 | asm_Latn          | Assamese (Latin)  |              1375 |       0.995 |    0.986 | 0.988 | 1356 |    7 | 59140 |   19 |
| 24 | nep               | Nepali            |              1090 |       0.998 |    0.999 | 0.998 | 1089 |    2 | 59430 |    1 |
| 25 | nep_Latn          | Nepali (Latin)    |              1064 |       0.992 |    0.989 | 0.986 | 1052 |    9 | 59449 |   12 |
| 26 | urd               | Urdu              |               544 |       1.000 |    1.000 | 1.000 |  544 |    0 | 59978 |    0 |
| 27 | urd_Latn          | Urdu (Latin)      |               531 |       0.969 |    0.953 | 0.947 |  506 |   16 | 59975 |   25 |