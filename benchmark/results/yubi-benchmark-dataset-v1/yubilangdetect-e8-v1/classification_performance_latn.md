# Classification performance for yubilangdetect-e8-v1 on yubi-benchmark-dataset-v1

- Dataset coverage (sentences in supported languages): 60522 (100.00%)
- **Aggregated accuracy: 98.82%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben               | Bangla            |              4363 |       0.998 |    1.000 | 0.998 | 4363 |    8 | 56151 |    0 |
|  2 | ben_Latn          | Bangla (Latin)    |              4328 |       0.981 |    0.984 | 0.973 | 4258 |   81 | 56113 |   70 |
|  3 | hin_Latn          | Hindi (Latin)     |              3071 |       0.993 |    0.983 | 0.985 | 3020 |   22 | 57429 |   51 |
|  4 | hin               | Hindi             |              2971 |       0.996 |    0.998 | 0.995 | 2966 |   11 | 57540 |    5 |
|  5 | kan               | Kannada           |              2845 |       1.000 |    1.000 | 1.000 | 2845 |    0 | 57677 |    0 |
|  6 | kan_Latn          | Kannada (Latin)   |              2806 |       0.976 |    0.963 | 0.958 | 2701 |   67 | 57649 |  105 |
|  7 | mal_Latn          | Malayalam (Latin) |              2547 |       0.969 |    0.967 | 0.953 | 2463 |   80 | 57895 |   84 |
|  8 | eng               | English           |              2545 |       0.997 |    0.998 | 0.996 | 2539 |    8 | 57969 |    6 |
|  9 | mar_Latn          | Marathi (Latin)   |              2540 |       0.993 |    0.991 | 0.989 | 2516 |   17 | 57965 |   24 |
| 10 | guj               | Gujarati          |              2533 |       1.000 |    1.000 | 1.000 | 2533 |    0 | 57989 |    0 |
| 11 | guj_Latn          | Gujarati (Latin)  |              2510 |       0.947 |    0.967 | 0.932 | 2426 |  136 | 57876 |   84 |
| 12 | mar               | Marathi           |              2498 |       0.999 |    0.995 | 0.997 | 2486 |    2 | 58022 |   12 |
| 13 | mal               | Malayalam         |              2467 |       1.000 |    1.000 | 1.000 | 2467 |    0 | 58055 |    0 |
| 14 | tel               | Telugu            |              2376 |       1.000 |    1.000 | 1.000 | 2376 |    0 | 58146 |    0 |
| 15 | tel_Latn          | Telugu (Latin)    |              2296 |       0.941 |    0.963 | 0.924 | 2210 |  138 | 58088 |   86 |
| 16 | tam               | Tamil             |              2276 |       1.000 |    1.000 | 1.000 | 2276 |    0 | 58246 |    0 |
| 17 | tam_Latn          | Tamil (Latin)     |              2261 |       0.977 |    0.992 | 0.973 | 2242 |   52 | 58209 |   19 |
| 18 | ori               | Odia              |              2165 |       1.000 |    1.000 | 1.000 | 2165 |    0 | 58357 |    0 |
| 19 | ori_Latn          | Odia (Latin)      |              2137 |       0.983 |    0.972 | 0.969 | 2077 |   36 | 58349 |   60 |
| 20 | pan               | Punjabi           |              1508 |       1.000 |    1.000 | 1.000 | 1508 |    0 | 59014 |    0 |
| 21 | pan_Latn          | Punjabi (Latin)   |              1463 |       0.978 |    0.959 | 0.958 | 1403 |   31 | 59028 |   60 |
| 22 | asm               | Assamese          |              1412 |       1.000 |    0.994 | 0.997 | 1404 |    0 | 59110 |    8 |
| 23 | asm_Latn          | Assamese (Latin)  |              1375 |       0.995 |    0.990 | 0.990 | 1361 |    7 | 59140 |   14 |
| 24 | nep               | Nepali            |              1090 |       0.995 |    1.000 | 0.995 | 1090 |    5 | 59427 |    0 |
| 25 | nep_Latn          | Nepali (Latin)    |              1064 |       0.993 |    0.996 | 0.992 | 1060 |    7 | 59451 |    4 |
| 26 | urd               | Urdu              |               544 |       1.000 |    1.000 | 1.000 |  544 |    0 | 59978 |    0 |
| 27 | urd_Latn          | Urdu (Latin)      |               531 |       0.992 |    0.962 | 0.973 |  511 |    4 | 59987 |   20 |