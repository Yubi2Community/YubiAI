# Classification performance for fasttext-compressed on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 1570047 (45.79%)
- **Aggregated accuracy: 99.52%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |      tp |   fp |      tn |   fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|--------:|-----:|--------:|-----:|
|  1 | eng               | English    |           1479731 |       1.000 |    0.997 | 0.998 | 1475221 |   40 |   90276 | 4510 |
|  2 | mar               | Marathi    |             64126 |       0.993 |    0.984 | 0.985 |   63072 |  431 | 1505490 | 1054 |
|  3 | hin               | Hindi      |             14230 |       0.933 |    0.962 | 0.916 |   13687 |  985 | 1554832 |  543 |
|  4 | ben               | Bangla     |              4714 |       0.805 |    0.996 | 0.803 |    4693 | 1139 | 1564194 |   21 |
|  5 | asm               | Assamese   |              2912 |       0.995 |    0.594 | 0.742 |    1729 |    9 | 1567126 | 1183 |
|  6 | urd               | Urdu       |              2005 |       0.999 |    0.955 | 0.976 |    1915 |    2 | 1568040 |   90 |
|  7 | mal               | Malayalam  |               827 |       1.000 |    0.999 | 0.999 |     826 |    0 | 1569220 |    1 |
|  8 | ori               | Odia       |               374 |       1.000 |    0.741 | 0.851 |     277 |    0 | 1569673 |   97 |
|  9 | tam               | Tamil      |               334 |       0.997 |    1.000 | 0.997 |     334 |    1 | 1569712 |    0 |
| 10 | tel               | Telugu     |               254 |       0.969 |    1.000 | 0.969 |     254 |    8 | 1569785 |    0 |
| 11 | pan               | Punjabi    |               196 |       0.990 |    1.000 | 0.990 |     196 |    2 | 1569849 |    0 |
| 12 | kan               | Kannada    |               176 |       0.983 |    1.000 | 0.983 |     176 |    3 | 1569868 |    0 |
| 13 | guj               | Gujarati   |               168 |       1.000 |    1.000 | 1.000 |     168 |    0 | 1569879 |    0 |