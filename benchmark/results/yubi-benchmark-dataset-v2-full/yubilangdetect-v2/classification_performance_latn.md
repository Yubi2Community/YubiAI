# Classification performance for yubilangdetect-v2 on yubi-benchmark-dataset-v2-full

- Dataset coverage (sentences in supported languages): 2671383 (100.00%)
- **Aggregated accuracy: 93.79%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |     tp |    fp |      tn |    fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-------:|------:|--------:|------:|
|  1 | ben_Latn          | Bangla (Latin)    |            198442 |       0.940 |    0.929 | 0.907 | 184276 | 11823 | 2461118 | 14166 |
|  2 | mal_Latn          | Malayalam (Latin) |            183874 |       0.945 |    0.933 | 0.914 | 171495 |  9999 | 2477510 | 12379 |
|  3 | kan_Latn          | Kannada (Latin)   |            171671 |       0.925 |    0.904 | 0.882 | 155171 | 12578 | 2487134 | 16500 |
|  4 | tam_Latn          | Tamil (Latin)     |            156564 |       0.954 |    0.942 | 0.927 | 147465 |  7060 | 2507759 |  9099 |
|  5 | hin_Latn          | Hindi (Latin)     |            147189 |       0.806 |    0.885 | 0.766 | 130234 | 31355 | 2492839 | 16955 |
|  6 | tel_Latn          | Telugu (Latin)    |            141218 |       0.892 |    0.891 | 0.845 | 125811 | 15293 | 2514872 | 15407 |
|  7 | mal               | Malayalam         |            133162 |       1.000 |    1.000 | 1.000 | 133161 |     1 | 2538220 |     1 |
|  8 | mar_Latn          | Marathi (Latin)   |            128763 |       0.942 |    0.920 | 0.905 | 118427 |  7292 | 2535328 | 10336 |
|  9 | guj_Latn          | Gujarati (Latin)  |            124835 |       0.879 |    0.882 | 0.830 | 110084 | 15130 | 2531418 | 14751 |
| 10 | kan               | Kannada           |            114958 |       1.000 |    1.000 | 1.000 | 114958 |     5 | 2556420 |     0 |
| 11 | ben               | Bangla            |            111340 |       0.987 |    0.999 | 0.987 | 111260 |  1444 | 2558599 |    80 |
| 12 | tam               | Tamil             |            110537 |       1.000 |    1.000 | 1.000 | 110536 |     1 | 2560845 |     1 |
| 13 | tel               | Telugu            |             95609 |       1.000 |    1.000 | 1.000 |  95608 |     0 | 2575774 |     1 |
| 14 | ori_Latn          | Odia (Latin)      |             92042 |       0.958 |    0.940 | 0.930 |  86529 |  3803 | 2575538 |  5513 |
| 15 | nep_Latn          | Nepali (Latin)    |             91363 |       0.848 |    0.897 | 0.809 |  81996 | 14716 | 2565304 |  9367 |
| 16 | hin               | Hindi             |             86513 |       0.883 |    0.918 | 0.849 |  79418 | 10556 | 2574314 |  7095 |
| 17 | mar               | Marathi           |             79305 |       0.956 |    0.908 | 0.912 |  72008 |  3294 | 2588784 |  7297 |
| 18 | guj               | Gujarati          |             74297 |       1.000 |    1.000 | 1.000 |  74296 |     2 | 2597084 |     1 |
| 19 | nep               | Nepali            |             69884 |       0.914 |    0.921 | 0.880 |  64374 |  6062 | 2595437 |  5510 |
| 20 | pan_Latn          | Punjabi (Latin)   |             69079 |       0.919 |    0.839 | 0.845 |  57932 |  5090 | 2597214 | 11147 |
| 21 | asm_Latn          | Assamese (Latin)  |             58129 |       0.975 |    0.965 | 0.958 |  56101 |  1464 | 2611790 |  2028 |
| 22 | eng               | English           |             50759 |       0.997 |    0.998 | 0.996 |  50638 |   156 | 2620468 |   121 |
| 23 | ori               | Odia              |             49645 |       1.000 |    1.000 | 1.000 |  49643 |     1 | 2621737 |     2 |
| 24 | pan               | Punjabi           |             39690 |       1.000 |    1.000 | 1.000 |  39690 |     6 | 2631687 |     0 |
| 25 | urd_Latn          | Urdu (Latin)      |             34855 |       0.763 |    0.806 | 0.699 |  28110 |  8735 | 2627793 |  6745 |
| 26 | asm               | Assamese          |             32307 |       0.998 |    0.955 | 0.975 |  30868 |    76 | 2639000 |  1439 |
| 27 | urd               | Urdu              |             25353 |       1.000 |    1.000 | 1.000 |  25352 |     0 | 2646030 |     1 |