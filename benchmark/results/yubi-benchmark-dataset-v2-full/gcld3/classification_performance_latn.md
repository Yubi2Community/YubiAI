# Classification performance for gcld3 on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 36.23%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |     tp |     fp |      tn |     fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-------:|-------:|--------:|-------:|
|  1 | ben_Latn          | Bangla (Latin)    |            198442 |     nan     |    0.000 | 0.000 |      0 |      0 | 2472941 | 198442 |
|  2 | mal_Latn          | Malayalam (Latin) |            183874 |     nan     |    0.000 | 0.000 |      0 |      0 | 2487509 | 183874 |
|  3 | kan_Latn          | Kannada (Latin)   |            171671 |     nan     |    0.000 | 0.000 |      0 |      0 | 2499712 | 171671 |
|  4 | tam_Latn          | Tamil (Latin)     |            156564 |     nan     |    0.000 | 0.000 |      0 |      0 | 2514819 | 156564 |
|  5 | hin_Latn          | Hindi (Latin)     |            147189 |       0.120 |    0.292 | 0.105 |  43014 | 314966 | 2209228 | 104175 |
|  6 | tel_Latn          | Telugu (Latin)    |            141218 |     nan     |    0.000 | 0.000 |      0 |      0 | 2530165 | 141218 |
|  7 | mal               | Malayalam         |            133162 |       1.000 |    0.991 | 0.995 | 131909 |      0 | 2538221 |   1253 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |     nan     |    0.000 | 0.000 |      0 |      0 | 2542620 | 128763 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |     nan     |    0.000 | 0.000 |      0 |      0 | 2546548 | 124835 |
| 10 | kan               | Kannada           |            114958 |       1.000 |    0.994 | 0.997 | 114213 |      9 | 2556416 |    745 |
| 11 | ben               | Bangla            |            111340 |       0.777 |    0.994 | 0.775 | 110707 |  31840 | 2528203 |    633 |
| 12 | tam               | Tamil             |            110537 |       1.000 |    0.995 | 0.997 | 109938 |      1 | 2560845 |    599 |
| 13 | tel               | Telugu            |             95609 |       1.000 |    0.995 | 0.997 |  95119 |      0 | 2575774 |    490 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |     nan     |    0.000 | 0.000 |      0 |      0 | 2579341 |  92042 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |     nan     |    0.000 | 0.000 |      0 |      0 | 2580020 |  91363 |
| 16 | hin               | Hindi             |             86513 |       0.672 |    0.753 | 0.605 |  65112 |  31839 | 2553031 |  21401 |
| 17 | mar               | Marathi           |             79305 |       0.714 |    0.869 | 0.677 |  68883 |  27622 | 2564456 |  10422 |
| 18 | guj               | Gujarati          |             74297 |       0.999 |    0.989 | 0.994 |  73489 |     39 | 2597047 |    808 |
| 19 | nep               | Nepali            |             69884 |       0.594 |    0.744 | 0.539 |  51998 |  35485 | 2566014 |  17886 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |     nan     |    0.000 | 0.000 |      0 |      0 | 2602304 |  69079 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |     nan     |    0.000 | 0.000 |      0 |      0 | 2613254 |  58129 |
| 22 | eng               | English           |             50759 |       0.816 |    0.958 | 0.801 |  48614 |  10980 | 2609644 |   2145 |
| 23 | ori               | Odia              |             49645 |     nan     |    0.000 | 0.000 |      0 |      0 | 2621738 |  49645 |
| 24 | pan               | Punjabi           |             39690 |       1.000 |    0.993 | 0.996 |  39398 |      0 | 2631693 |    292 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |     nan     |    0.000 | 0.000 |      0 |      0 | 2636528 |  34855 |
| 26 | asm               | Assamese          |             32307 |     nan     |    0.000 | 0.000 |      0 |      0 | 2639076 |  32307 |
| 27 | urd               | Urdu              |             25353 |       0.970 |    0.614 | 0.744 |  15569 |    476 | 2645554 |   9784 |