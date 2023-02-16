# Classification performance for pycld2 on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 36.21%**

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
|  7 | mal               | Malayalam         |            133162 |       1.000 |    1.000 | 1.000 | 133156 |     7 | 2538214 |      6 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |     nan     |    0.000 | 0.000 |      0 |     0 | 2542620 | 128763 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |     nan     |    0.000 | 0.000 |      0 |     0 | 2546548 | 124835 |
| 10 | kan               | Kannada           |            114958 |       1.000 |    1.000 | 1.000 | 114945 |    50 | 2556375 |     13 |
| 11 | ben               | Bangla            |            111340 |       0.995 |    0.756 | 0.858 |  84191 |   405 | 2559638 |  27149 |
| 12 | tam               | Tamil             |            110537 |       1.000 |    1.000 | 1.000 | 110533 |     5 | 2560841 |      4 |
| 13 | tel               | Telugu            |             95609 |       1.000 |    1.000 | 1.000 |  95602 |     7 | 2575767 |      7 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |     nan     |    0.000 | 0.000 |      0 |     0 | 2579341 |  92042 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |     nan     |    0.000 | 0.000 |      0 |     0 | 2580020 |  91363 |
| 16 | hin               | Hindi             |             86513 |       0.912 |    0.764 | 0.799 |  66064 |  6348 | 2578522 |  20449 |
| 17 | mar               | Marathi           |             79305 |       0.929 |    0.824 | 0.845 |  65313 |  4968 | 2587110 |  13992 |
| 18 | guj               | Gujarati          |             74297 |       0.999 |    1.000 | 0.998 |  74281 |   105 | 2596981 |     16 |
| 19 | nep               | Nepali            |             69884 |       0.935 |    0.656 | 0.751 |  45850 |  3162 | 2598337 |  24034 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |     nan     |    0.000 | 0.000 |      0 |     0 | 2602304 |  69079 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |     nan     |    0.000 | 0.000 |      0 |     0 | 2613254 |  58129 |
| 22 | eng               | English           |             50759 |       0.543 |    0.988 | 0.541 |  50173 | 42248 | 2578376 |    586 |
| 23 | ori               | Odia              |             49645 |       0.999 |    0.998 | 0.998 |  49537 |    32 | 2621706 |    108 |
| 24 | pan               | Punjabi           |             39690 |       1.000 |    0.998 | 0.999 |  39616 |     1 | 2631692 |     74 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |     nan     |    0.000 | 0.000 |      0 |     0 | 2636528 |  34855 |
| 26 | asm               | Assamese          |             32307 |       0.996 |    0.830 | 0.904 |  26806 |   110 | 2638966 |   5501 |
| 27 | urd               | Urdu              |             25353 |       0.996 |    0.443 | 0.612 |  11232 |    46 | 2645984 |  14121 |