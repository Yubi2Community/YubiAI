# Classification performance for pycld2 on yubi-benchmark-dataset-v1

- Dataset coverage (sentences in supported languages): 60522 (100.00%)
- **Aggregated accuracy: 51.26%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben               | Bangla            |              4363 |       0.996 |    0.933 | 0.961 | 4069 |   17 | 56142 |  294 |
|  2 | ben_Latn          | Bangla (Latin)    |              4328 |     nan     |    0.000 | 0.000 |    0 |    0 | 56194 | 4328 |
|  3 | hin_Latn          | Hindi (Latin)     |              3071 |     nan     |    0.000 | 0.000 |    0 |    0 | 57451 | 3071 |
|  4 | hin               | Hindi             |              2971 |       0.987 |    0.986 | 0.979 | 2928 |   40 | 57511 |   43 |
|  5 | kan               | Kannada           |              2845 |       1.000 |    1.000 | 1.000 | 2844 |    0 | 57677 |    1 |
|  6 | kan_Latn          | Kannada (Latin)   |              2806 |     nan     |    0.000 | 0.000 |    0 |    0 | 57716 | 2806 |
|  7 | mal_Latn          | Malayalam (Latin) |              2547 |     nan     |    0.000 | 0.000 |    0 |    0 | 57975 | 2547 |
|  8 | eng               | English           |              2545 |       0.722 |    0.985 | 0.719 | 2508 |  964 | 57013 |   37 |
|  9 | mar_Latn          | Marathi (Latin)   |              2540 |     nan     |    0.000 | 0.000 |    0 |    0 | 57982 | 2540 |
| 10 | guj               | Gujarati          |              2533 |       1.000 |    1.000 | 1.000 | 2533 |    0 | 57989 |    0 |
| 11 | guj_Latn          | Gujarati (Latin)  |              2510 |     nan     |    0.000 | 0.000 |    0 |    0 | 58012 | 2510 |
| 12 | mar               | Marathi           |              2498 |       0.998 |    0.981 | 0.989 | 2450 |    4 | 58020 |   48 |
| 13 | mal               | Malayalam         |              2467 |       1.000 |    1.000 | 1.000 | 2467 |    0 | 58055 |    0 |
| 14 | tel               | Telugu            |              2376 |       1.000 |    1.000 | 1.000 | 2375 |    0 | 58146 |    1 |
| 15 | tel_Latn          | Telugu (Latin)    |              2296 |     nan     |    0.000 | 0.000 |    0 |    0 | 58226 | 2296 |
| 16 | tam               | Tamil             |              2276 |       1.000 |    1.000 | 1.000 | 2276 |    0 | 58246 |    0 |
| 17 | tam_Latn          | Tamil (Latin)     |              2261 |     nan     |    0.000 | 0.000 |    0 |    0 | 58261 | 2261 |
| 18 | ori               | Odia              |              2165 |       1.000 |    0.997 | 0.999 | 2159 |    0 | 58357 |    6 |
| 19 | ori_Latn          | Odia (Latin)      |              2137 |     nan     |    0.000 | 0.000 |    0 |    0 | 58385 | 2137 |
| 20 | pan               | Punjabi           |              1508 |       1.000 |    0.997 | 0.998 | 1503 |    0 | 59014 |    5 |
| 21 | pan_Latn          | Punjabi (Latin)   |              1463 |     nan     |    0.000 | 0.000 |    0 |    0 | 59059 | 1463 |
| 22 | asm               | Assamese          |              1412 |       0.999 |    0.933 | 0.965 | 1318 |    1 | 59109 |   94 |
| 23 | asm_Latn          | Assamese (Latin)  |              1375 |     nan     |    0.000 | 0.000 |    0 |    0 | 59147 | 1375 |
| 24 | nep               | Nepali            |              1090 |       0.992 |    0.981 | 0.982 | 1069 |    9 | 59423 |   21 |
| 25 | nep_Latn          | Nepali (Latin)    |              1064 |     nan     |    0.000 | 0.000 |    0 |    0 | 59458 | 1064 |
| 26 | urd               | Urdu              |               544 |       1.000 |    0.965 | 0.982 |  525 |    0 | 59978 |   19 |
| 27 | urd_Latn          | Urdu (Latin)      |               531 |     nan     |    0.000 | 0.000 |    0 |    0 | 59991 |  531 |