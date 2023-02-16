# Classification performance for langid on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 36.68%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |     tp |     fp |      tn |     fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-------:|-------:|--------:|-------:|
|  1 | ben_Latn          | Bangla (Latin)    |            198442 |     nan     |    0.000 | 0.000 |      0 |      0 | 2472941 | 198442 |
|  2 | mal_Latn          | Malayalam (Latin) |            183874 |     nan     |    0.000 | 0.000 |      0 |      0 | 2487509 | 183874 |
|  3 | kan_Latn          | Kannada (Latin)   |            171671 |     nan     |    0.000 | 0.000 |      0 |      0 | 2499712 | 171671 |
|  4 | tam_Latn          | Tamil (Latin)     |            156564 |     nan     |    0.000 | 0.000 |      0 |      0 | 2514819 | 156564 |
|  5 | hin_Latn          | Hindi (Latin)     |            147189 |     nan     |    0.000 | 0.000 |      0 |      0 | 2524194 | 147189 |
|  6 | tel_Latn          | Telugu (Latin)    |            141218 |     nan     |    0.000 | 0.000 |      0 |      0 | 2530165 | 141218 |
|  7 | mal               | Malayalam         |            133162 |       1.000 |    1.000 | 1.000 | 133161 |     11 | 2538210 |      1 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |     nan     |    0.000 | 0.000 |      0 |      0 | 2542620 | 128763 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |     nan     |    0.000 | 0.000 |      0 |      0 | 2546548 | 124835 |
| 10 | kan               | Kannada           |            114958 |       1.000 |    1.000 | 1.000 | 114954 |     22 | 2556403 |      4 |
| 11 | ben               | Bangla            |            111340 |       0.900 |    0.952 | 0.880 | 106048 |  11831 | 2548212 |   5292 |
| 12 | tam               | Tamil             |            110537 |       1.000 |    1.000 | 1.000 | 110537 |     32 | 2560814 |      0 |
| 13 | tel               | Telugu            |             95609 |       1.000 |    1.000 | 1.000 |  95609 |      1 | 2575773 |      0 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |     nan     |    0.000 | 0.000 |      0 |      0 | 2579341 |  92042 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |     nan     |    0.000 | 0.000 |      0 |      0 | 2580020 |  91363 |
| 16 | hin               | Hindi             |             86513 |       0.726 |    0.773 | 0.656 |  66893 |  25275 | 2559595 |  19620 |
| 17 | mar               | Marathi           |             79305 |       0.707 |    0.828 | 0.659 |  65646 |  27151 | 2564927 |  13659 |
| 18 | guj               | Gujarati          |             74297 |       1.000 |    1.000 | 1.000 |  74289 |      7 | 2597079 |      8 |
| 19 | nep               | Nepali            |             69884 |       0.768 |    0.558 | 0.589 |  38997 |  11751 | 2589748 |  30887 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |     nan     |    0.000 | 0.000 |      0 |      0 | 2602304 |  69079 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |     nan     |    0.000 | 0.000 |      0 |      0 | 2613254 |  58129 |
| 22 | eng               | English           |             50759 |       0.141 |    0.990 | 0.140 |  50271 | 307479 | 2313145 |    488 |
| 23 | ori               | Odia              |             49645 |       1.000 |    1.000 | 1.000 |  49640 |      3 | 2621735 |      5 |
| 24 | pan               | Punjabi           |             39690 |       1.000 |    1.000 | 1.000 |  39685 |      1 | 2631692 |      5 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |     nan     |    0.000 | 0.000 |      0 |      0 | 2636528 |  34855 |
| 26 | asm               | Assamese          |             32307 |       0.795 |    0.634 | 0.647 |  20486 |   5286 | 2633790 |  11821 |
| 27 | urd               | Urdu              |             25353 |       1.000 |    0.539 | 0.701 |  13670 |      1 | 2646029 |  11683 |