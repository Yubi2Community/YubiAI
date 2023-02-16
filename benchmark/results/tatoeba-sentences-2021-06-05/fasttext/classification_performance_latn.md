# Classification performance for fasttext on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 1570047 (45.79%)
- **Aggregated accuracy: 99.83%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |      tp |   fp |      tn |   fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|--------:|-----:|--------:|-----:|
|  1 | eng               | English    |           1479731 |       1.000 |    0.999 | 1.000 | 1478395 |   11 |   90305 | 1336 |
|  2 | mar               | Marathi    |             64126 |       0.999 |    0.998 | 0.998 |   64016 |   96 | 1505825 |  110 |
|  3 | hin               | Hindi      |             14230 |       0.994 |    0.989 | 0.989 |   14076 |   81 | 1555736 |  154 |
|  4 | ben               | Bangla     |              4714 |       0.847 |    0.999 | 0.847 |    4709 |  851 | 1564482 |    5 |
|  5 | asm               | Assamese   |              2912 |       1.000 |    0.691 | 0.817 |    2011 |    1 | 1567134 |  901 |
|  6 | urd               | Urdu       |              2005 |       1.000 |    0.984 | 0.992 |    1972 |    0 | 1568042 |   33 |
|  7 | mal               | Malayalam  |               827 |       1.000 |    1.000 | 1.000 |     827 |    0 | 1569220 |    0 |
|  8 | ori               | Odia       |               374 |       0.997 |    0.794 | 0.883 |     297 |    1 | 1569672 |   77 |
|  9 | tam               | Tamil      |               334 |       0.985 |    1.000 | 0.985 |     334 |    5 | 1569708 |    0 |
| 10 | tel               | Telugu     |               254 |       0.988 |    1.000 | 0.988 |     254 |    3 | 1569790 |    0 |
| 11 | pan               | Punjabi    |               196 |       0.995 |    1.000 | 0.995 |     196 |    1 | 1569850 |    0 |
| 12 | kan               | Kannada    |               176 |       0.989 |    1.000 | 0.989 |     176 |    2 | 1569869 |    0 |
| 13 | guj               | Gujarati   |               168 |       1.000 |    1.000 | 1.000 |     168 |    0 | 1569879 |    0 |