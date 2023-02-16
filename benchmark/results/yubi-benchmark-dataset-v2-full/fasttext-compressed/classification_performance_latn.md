# Classification performance for fasttext-compressed on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 37.35%**

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
|  7 | mal               | Malayalam         |            133162 |       0.996 |    0.998 | 0.995 | 132914 |    541 | 2537680 |    248 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |     nan     |    0.000 | 0.000 |      0 |      0 | 2542620 | 128763 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |     nan     |    0.000 | 0.000 |      0 |      0 | 2546548 | 124835 |
| 10 | kan               | Kannada           |            114958 |       0.998 |    0.998 | 0.996 | 114676 |    269 | 2556156 |    282 |
| 11 | ben               | Bangla            |            111340 |       0.959 |    0.982 | 0.951 | 109355 |   4640 | 2555403 |   1985 |
| 12 | tam               | Tamil             |            110537 |       0.999 |    0.999 | 0.999 | 110480 |    107 | 2560739 |     57 |
| 13 | tel               | Telugu            |             95609 |       0.999 |    0.999 | 0.998 |  95480 |    104 | 2575670 |    129 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |     nan     |    0.000 | 0.000 |      0 |      0 | 2579341 |  92042 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |     nan     |    0.000 | 0.000 |      0 |      0 | 2580020 |  91363 |
| 16 | hin               | Hindi             |             86513 |       0.707 |    0.893 | 0.679 |  77278 |  31959 | 2552911 |   9235 |
| 17 | mar               | Marathi           |             79305 |       0.819 |    0.845 | 0.762 |  67048 |  14835 | 2577243 |  12257 |
| 18 | guj               | Gujarati          |             74297 |       1.000 |    0.994 | 0.997 |  73832 |     17 | 2597069 |    465 |
| 19 | nep               | Nepali            |             69884 |       0.963 |    0.507 | 0.656 |  35440 |   1365 | 2600134 |  34444 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |     nan     |    0.000 | 0.000 |      0 |      0 | 2602304 |  69079 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |     nan     |    0.000 | 0.000 |      0 |      0 | 2613254 |  58129 |
| 22 | eng               | English           |             50759 |       0.053 |    0.996 | 0.053 |  50573 | 896373 | 1724251 |    186 |
| 23 | ori               | Odia              |             49645 |       1.000 |    0.989 | 0.994 |  49077 |     10 | 2621728 |    568 |
| 24 | pan               | Punjabi           |             39690 |       0.999 |    0.992 | 0.995 |  39375 |     43 | 2631650 |    315 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |     nan     |    0.000 | 0.000 |      0 |      0 | 2636528 |  34855 |
| 26 | asm               | Assamese          |             32307 |       0.991 |    0.854 | 0.914 |  27601 |    250 | 2638826 |   4706 |
| 27 | urd               | Urdu              |             25353 |       0.945 |    0.573 | 0.699 |  14538 |    854 | 2645176 |  10815 |