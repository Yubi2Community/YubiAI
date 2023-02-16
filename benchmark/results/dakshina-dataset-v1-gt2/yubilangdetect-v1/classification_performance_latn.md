# Classification performance for yubilangdetect-v1 on dakshina-dataset-v1-gt2

- Dataset coverage (sentences in supported languages): 180013 (82.92%)
- **Aggregated accuracy: 82.66%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|-------:|-----:|
|  1 | kan               | Kannada           |              9417 |       1.000 |    1.000 | 1.000 | 9417 |    0 | 170596 |    0 |
|  2 | kan_Latn          | Kannada (Latin)   |              9416 |       0.820 |    0.885 | 0.779 | 8333 | 1826 | 168771 | 1083 |
|  3 | guj               | Gujarati          |              9330 |       1.000 |    1.000 | 1.000 | 9330 |    0 | 170683 |    0 |
|  4 | guj_Latn          | Gujarati (Latin)  |              9328 |       0.624 |    0.709 | 0.553 | 6618 | 3991 | 166694 | 2710 |
|  5 | pan               | Punjabi           |              9305 |       1.000 |    1.000 | 1.000 | 9305 |    1 | 170707 |    0 |
|  6 | pan_Latn          | Punjabi (Latin)   |              9305 |       0.861 |    0.706 | 0.730 | 6566 | 1063 | 169645 | 2739 |
|  7 | hin               | Hindi             |              9193 |       0.979 |    0.994 | 0.976 | 9139 |  195 | 170625 |   54 |
|  8 | hin_Latn          | Hindi (Latin)     |              9189 |       0.506 |    0.362 | 0.350 | 3328 | 3243 | 167581 | 5861 |
|  9 | ben_Latn          | Bangla (Latin)    |              9139 |       0.864 |    0.783 | 0.772 | 7154 | 1126 | 169748 | 1985 |
| 10 | ben               | Bangla            |              9137 |       1.000 |    0.998 | 0.999 | 9119 |    2 | 170874 |   18 |
| 11 | mal               | Malayalam         |              9017 |       1.000 |    1.000 | 1.000 | 9017 |    0 | 170996 |    0 |
| 12 | mal_Latn          | Malayalam (Latin) |              9015 |       0.730 |    0.622 | 0.597 | 5604 | 2074 | 168924 | 3411 |
| 13 | tam               | Tamil             |              8818 |       1.000 |    1.000 | 1.000 | 8818 |    0 | 171195 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              8817 |       0.778 |    0.745 | 0.687 | 6571 | 1870 | 169326 | 2246 |
| 15 | mar               | Marathi           |              8803 |       0.995 |    0.977 | 0.984 | 8603 |   41 | 171169 |  200 |
| 16 | mar_Latn          | Marathi (Latin)   |              8799 |       0.765 |    0.820 | 0.706 | 7211 | 2212 | 169002 | 1588 |
| 17 | urd               | Urdu              |              8529 |       1.000 |    1.000 | 1.000 | 8529 |    3 | 171481 |    0 |
| 18 | urd_Latn          | Urdu (Latin)      |              8493 |       0.667 |    0.191 | 0.276 | 1621 |  810 | 170710 | 6872 |
| 19 | tel_Latn          | Telugu (Latin)    |              8482 |       0.806 |    0.711 | 0.693 | 6033 | 1453 | 170078 | 2449 |
| 20 | tel               | Telugu            |              8481 |       1.000 |    1.000 | 1.000 | 8481 |    0 | 171532 |    0 |