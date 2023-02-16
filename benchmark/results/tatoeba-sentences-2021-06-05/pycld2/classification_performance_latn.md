# Classification performance for pycld2 on tatoeba-sentences-2021-06-05

- Dataset coverage (sentences in supported languages): 1570047 (45.79%)
- **Aggregated accuracy: 96.87%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |      tp |   fp |      tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|--------:|-----:|--------:|------:|
|  1 | eng               | English    |           1479731 |       1.000 |    0.970 | 0.985 | 1435203 |    0 |   90316 | 44528 |
|  2 | mar               | Marathi    |             64126 |       1.000 |    0.967 | 0.983 |   62024 |   24 | 1505897 |  2102 |
|  3 | hin               | Hindi      |             14230 |       0.918 |    0.973 | 0.907 |   13848 | 1230 | 1554587 |   382 |
|  4 | ben               | Bangla     |              4714 |       0.993 |    0.777 | 0.869 |    3662 |   25 | 1565308 |  1052 |
|  5 | asm               | Assamese   |              2912 |       0.999 |    0.688 | 0.814 |    2003 |    3 | 1567132 |   909 |
|  6 | urd               | Urdu       |              2005 |       1.000 |    0.949 | 0.974 |    1903 |    0 | 1568042 |   102 |
|  7 | mal               | Malayalam  |               827 |       1.000 |    1.000 | 1.000 |     827 |    0 | 1569220 |     0 |
|  8 | ori               | Odia       |               374 |       1.000 |    1.000 | 1.000 |     374 |    0 | 1569673 |     0 |
|  9 | tam               | Tamil      |               334 |       1.000 |    1.000 | 1.000 |     334 |    0 | 1569713 |     0 |
| 10 | tel               | Telugu     |               254 |       1.000 |    1.000 | 1.000 |     254 |    0 | 1569793 |     0 |
| 11 | pan               | Punjabi    |               196 |       1.000 |    1.000 | 1.000 |     196 |    0 | 1569851 |     0 |
| 12 | kan               | Kannada    |               176 |       1.000 |    1.000 | 1.000 |     176 |    0 | 1569871 |     0 |
| 13 | guj               | Gujarati   |               168 |       1.000 |    1.000 | 1.000 |     168 |    0 | 1569879 |     0 |