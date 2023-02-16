# Classification performance for yubilangdetect-e8-v1 on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 94.11%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |     tp |    fp |      tn |    fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-------:|------:|--------:|------:|
|  1 | ben_Latn          | Bangla (Latin)    |            198442 |       0.938 |    0.935 | 0.909 | 185564 | 12184 | 2460757 | 12878 |
|  2 | mal_Latn          | Malayalam (Latin) |            183874 |       0.949 |    0.937 | 0.920 | 172206 |  9190 | 2478319 | 11668 |
|  3 | kan_Latn          | Kannada (Latin)   |            171671 |       0.933 |    0.910 | 0.892 | 156254 | 11250 | 2488462 | 15417 |
|  4 | tam_Latn          | Tamil (Latin)     |            156564 |       0.956 |    0.947 | 0.931 | 148268 |  6760 | 2508059 |  8296 |
|  5 | hin_Latn          | Hindi (Latin)     |            147189 |       0.797 |    0.892 | 0.761 | 131319 | 33350 | 2490844 | 15870 |
|  6 | tel_Latn          | Telugu (Latin)    |            141218 |       0.894 |    0.900 | 0.852 | 127140 | 15100 | 2515065 | 14078 |
|  7 | mal               | Malayalam         |            133162 |       1.000 |    1.000 | 1.000 | 133161 |     1 | 2538220 |     1 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |       0.950 |    0.921 | 0.913 | 118565 |  6219 | 2536401 | 10198 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |       0.898 |    0.884 | 0.848 | 110364 | 12556 | 2533992 | 14471 |
| 10 | kan               | Kannada           |            114958 |       1.000 |    1.000 | 1.000 | 114958 |     2 | 2556423 |     0 |
| 11 | ben               | Bangla            |            111340 |       0.988 |    0.999 | 0.987 | 111259 |  1385 | 2558658 |    81 |
| 12 | tam               | Tamil             |            110537 |       1.000 |    1.000 | 1.000 | 110534 |     0 | 2560846 |     3 |
| 13 | tel               | Telugu            |             95609 |       1.000 |    1.000 | 1.000 |  95607 |     0 | 2575774 |     2 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |       0.963 |    0.944 | 0.936 |  86864 |  3312 | 2576029 |  5178 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |       0.867 |    0.901 | 0.827 |  82304 | 12661 | 2567359 |  9059 |
| 16 | hin               | Hindi             |             86513 |       0.881 |    0.923 | 0.850 |  79844 | 10810 | 2574060 |  6669 |
| 17 | mar               | Marathi           |             79305 |       0.959 |    0.906 | 0.914 |  71885 |  3036 | 2589042 |  7420 |
| 18 | guj               | Gujarati          |             74297 |       1.000 |    1.000 | 1.000 |  74296 |     1 | 2597085 |     1 |
| 19 | nep               | Nepali            |             69884 |       0.919 |    0.922 | 0.885 |  64444 |  5692 | 2595807 |  5440 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |       0.922 |    0.844 | 0.850 |  58289 |  4900 | 2597404 | 10790 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |       0.981 |    0.966 | 0.965 |  56145 |  1070 | 2612184 |  1984 |
| 22 | eng               | English           |             50759 |       0.998 |    0.998 | 0.997 |  50641 |   110 | 2620514 |   118 |
| 23 | ori               | Odia              |             49645 |       1.000 |    1.000 | 1.000 |  49644 |     0 | 2621738 |     1 |
| 24 | pan               | Punjabi           |             39690 |       1.000 |    1.000 | 1.000 |  39690 |     4 | 2631689 |     0 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |       0.788 |    0.818 | 0.725 |  28522 |  7667 | 2628861 |  6333 |
| 26 | asm               | Assamese          |             32307 |       0.997 |    0.957 | 0.976 |  30924 |    80 | 2638996 |  1383 |
| 27 | urd               | Urdu              |             25353 |       1.000 |    1.000 | 1.000 |  25352 |     0 | 2646030 |     1 |