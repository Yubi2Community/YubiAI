# Classification performance for gcld3 on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 1570047 (45.79%)
- **Aggregated accuracy: 85.23%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |      tp |   fp |      tn |     fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|--------:|-----:|--------:|-------:|
|  1 | eng               | English    |           1479731 |       1.000 |    0.851 | 0.919 | 1258584 |   12 |   90304 | 221147 |
|  2 | mar               | Marathi    |             64126 |       0.989 |    0.911 | 0.943 |   58406 |  669 | 1505252 |   5720 |
|  3 | hin               | Hindi      |             14230 |       0.760 |    0.880 | 0.723 |   12526 | 3947 | 1551870 |   1704 |
|  4 | ben               | Bangla     |              4714 |       0.618 |    0.998 | 0.618 |    4704 | 2902 | 1562431 |     10 |
|  5 | asm               | Assamese   |              2912 |     nan     |    0.000 | 0.000 |       0 |    0 | 1567135 |   2912 |
|  6 | urd               | Urdu       |              2005 |       0.984 |    0.963 | 0.965 |    1930 |   32 | 1568010 |     75 |
|  7 | mal               | Malayalam  |               827 |       1.000 |    1.000 | 1.000 |     827 |    0 | 1569220 |      0 |
|  8 | ori               | Odia       |               374 |     nan     |    0.000 | 0.000 |       0 |    0 | 1569673 |    374 |
|  9 | tam               | Tamil      |               334 |       1.000 |    1.000 | 1.000 |     334 |    0 | 1569713 |      0 |
| 10 | tel               | Telugu     |               254 |       1.000 |    1.000 | 1.000 |     254 |    0 | 1569793 |      0 |
| 11 | pan               | Punjabi    |               196 |       1.000 |    0.995 | 0.997 |     195 |    0 | 1569851 |      1 |
| 12 | kan               | Kannada    |               176 |       1.000 |    1.000 | 1.000 |     176 |    0 | 1569871 |      0 |
| 13 | guj               | Gujarati   |               168 |       1.000 |    0.982 | 0.991 |     165 |    0 | 1569879 |      3 |