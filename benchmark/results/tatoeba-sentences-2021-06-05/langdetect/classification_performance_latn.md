# Classification performance for langdetect on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 1570047 (45.79%)
- **Aggregated accuracy: 93.20%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |      tp |   fp |      tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|--------:|-----:|--------:|------:|
|  1 | eng               | English    |           1479731 |       1.000 |    0.933 | 0.966 | 1381210 |    0 |   90316 | 98521 |
|  2 | mar               | Marathi    |             64126 |       0.997 |    0.933 | 0.962 |   59818 |  195 | 1505726 |  4308 |
|  3 | hin               | Hindi      |             14230 |       0.787 |    0.957 | 0.774 |   13619 | 3680 | 1552137 |   611 |
|  4 | ben               | Bangla     |              4714 |       0.618 |    1.000 | 0.618 |    4714 | 2912 | 1562421 |     0 |
|  5 | asm               | Assamese   |              2912 |     nan     |    0.000 | 0.000 |       0 |    0 | 1567135 |  2912 |
|  6 | urd               | Urdu       |              2005 |       1.000 |    0.993 | 0.996 |    1990 |    0 | 1568042 |    15 |
|  7 | mal               | Malayalam  |               827 |       1.000 |    1.000 | 1.000 |     827 |    0 | 1569220 |     0 |
|  8 | ori               | Odia       |               374 |     nan     |    0.000 | 0.000 |       0 |    0 | 1569673 |   374 |
|  9 | tam               | Tamil      |               334 |       1.000 |    1.000 | 1.000 |     334 |    0 | 1569713 |     0 |
| 10 | tel               | Telugu     |               254 |       1.000 |    1.000 | 1.000 |     254 |    0 | 1569793 |     0 |
| 11 | pan               | Punjabi    |               196 |       0.585 |    1.000 | 0.585 |     196 |  139 | 1569712 |     0 |
| 12 | kan               | Kannada    |               176 |       1.000 |    1.000 | 1.000 |     176 |    0 | 1569871 |     0 |
| 13 | guj               | Gujarati   |               168 |       1.000 |    1.000 | 1.000 |     168 |    0 | 1569879 |     0 |