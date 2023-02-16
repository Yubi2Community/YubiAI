# Classification performance for yubilangdetect-v1 on yubi-benchmark-dataset-v2-full-gt2

- Dataset coverage (sentences in supported languages): 1771981 (100.00%)
- **Aggregated accuracy: 85.41%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |     tp |    fp |      tn |    fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-------:|------:|--------:|------:|
|  1 | ben_Latn          | Bangla (Latin)    |            172295 |       0.926 |    0.772 | 0.814 | 133053 | 10701 | 1588985 | 39242 |
|  2 | hin_Latn          | Hindi (Latin)     |            120543 |       0.880 |    0.659 | 0.717 |  79472 | 10869 | 1640569 | 41071 |
|  3 | kan_Latn          | Kannada (Latin)   |            111911 |       0.884 |    0.871 | 0.830 |  97437 | 12776 | 1647294 | 14474 |
|  4 | guj_Latn          | Gujarati (Latin)  |            100559 |       0.647 |    0.688 | 0.565 |  69203 | 37686 | 1633736 | 31356 |
|  5 | mal_Latn          | Malayalam (Latin) |             99892 |       0.860 |    0.738 | 0.746 |  73685 | 12018 | 1660071 | 26207 |
|  6 | mar_Latn          | Marathi (Latin)   |             98926 |       0.900 |    0.950 | 0.879 |  94020 | 10469 | 1662586 |  4906 |
|  7 | tel_Latn          | Telugu (Latin)    |             91750 |       0.894 |    0.766 | 0.787 |  70290 |  8338 | 1671893 | 21460 |
|  8 | tam_Latn          | Tamil (Latin)     |             90865 |       0.857 |    0.751 | 0.751 |  68276 | 11358 | 1669758 | 22589 |
|  9 | ben               | Bangla            |             85534 |       0.999 |    1.000 | 0.999 |  85525 |   117 | 1686330 |     9 |
| 10 | ori_Latn          | Odia (Latin)      |             84961 |       0.634 |    0.831 | 0.595 |  70564 | 40818 | 1646202 | 14397 |
| 11 | hin               | Hindi             |             60125 |       0.999 |    0.999 | 0.998 |  60084 |    71 | 1711785 |    41 |
| 12 | pan_Latn          | Punjabi (Latin)   |             58142 |       0.790 |    0.620 | 0.636 |  36036 |  9608 | 1704231 | 22106 |
| 13 | kan               | Kannada           |             55734 |       1.000 |    1.000 | 1.000 |  55734 |    23 | 1716224 |     0 |
| 14 | asm_Latn          | Assamese (Latin)  |             53966 |       0.918 |    0.762 | 0.803 |  41111 |  3653 | 1714362 | 12855 |
| 15 | eng               | English           |             50495 |       0.655 |    0.999 | 0.655 |  50436 | 26555 | 1694931 |    59 |
| 16 | guj               | Gujarati          |             50312 |       1.000 |    1.000 | 1.000 |  50311 |     5 | 1721664 |     1 |
| 17 | mal               | Malayalam         |             49607 |       1.000 |    1.000 | 1.000 |  49607 |     1 | 1722373 |     0 |
| 18 | mar               | Marathi           |             49449 |       0.999 |    0.999 | 0.998 |  49399 |    56 | 1722476 |    50 |
| 19 | tel               | Telugu            |             45958 |       1.000 |    1.000 | 1.000 |  45957 |     3 | 1726020 |     1 |
| 20 | tam               | Tamil             |             45230 |       1.000 |    1.000 | 1.000 |  45230 |     4 | 1726747 |     0 |
| 21 | nep_Latn          | Nepali (Latin)    |             43308 |       0.488 |    0.968 | 0.484 |  41929 | 43928 | 1684745 |  1379 |
| 22 | ori               | Odia              |             42513 |       1.000 |    1.000 | 1.000 |  42513 |     3 | 1729465 |     0 |
| 23 | pan               | Punjabi           |             28861 |       1.000 |    1.000 | 1.000 |  28861 |     2 | 1743118 |     0 |
| 24 | asm               | Assamese          |             28278 |       0.999 |    0.996 | 0.997 |  28177 |    22 | 1743681 |   101 |
| 25 | nep               | Nepali            |             21493 |       1.000 |    0.999 | 0.999 |  21467 |     6 | 1750482 |    26 |
| 26 | urd_Latn          | Urdu (Latin)      |             20504 |       0.422 |    0.694 | 0.386 |  14239 | 19502 | 1731975 |  6265 |
| 27 | urd               | Urdu              |             10770 |       1.000 |    1.000 | 1.000 |  10770 |     3 | 1761208 |     0 |