# Classification performance for yubilangdetect-v2 on yubi-benchmark-dataset-v1

- Dataset coverage (sentences in supported languages): 60522 (100.00%)
- **Aggregated accuracy: 98.58%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben               | Bangla            |              4363 |       0.996 |    1.000 | 0.996 | 4363 |   17 | 56142 |    0 |
|  2 | ben_Latn          | Bangla (Latin)    |              4328 |       0.982 |    0.978 | 0.971 | 4231 |   78 | 56116 |   97 |
|  3 | hin_Latn          | Hindi (Latin)     |              3071 |       0.987 |    0.986 | 0.980 | 3027 |   39 | 57412 |   44 |
|  4 | hin               | Hindi             |              2971 |       0.996 |    0.998 | 0.995 | 2965 |   11 | 57540 |    6 |
|  5 | kan               | Kannada           |              2845 |       1.000 |    1.000 | 1.000 | 2845 |    0 | 57677 |    0 |
|  6 | kan_Latn          | Kannada (Latin)   |              2806 |       0.975 |    0.951 | 0.951 | 2669 |   68 | 57648 |  137 |
|  7 | mal_Latn          | Malayalam (Latin) |              2547 |       0.950 |    0.960 | 0.932 | 2445 |  128 | 57847 |  102 |
|  8 | eng               | English           |              2545 |       0.996 |    0.998 | 0.995 | 2541 |   10 | 57967 |    4 |
|  9 | mar_Latn          | Marathi (Latin)   |              2540 |       0.992 |    0.990 | 0.987 | 2515 |   20 | 57962 |   25 |
| 10 | guj               | Gujarati          |              2533 |       1.000 |    1.000 | 1.000 | 2533 |    0 | 57989 |    0 |
| 11 | guj_Latn          | Gujarati (Latin)  |              2510 |       0.947 |    0.963 | 0.930 | 2416 |  135 | 57877 |   94 |
| 12 | mar               | Marathi           |              2498 |       1.000 |    0.995 | 0.997 | 2485 |    1 | 58023 |   13 |
| 13 | mal               | Malayalam         |              2467 |       1.000 |    1.000 | 1.000 | 2467 |    0 | 58055 |    0 |
| 14 | tel               | Telugu            |              2376 |       1.000 |    1.000 | 1.000 | 2376 |    0 | 58146 |    0 |
| 15 | tel_Latn          | Telugu (Latin)    |              2296 |       0.936 |    0.948 | 0.913 | 2177 |  148 | 58078 |  119 |
| 16 | tam               | Tamil             |              2276 |       1.000 |    1.000 | 1.000 | 2276 |    0 | 58246 |    0 |
| 17 | tam_Latn          | Tamil (Latin)     |              2261 |       0.978 |    0.987 | 0.972 | 2232 |   50 | 58211 |   29 |
| 18 | ori               | Odia              |              2165 |       1.000 |    1.000 | 1.000 | 2165 |    0 | 58357 |    0 |
| 19 | ori_Latn          | Odia (Latin)      |              2137 |       0.976 |    0.968 | 0.960 | 2068 |   51 | 58334 |   69 |
| 20 | pan               | Punjabi           |              1508 |       1.000 |    1.000 | 1.000 | 1508 |    0 | 59014 |    0 |
| 21 | pan_Latn          | Punjabi (Latin)   |              1463 |       0.958 |    0.961 | 0.940 | 1406 |   61 | 58998 |   57 |
| 22 | asm               | Assamese          |              1412 |       1.000 |    0.988 | 0.994 | 1395 |    0 | 59110 |   17 |
| 23 | asm_Latn          | Assamese (Latin)  |              1375 |       0.985 |    0.992 | 0.981 | 1364 |   21 | 59126 |   11 |
| 24 | nep               | Nepali            |              1090 |       0.995 |    1.000 | 0.995 | 1090 |    6 | 59426 |    0 |
| 25 | nep_Latn          | Nepali (Latin)    |              1064 |       0.990 |    0.994 | 0.987 | 1058 |   11 | 59447 |    6 |
| 26 | urd               | Urdu              |               544 |       1.000 |    1.000 | 1.000 |  544 |    0 | 59978 |    0 |
| 27 | urd_Latn          | Urdu (Latin)      |               531 |       0.992 |    0.945 | 0.964 |  502 |    4 | 59987 |   29 |