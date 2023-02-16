# Classification performance for yubilangdetect-v1 on yubi-benchmark-dataset-v2

- Dataset coverage (sentences in supported languages): 80144 (100.00%)
- **Aggregated accuracy: 76.14%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben_Latn          | Bangla (Latin)    |              5954 |       0.874 |    0.681 | 0.726 | 4056 |  583 | 73607 | 1898 |
|  2 | mal_Latn          | Malayalam (Latin) |              5374 |       0.744 |    0.497 | 0.541 | 2673 |  918 | 73852 | 2701 |
|  3 | kan_Latn          | Kannada (Latin)   |              5068 |       0.665 |    0.775 | 0.607 | 3930 | 1978 | 73098 | 1138 |
|  4 | tam_Latn          | Tamil (Latin)     |              4706 |       0.673 |    0.586 | 0.544 | 2760 | 1342 | 74096 | 1946 |
|  5 | hin_Latn          | Hindi (Latin)     |              4354 |       0.764 |    0.545 | 0.579 | 2373 |  732 | 75058 | 1981 |
|  6 | tel_Latn          | Telugu (Latin)    |              4288 |       0.707 |    0.594 | 0.569 | 2549 | 1058 | 74798 | 1739 |
|  7 | mal               | Malayalam         |              3992 |       0.999 |    0.999 | 0.999 | 3990 |    2 | 76150 |    2 |
|  8 | mar_Latn          | Marathi (Latin)   |              3915 |       0.645 |    0.800 | 0.597 | 3133 | 1726 | 74503 |  782 |
|  9 | guj_Latn          | Gujarati (Latin)  |              3749 |       0.606 |    0.567 | 0.492 | 2127 | 1382 | 75013 | 1622 |
| 10 | kan               | Kannada           |              3431 |       0.997 |    1.000 | 0.997 | 3431 |   10 | 76703 |    0 |
| 11 | ben               | Bangla            |              3387 |       0.992 |    0.943 | 0.963 | 3193 |   27 | 76730 |  194 |
| 12 | tam               | Tamil             |              3344 |       1.000 |    1.000 | 1.000 | 3344 |    1 | 76799 |    0 |
| 13 | tel               | Telugu            |              2881 |       0.996 |    1.000 | 0.996 | 2881 |   11 | 77252 |    0 |
| 14 | ori_Latn          | Odia (Latin)      |              2798 |       0.583 |    0.782 | 0.540 | 2188 | 1562 | 75784 |  610 |
| 15 | nep_Latn          | Nepali (Latin)    |              2765 |       0.501 |    0.511 | 0.404 | 1414 | 1411 | 75968 | 1351 |
| 16 | hin               | Hindi             |              2583 |       0.819 |    0.886 | 0.778 | 2289 |  506 | 77055 |  294 |
| 17 | mar               | Marathi           |              2411 |       0.794 |    0.943 | 0.775 | 2273 |  591 | 77142 |  138 |
| 18 | guj               | Gujarati          |              2283 |       1.000 |    1.000 | 1.000 | 2283 |    0 | 77861 |    0 |
| 19 | nep               | Nepali            |              2089 |       0.982 |    0.666 | 0.788 | 1392 |   25 | 78030 |  697 |
| 20 | pan_Latn          | Punjabi (Latin)   |              2085 |       0.746 |    0.541 | 0.567 | 1129 |  384 | 77675 |  956 |
| 21 | asm_Latn          | Assamese (Latin)  |              1731 |       0.305 |    0.741 | 0.289 | 1283 | 2925 | 75488 |  448 |
| 22 | eng               | English           |              1564 |       0.583 |    0.998 | 0.583 | 1561 | 1116 | 77464 |    3 |
| 23 | ori               | Odia              |              1450 |       0.998 |    0.999 | 0.998 | 1449 |    3 | 78691 |    1 |
| 24 | pan               | Punjabi           |              1213 |       0.995 |    0.998 | 0.994 | 1211 |    6 | 78925 |    2 |
| 25 | urd_Latn          | Urdu (Latin)      |               993 |       0.385 |    0.398 | 0.298 |  395 |  631 | 78520 |  598 |
| 26 | asm               | Assamese          |               925 |       0.823 |    0.975 | 0.814 |  902 |  194 | 79025 |   23 |
| 27 | urd               | Urdu              |               811 |       1.000 |    1.000 | 1.000 |  811 |    0 | 79333 |    0 |