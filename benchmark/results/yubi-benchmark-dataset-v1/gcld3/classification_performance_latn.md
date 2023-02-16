# Classification performance for gcld3 on yubi-benchmark-dataset-v1

- Dataset coverage (sentences in supported languages): 60522 (100.00%)
- **Aggregated accuracy: 48.25%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |    fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|------:|------:|-----:|
|  1 | ben               | Bangla            |              4363 |       0.757 |    0.996 | 0.756 | 4345 |  1395 | 54764 |   18 |
|  2 | ben_Latn          | Bangla (Latin)    |              4328 |     nan     |    0.000 | 0.000 |    0 |     0 | 56194 | 4328 |
|  3 | hin_Latn          | Hindi (Latin)     |              3071 |       0.138 |    0.528 | 0.130 | 1621 | 10116 | 47335 | 1450 |
|  4 | hin               | Hindi             |              2971 |       0.727 |    0.971 | 0.719 | 2884 |  1083 | 56468 |   87 |
|  5 | kan               | Kannada           |              2845 |       1.000 |    0.989 | 0.995 | 2814 |     0 | 57677 |   31 |
|  6 | kan_Latn          | Kannada (Latin)   |              2806 |     nan     |    0.000 | 0.000 |    0 |     0 | 57716 | 2806 |
|  7 | mal_Latn          | Malayalam (Latin) |              2547 |     nan     |    0.000 | 0.000 |    0 |     0 | 57975 | 2547 |
|  8 | eng               | English           |              2545 |       0.937 |    0.958 | 0.918 | 2438 |   165 | 57812 |  107 |
|  9 | mar_Latn          | Marathi (Latin)   |              2540 |     nan     |    0.000 | 0.000 |    0 |     0 | 57982 | 2540 |
| 10 | guj               | Gujarati          |              2533 |       1.000 |    0.986 | 0.993 | 2498 |     0 | 57989 |   35 |
| 11 | guj_Latn          | Gujarati (Latin)  |              2510 |     nan     |    0.000 | 0.000 |    0 |     0 | 58012 | 2510 |
| 12 | mar               | Marathi           |              2498 |       0.905 |    0.974 | 0.894 | 2432 |   255 | 57769 |   66 |
| 13 | mal               | Malayalam         |              2467 |       1.000 |    0.995 | 0.997 | 2454 |     0 | 58055 |   13 |
| 14 | tel               | Telugu            |              2376 |       1.000 |    0.995 | 0.997 | 2364 |     0 | 58146 |   12 |
| 15 | tel_Latn          | Telugu (Latin)    |              2296 |     nan     |    0.000 | 0.000 |    0 |     0 | 58226 | 2296 |
| 16 | tam               | Tamil             |              2276 |       1.000 |    0.990 | 0.995 | 2254 |     0 | 58246 |   22 |
| 17 | tam_Latn          | Tamil (Latin)     |              2261 |     nan     |    0.000 | 0.000 |    0 |     0 | 58261 | 2261 |
| 18 | ori               | Odia              |              2165 |     nan     |    0.000 | 0.000 |    0 |     0 | 58357 | 2165 |
| 19 | ori_Latn          | Odia (Latin)      |              2137 |     nan     |    0.000 | 0.000 |    0 |     0 | 58385 | 2137 |
| 20 | pan               | Punjabi           |              1508 |       1.000 |    0.996 | 0.998 | 1502 |     0 | 59014 |    6 |
| 21 | pan_Latn          | Punjabi (Latin)   |              1463 |     nan     |    0.000 | 0.000 |    0 |     0 | 59059 | 1463 |
| 22 | asm               | Assamese          |              1412 |     nan     |    0.000 | 0.000 |    0 |     0 | 59110 | 1412 |
| 23 | asm_Latn          | Assamese (Latin)  |              1375 |     nan     |    0.000 | 0.000 |    0 |     0 | 59147 | 1375 |
| 24 | nep               | Nepali            |              1090 |       0.498 |    0.972 | 0.494 | 1060 |  1069 | 58363 |   30 |
| 25 | nep_Latn          | Nepali (Latin)    |              1064 |     nan     |    0.000 | 0.000 |    0 |     0 | 59458 | 1064 |
| 26 | urd               | Urdu              |               544 |       0.989 |    0.987 | 0.983 |  537 |     6 | 59972 |    7 |
| 27 | urd_Latn          | Urdu (Latin)      |               531 |     nan     |    0.000 | 0.000 |    0 |     0 | 59991 |  531 |