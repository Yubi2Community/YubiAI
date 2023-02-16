# Classification performance for fasttext on yubi-benchmark-dataset-v2-full-gt2

- Dataset coverage (sentences in supported languages): 1771981 (100.00%)
- **Aggregated accuracy: 35.07%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |    tp |     fp |      tn |     fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|------:|-------:|--------:|-------:|
|  1 | ben_Latn          | Bangla (Latin)    |            172295 |     nan     |    0.000 | 0.000 |     0 |      0 | 1599686 | 172295 |
|  2 | hin_Latn          | Hindi (Latin)     |            120543 |     nan     |    0.000 | 0.000 |     0 |      0 | 1651438 | 120543 |
|  3 | kan_Latn          | Kannada (Latin)   |            111911 |     nan     |    0.000 | 0.000 |     0 |      0 | 1660070 | 111911 |
|  4 | guj_Latn          | Gujarati (Latin)  |            100559 |     nan     |    0.000 | 0.000 |     0 |      0 | 1671422 | 100559 |
|  5 | mal_Latn          | Malayalam (Latin) |             99892 |     nan     |    0.000 | 0.000 |     0 |      0 | 1672089 |  99892 |
|  6 | mar_Latn          | Marathi (Latin)   |             98926 |     nan     |    0.000 | 0.000 |     0 |      0 | 1673055 |  98926 |
|  7 | tel_Latn          | Telugu (Latin)    |             91750 |     nan     |    0.000 | 0.000 |     0 |      0 | 1680231 |  91750 |
|  8 | tam_Latn          | Tamil (Latin)     |             90865 |     nan     |    0.000 | 0.000 |     0 |      0 | 1681116 |  90865 |
|  9 | ben               | Bangla            |             85534 |       0.976 |    1.000 | 0.976 | 85514 |   2117 | 1684330 |     20 |
| 10 | ori_Latn          | Odia (Latin)      |             84961 |     nan     |    0.000 | 0.000 |     0 |      0 | 1687020 |  84961 |
| 11 | hin               | Hindi             |             60125 |       0.987 |    0.997 | 0.986 | 59973 |    802 | 1711054 |    152 |
| 12 | pan_Latn          | Punjabi (Latin)   |             58142 |     nan     |    0.000 | 0.000 |     0 |      0 | 1713839 |  58142 |
| 13 | kan               | Kannada           |             55734 |       0.979 |    1.000 | 0.979 | 55733 |   1221 | 1715026 |      1 |
| 14 | asm_Latn          | Assamese (Latin)  |             53966 |     nan     |    0.000 | 0.000 |     0 |      0 | 1718015 |  53966 |
| 15 | eng               | English           |             50495 |       0.056 |    0.998 | 0.056 | 50411 | 853307 |  868179 |     84 |
| 16 | guj               | Gujarati          |             50312 |       1.000 |    1.000 | 1.000 | 50306 |     11 | 1721658 |      6 |
| 17 | mal               | Malayalam         |             49607 |       0.980 |    1.000 | 0.980 | 49602 |    989 | 1721385 |      5 |
| 18 | mar               | Marathi           |             49449 |       0.996 |    0.994 | 0.993 | 49148 |    200 | 1722332 |    301 |
| 19 | tel               | Telugu            |             45958 |       0.999 |    1.000 | 0.999 | 45958 |     61 | 1725962 |      0 |
| 20 | tam               | Tamil             |             45230 |       0.998 |    1.000 | 0.998 | 45230 |     82 | 1726669 |      0 |
| 21 | nep_Latn          | Nepali (Latin)    |             43308 |     nan     |    0.000 | 0.000 |     0 |      0 | 1728673 |  43308 |
| 22 | ori               | Odia              |             42513 |       1.000 |    1.000 | 1.000 | 42512 |      0 | 1729468 |      1 |
| 23 | pan               | Punjabi           |             28861 |       1.000 |    1.000 | 1.000 | 28853 |      1 | 1743119 |      8 |
| 24 | asm               | Assamese          |             28278 |       1.000 |    0.949 | 0.974 | 26849 |     10 | 1743693 |   1429 |
| 25 | nep               | Nepali            |             21493 |       0.998 |    0.963 | 0.979 | 20698 |     46 | 1750442 |    795 |
| 26 | urd_Latn          | Urdu (Latin)      |             20504 |     nan     |    0.000 | 0.000 |     0 |      0 | 1751477 |  20504 |
| 27 | urd               | Urdu              |             10770 |       0.918 |    0.990 | 0.914 | 10659 |    948 | 1760263 |    111 |