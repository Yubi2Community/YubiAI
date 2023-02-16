# Classification performance for langid on yubi-benchmark-dataset-v2-full-gt2

- Dataset coverage (sentences in supported languages): 1771981 (100.00%)
- **Aggregated accuracy: 33.86%**

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
|  9 | ben               | Bangla            |             85534 |       0.901 |    0.960 | 0.885 | 82110 |   9009 | 1677438 |   3424 |
| 10 | ori_Latn          | Odia (Latin)      |             84961 |     nan     |    0.000 | 0.000 |     0 |      0 | 1687020 |  84961 |
| 11 | hin               | Hindi             |             60125 |       0.908 |    0.932 | 0.879 | 56025 |   5676 | 1706180 |   4100 |
| 12 | pan_Latn          | Punjabi (Latin)   |             58142 |     nan     |    0.000 | 0.000 |     0 |      0 | 1713839 |  58142 |
| 13 | kan               | Kannada           |             55734 |       1.000 |    1.000 | 1.000 | 55734 |     20 | 1716227 |      0 |
| 14 | asm_Latn          | Assamese (Latin)  |             53966 |     nan     |    0.000 | 0.000 |     0 |      0 | 1718015 |  53966 |
| 15 | eng               | English           |             50495 |       0.265 |    0.992 | 0.265 | 50089 | 139066 | 1582420 |    406 |
| 16 | guj               | Gujarati          |             50312 |       1.000 |    1.000 | 1.000 | 50307 |      3 | 1721666 |      5 |
| 17 | mal               | Malayalam         |             49607 |       1.000 |    1.000 | 1.000 | 49607 |     11 | 1722363 |      0 |
| 18 | mar               | Marathi           |             49449 |       0.918 |    0.939 | 0.891 | 46432 |   4158 | 1718374 |   3017 |
| 19 | tel               | Telugu            |             45958 |       1.000 |    1.000 | 1.000 | 45958 |      1 | 1726022 |      0 |
| 20 | tam               | Tamil             |             45230 |       0.999 |    1.000 | 0.999 | 45230 |     30 | 1726721 |      0 |
| 21 | nep_Latn          | Nepali (Latin)    |             43308 |     nan     |    0.000 | 0.000 |     0 |      0 | 1728673 |  43308 |
| 22 | ori               | Odia              |             42513 |       1.000 |    1.000 | 1.000 | 42513 |      3 | 1729465 |      0 |
| 23 | pan               | Punjabi           |             28861 |       1.000 |    1.000 | 1.000 | 28859 |      0 | 1743120 |      2 |
| 24 | asm               | Assamese          |             28278 |       0.849 |    0.682 | 0.709 | 19274 |   3425 | 1740278 |   9004 |
| 25 | nep               | Nepali            |             21493 |       0.920 |    0.804 | 0.827 | 17286 |   1504 | 1748984 |   4207 |
| 26 | urd_Latn          | Urdu (Latin)      |             20504 |     nan     |    0.000 | 0.000 |     0 |      0 | 1751477 |  20504 |
| 27 | urd               | Urdu              |             10770 |       1.000 |    0.985 | 0.993 | 10612 |      1 | 1761210 |    158 |