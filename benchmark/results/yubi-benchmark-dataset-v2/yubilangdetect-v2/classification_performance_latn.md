# Classification performance for yubilangdetect-v2 on yubi-benchmark-dataset-v2

- Dataset coverage (sentences in supported languages): 80144 (100.00%)
- **Aggregated accuracy: 93.94%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben_Latn          | Bangla (Latin)    |              5954 |       0.940 |    0.931 | 0.909 | 5542 |  352 | 73838 |  412 |
|  2 | mal_Latn          | Malayalam (Latin) |              5374 |       0.948 |    0.933 | 0.917 | 5013 |  275 | 74495 |  361 |
|  3 | kan_Latn          | Kannada (Latin)   |              5068 |       0.931 |    0.904 | 0.886 | 4579 |  342 | 74734 |  489 |
|  4 | tam_Latn          | Tamil (Latin)     |              4706 |       0.956 |    0.948 | 0.932 | 4461 |  205 | 75233 |  245 |
|  5 | hin_Latn          | Hindi (Latin)     |              4354 |       0.802 |    0.891 | 0.764 | 3878 |  959 | 74831 |  476 |
|  6 | tel_Latn          | Telugu (Latin)    |              4288 |       0.895 |    0.884 | 0.845 | 3790 |  446 | 75410 |  498 |
|  7 | mal               | Malayalam         |              3992 |       1.000 |    1.000 | 1.000 | 3992 |    0 | 76152 |    0 |
|  8 | mar_Latn          | Marathi (Latin)   |              3915 |       0.946 |    0.917 | 0.908 | 3591 |  203 | 76026 |  324 |
|  9 | guj_Latn          | Gujarati (Latin)  |              3749 |       0.880 |    0.885 | 0.832 | 3317 |  452 | 75943 |  432 |
| 10 | kan               | Kannada           |              3431 |       1.000 |    1.000 | 1.000 | 3431 |    0 | 76713 |    0 |
| 11 | ben               | Bangla            |              3387 |       0.989 |    1.000 | 0.989 | 3386 |   37 | 76720 |    1 |
| 12 | tam               | Tamil             |              3344 |       1.000 |    1.000 | 1.000 | 3344 |    1 | 76799 |    0 |
| 13 | tel               | Telugu            |              2881 |       1.000 |    1.000 | 1.000 | 2881 |    0 | 77263 |    0 |
| 14 | ori_Latn          | Odia (Latin)      |              2798 |       0.955 |    0.948 | 0.931 | 2653 |  125 | 77221 |  145 |
| 15 | nep_Latn          | Nepali (Latin)    |              2765 |       0.853 |    0.900 | 0.814 | 2489 |  430 | 76949 |  276 |
| 16 | hin               | Hindi             |              2583 |       0.888 |    0.913 | 0.852 | 2359 |  299 | 77262 |  224 |
| 17 | mar               | Marathi           |              2411 |       0.956 |    0.910 | 0.913 | 2195 |  100 | 77633 |  216 |
| 18 | guj               | Gujarati          |              2283 |       1.000 |    1.000 | 1.000 | 2283 |    0 | 77861 |    0 |
| 19 | nep               | Nepali            |              2089 |       0.912 |    0.930 | 0.882 | 1943 |  187 | 77868 |  146 |
| 20 | pan_Latn          | Punjabi (Latin)   |              2085 |       0.926 |    0.844 | 0.853 | 1759 |  141 | 77918 |  326 |
| 21 | asm_Latn          | Assamese (Latin)  |              1731 |       0.973 |    0.967 | 0.957 | 1674 |   46 | 78367 |   57 |
| 22 | eng               | English           |              1564 |       0.998 |    0.998 | 0.997 | 1561 |    3 | 78577 |    3 |
| 23 | ori               | Odia              |              1450 |       1.000 |    1.000 | 1.000 | 1450 |    0 | 78694 |    0 |
| 24 | pan               | Punjabi           |              1213 |       1.000 |    1.000 | 1.000 | 1213 |    0 | 78931 |    0 |
| 25 | urd_Latn          | Urdu (Latin)      |               993 |       0.763 |    0.813 | 0.702 |  807 |  250 | 78901 |  186 |
| 26 | asm               | Assamese          |               925 |       0.999 |    0.960 | 0.979 |  888 |    1 | 79218 |   37 |
| 27 | urd               | Urdu              |               811 |       1.000 |    1.000 | 1.000 |  811 |    0 | 79333 |    0 |