# Classification performance for langid on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 1570047 (45.79%)
- **Aggregated accuracy: 95.98%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |      tp |    fp |      tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|--------:|------:|--------:|------:|
|  1 | eng               | English    |           1479731 |       1.000 |    0.973 | 0.986 | 1439788 |     0 |   90316 | 39943 |
|  2 | mar               | Marathi    |             64126 |       0.988 |    0.700 | 0.815 |   44902 |   563 | 1505358 | 19224 |
|  3 | hin               | Hindi      |             14230 |       0.420 |    0.901 | 0.410 |   12825 | 17726 | 1538091 |  1405 |
|  4 | ben               | Bangla     |              4714 |       0.672 |    0.977 | 0.667 |    4605 |  2248 | 1563085 |   109 |
|  5 | asm               | Assamese   |              2912 |       0.859 |    0.227 | 0.349 |     662 |   109 | 1567026 |  2250 |
|  6 | urd               | Urdu       |              2005 |       1.000 |    0.948 | 0.973 |    1901 |     0 | 1568042 |   104 |
|  7 | mal               | Malayalam  |               827 |       1.000 |    1.000 | 1.000 |     827 |     0 | 1569220 |     0 |
|  8 | ori               | Odia       |               374 |       1.000 |    0.992 | 0.996 |     371 |     0 | 1569673 |     3 |
|  9 | tam               | Tamil      |               334 |       1.000 |    1.000 | 1.000 |     334 |     0 | 1569713 |     0 |
| 10 | tel               | Telugu     |               254 |       1.000 |    1.000 | 1.000 |     254 |     0 | 1569793 |     0 |
| 11 | pan               | Punjabi    |               196 |       1.000 |    1.000 | 1.000 |     196 |     0 | 1569851 |     0 |
| 12 | kan               | Kannada    |               176 |       1.000 |    1.000 | 1.000 |     176 |     0 | 1569871 |     0 |
| 13 | guj               | Gujarati   |               168 |       1.000 |    1.000 | 1.000 |     168 |     0 | 1569879 |     0 |