# Classification performance for langdetect on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 35.39%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |     tp |    fp |      tn |     fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-------:|------:|--------:|-------:|
|  1 | ben_Latn          | Bangla (Latin)    |            198442 |     nan     |    0.000 | 0.000 |      0 |     0 | 2472941 | 198442 |
|  2 | mal_Latn          | Malayalam (Latin) |            183874 |     nan     |    0.000 | 0.000 |      0 |     0 | 2487509 | 183874 |
|  3 | kan_Latn          | Kannada (Latin)   |            171671 |     nan     |    0.000 | 0.000 |      0 |     0 | 2499712 | 171671 |
|  4 | tam_Latn          | Tamil (Latin)     |            156564 |     nan     |    0.000 | 0.000 |      0 |     0 | 2514819 | 156564 |
|  5 | hin_Latn          | Hindi (Latin)     |            147189 |     nan     |    0.000 | 0.000 |      0 |     0 | 2524194 | 147189 |
|  6 | tel_Latn          | Telugu (Latin)    |            141218 |     nan     |    0.000 | 0.000 |      0 |     0 | 2530165 | 141218 |
|  7 | mal               | Malayalam         |            133162 |       1.000 |    1.000 | 1.000 | 133160 |     0 | 2538221 |      2 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |     nan     |    0.000 | 0.000 |      0 |     0 | 2542620 | 128763 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |     nan     |    0.000 | 0.000 |      0 |     0 | 2546548 | 124835 |
| 10 | kan               | Kannada           |            114958 |       1.000 |    1.000 | 1.000 | 114954 |     0 | 2556425 |      4 |
| 11 | ben               | Bangla            |            111340 |       0.775 |    1.000 | 0.775 | 111339 | 32332 | 2527711 |      1 |
| 12 | tam               | Tamil             |            110537 |       1.000 |    1.000 | 1.000 | 110535 |     0 | 2560846 |      2 |
| 13 | tel               | Telugu            |             95609 |       1.000 |    1.000 | 1.000 |  95608 |     0 | 2575774 |      1 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |     nan     |    0.000 | 0.000 |      0 |     0 | 2579341 |  92042 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |     nan     |    0.000 | 0.000 |      0 |     0 | 2580020 |  91363 |
| 16 | hin               | Hindi             |             86513 |       0.860 |    0.809 | 0.780 |  69975 | 11424 | 2573446 |  16538 |
| 17 | mar               | Marathi           |             79305 |       0.797 |    0.904 | 0.765 |  71663 | 18246 | 2573832 |   7642 |
| 18 | guj               | Gujarati          |             74297 |       1.000 |    1.000 | 1.000 |  74285 |     0 | 2597086 |     12 |
| 19 | nep               | Nepali            |             69884 |       0.716 |    0.775 | 0.648 |  54129 | 21468 | 2580031 |  15755 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |     nan     |    0.000 | 0.000 |      0 |     0 | 2602304 |  69079 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |     nan     |    0.000 | 0.000 |      0 |     0 | 2613254 |  58129 |
| 22 | eng               | English           |             50759 |       0.340 |    0.983 | 0.339 |  49904 | 96796 | 2523828 |    855 |
| 23 | ori               | Odia              |             49645 |     nan     |    0.000 | 0.000 |      0 |     0 | 2621738 |  49645 |
| 24 | pan               | Punjabi           |             39690 |       0.638 |    1.000 | 0.638 |  39690 | 22483 | 2609210 |      0 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |     nan     |    0.000 | 0.000 |      0 |     0 | 2636528 |  34855 |
| 26 | asm               | Assamese          |             32307 |     nan     |    0.000 | 0.000 |      0 |     0 | 2639076 |  32307 |
| 27 | urd               | Urdu              |             25353 |       1.000 |    0.799 | 0.888 |  20265 |     0 | 2646030 |   5088 |