# Classification performance for pycld2 on yubi-benchmark-dataset-v2-full-gt2

- Dataset coverage (sentences in supported languages): 1771981 (100.00%)
- **Aggregated accuracy: 34.69%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |    tp |    fp |      tn |     fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|------:|------:|--------:|-------:|
|  1 | ben_Latn          | Bangla (Latin)    |            172295 |     nan     |    0.000 | 0.000 |     0 |     0 | 1599686 | 172295 |
|  2 | hin_Latn          | Hindi (Latin)     |            120543 |     nan     |    0.000 | 0.000 |     0 |     0 | 1651438 | 120543 |
|  3 | kan_Latn          | Kannada (Latin)   |            111911 |     nan     |    0.000 | 0.000 |     0 |     0 | 1660070 | 111911 |
|  4 | guj_Latn          | Gujarati (Latin)  |            100559 |     nan     |    0.000 | 0.000 |     0 |     0 | 1671422 | 100559 |
|  5 | mal_Latn          | Malayalam (Latin) |             99892 |     nan     |    0.000 | 0.000 |     0 |     0 | 1672089 |  99892 |
|  6 | mar_Latn          | Marathi (Latin)   |             98926 |     nan     |    0.000 | 0.000 |     0 |     0 | 1673055 |  98926 |
|  7 | tel_Latn          | Telugu (Latin)    |             91750 |     nan     |    0.000 | 0.000 |     0 |     0 | 1680231 |  91750 |
|  8 | tam_Latn          | Tamil (Latin)     |             90865 |     nan     |    0.000 | 0.000 |     0 |     0 | 1681116 |  90865 |
|  9 | ben               | Bangla            |             85534 |       0.996 |    0.939 | 0.965 | 80341 |   307 | 1686140 |   5193 |
| 10 | ori_Latn          | Odia (Latin)      |             84961 |     nan     |    0.000 | 0.000 |     0 |     0 | 1687020 |  84961 |
| 11 | hin               | Hindi             |             60125 |       0.991 |    0.987 | 0.984 | 59323 |   564 | 1711292 |    802 |
| 12 | pan_Latn          | Punjabi (Latin)   |             58142 |     nan     |    0.000 | 0.000 |     0 |     0 | 1713839 |  58142 |
| 13 | kan               | Kannada           |             55734 |       0.999 |    1.000 | 0.999 | 55721 |    50 | 1716197 |     13 |
| 14 | asm_Latn          | Assamese (Latin)  |             53966 |     nan     |    0.000 | 0.000 |     0 |     0 | 1718015 |  53966 |
| 15 | eng               | English           |             50495 |       0.604 |    0.993 | 0.602 | 50122 | 32917 | 1688569 |    373 |
| 16 | guj               | Gujarati          |             50312 |       0.998 |    1.000 | 0.998 | 50299 |   105 | 1721564 |     13 |
| 17 | mal               | Malayalam         |             49607 |       1.000 |    1.000 | 1.000 | 49602 |     7 | 1722367 |      5 |
| 18 | mar               | Marathi           |             49449 |       0.999 |    0.985 | 0.991 | 48688 |    73 | 1722459 |    761 |
| 19 | tel               | Telugu            |             45958 |       1.000 |    1.000 | 1.000 | 45951 |     7 | 1726016 |      7 |
| 20 | tam               | Tamil             |             45230 |       1.000 |    1.000 | 1.000 | 45226 |     5 | 1726746 |      4 |
| 21 | nep_Latn          | Nepali (Latin)    |             43308 |     nan     |    0.000 | 0.000 |     0 |     0 | 1728673 |  43308 |
| 22 | ori               | Odia              |             42513 |       0.999 |    0.998 | 0.998 | 42408 |    32 | 1729436 |    105 |
| 23 | pan               | Punjabi           |             28861 |       1.000 |    0.998 | 0.999 | 28789 |     1 | 1743119 |     72 |
| 24 | asm               | Assamese          |             28278 |       0.999 |    0.936 | 0.966 | 26482 |    22 | 1743681 |   1796 |
| 25 | nep               | Nepali            |             21493 |       0.993 |    0.988 | 0.987 | 21236 |   156 | 1750332 |    257 |
| 26 | urd_Latn          | Urdu (Latin)      |             20504 |     nan     |    0.000 | 0.000 |     0 |     0 | 1751477 |  20504 |
| 27 | urd               | Urdu              |             10770 |       0.996 |    0.976 | 0.984 | 10514 |    46 | 1761165 |    256 |