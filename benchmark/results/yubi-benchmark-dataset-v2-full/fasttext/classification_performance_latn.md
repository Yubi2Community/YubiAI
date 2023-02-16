# Classification performance for fasttext on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 37.81%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |     tp |      fp |      tn |     fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-------:|--------:|--------:|-------:|
|  1 | ben_Latn          | Bangla (Latin)    |            198442 |     nan     |    0.000 | 0.000 |      0 |       0 | 2472941 | 198442 |
|  2 | mal_Latn          | Malayalam (Latin) |            183874 |     nan     |    0.000 | 0.000 |      0 |       0 | 2487509 | 183874 |
|  3 | kan_Latn          | Kannada (Latin)   |            171671 |     nan     |    0.000 | 0.000 |      0 |       0 | 2499712 | 171671 |
|  4 | tam_Latn          | Tamil (Latin)     |            156564 |     nan     |    0.000 | 0.000 |      0 |       0 | 2514819 | 156564 |
|  5 | hin_Latn          | Hindi (Latin)     |            147189 |     nan     |    0.000 | 0.000 |      0 |       0 | 2524194 | 147189 |
|  6 | tel_Latn          | Telugu (Latin)    |            141218 |     nan     |    0.000 | 0.000 |      0 |       0 | 2530165 | 141218 |
|  7 | mal               | Malayalam         |            133162 |       0.987 |    0.999 | 0.987 | 133062 |    1729 | 2536492 |    100 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |     nan     |    0.000 | 0.000 |      0 |       0 | 2542620 | 128763 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |     nan     |    0.000 | 0.000 |      0 |       0 | 2546548 | 124835 |
| 10 | kan               | Kannada           |            114958 |       0.984 |    0.998 | 0.983 | 114726 |    1825 | 2554600 |    232 |
| 11 | ben               | Bangla            |            111340 |       0.964 |    0.985 | 0.957 | 109644 |    4111 | 2555932 |   1696 |
| 12 | tam               | Tamil             |            110537 |       0.998 |    1.000 | 0.998 | 110519 |     237 | 2560609 |     18 |
| 13 | tel               | Telugu            |             95609 |       0.998 |    1.000 | 0.997 |  95569 |     231 | 2575543 |     40 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |     nan     |    0.000 | 0.000 |      0 |       0 | 2579341 |  92042 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |     nan     |    0.000 | 0.000 |      0 |       0 | 2580020 |  91363 |
| 16 | hin               | Hindi             |             86513 |       0.773 |    0.897 | 0.740 |  77563 |   22785 | 2562085 |   8950 |
| 17 | mar               | Marathi           |             79305 |       0.871 |    0.857 | 0.812 |  67961 |   10048 | 2582030 |  11344 |
| 18 | guj               | Gujarati          |             74297 |       0.999 |    0.998 | 0.998 |  74122 |      89 | 2596997 |    175 |
| 19 | nep               | Nepali            |             69884 |       0.947 |    0.610 | 0.727 |  42659 |    2382 | 2599117 |  27225 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |     nan     |    0.000 | 0.000 |      0 |       0 | 2602304 |  69079 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |     nan     |    0.000 | 0.000 |      0 |       0 | 2613254 |  58129 |
| 22 | eng               | English           |             50759 |       0.045 |    0.997 | 0.045 |  50605 | 1067553 | 1553071 |    154 |
| 23 | ori               | Odia              |             49645 |       1.000 |    0.996 | 0.998 |  49452 |       9 | 2621729 |    193 |
| 24 | pan               | Punjabi           |             39690 |       0.998 |    0.997 | 0.997 |  39572 |      62 | 2631631 |    118 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |     nan     |    0.000 | 0.000 |      0 |       0 | 2636528 |  34855 |
| 26 | asm               | Assamese          |             32307 |       0.980 |    0.901 | 0.930 |  29097 |     581 | 2638495 |   3210 |
| 27 | urd               | Urdu              |             25353 |       0.894 |    0.613 | 0.697 |  15540 |    1844 | 2644186 |   9813 |