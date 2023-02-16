# Classification performance for yubilangdetect-v1 on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 1570047 (45.79%)
- **Aggregated accuracy: 99.76%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |      tp |   fp |      tn |   fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|--------:|-----:|--------:|-----:|
|  1 | eng               | English    |           1479731 |       1.000 |    0.998 | 0.999 | 1476405 |    3 |   90313 | 3326 |
|  2 | mar               | Marathi    |             64126 |       0.998 |    0.998 | 0.997 |   63968 |  123 | 1505798 |  158 |
|  3 | hin               | Hindi      |             14230 |       0.990 |    0.990 | 0.985 |   14082 |  145 | 1555672 |  148 |
|  4 | ben               | Bangla     |              4714 |       0.963 |    0.995 | 0.961 |    4690 |  180 | 1565153 |   24 |
|  5 | asm               | Assamese   |              2912 |       0.992 |    0.940 | 0.961 |    2737 |   23 | 1567112 |  175 |
|  6 | urd               | Urdu       |              2005 |       1.000 |    1.000 | 1.000 |    2005 |    0 | 1568042 |    0 |
|  7 | mal               | Malayalam  |               827 |       1.000 |    0.998 | 0.999 |     825 |    0 | 1569220 |    2 |
|  8 | ori               | Odia       |               374 |       1.000 |    1.000 | 1.000 |     374 |    0 | 1569673 |    0 |
|  9 | tam               | Tamil      |               334 |       0.997 |    1.000 | 0.997 |     334 |    1 | 1569712 |    0 |
| 10 | tel               | Telugu     |               254 |       0.981 |    1.000 | 0.981 |     254 |    5 | 1569788 |    0 |
| 11 | pan               | Punjabi    |               196 |       0.995 |    1.000 | 0.995 |     196 |    1 | 1569850 |    0 |
| 12 | kan               | Kannada    |               176 |       0.967 |    1.000 | 0.967 |     176 |    6 | 1569865 |    0 |
| 13 | guj               | Gujarati   |               168 |       0.988 |    1.000 | 0.988 |     168 |    2 | 1569877 |    0 |