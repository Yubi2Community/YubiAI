# Classification performance for yubilangdetect-e8-v1 on yubi-benchmark-dataset-v2

- Dataset coverage (sentences in supported languages): 80144 (100.00%)
- **Aggregated accuracy: 94.31%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |    tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|------:|-----:|
|  1 | ben_Latn          | Bangla (Latin)    |              5954 |       0.941 |    0.938 | 0.913 | 5584 |  347 | 73843 |  370 |
|  2 | mal_Latn          | Malayalam (Latin) |              5374 |       0.953 |    0.938 | 0.923 | 5040 |  251 | 74519 |  334 |
|  3 | kan_Latn          | Kannada (Latin)   |              5068 |       0.938 |    0.915 | 0.899 | 4635 |  306 | 74770 |  433 |
|  4 | tam_Latn          | Tamil (Latin)     |              4706 |       0.958 |    0.954 | 0.936 | 4488 |  199 | 75239 |  218 |
|  5 | hin_Latn          | Hindi (Latin)     |              4354 |       0.798 |    0.895 | 0.763 | 3895 |  983 | 74807 |  459 |
|  6 | tel_Latn          | Telugu (Latin)    |              4288 |       0.900 |    0.897 | 0.856 | 3848 |  428 | 75428 |  440 |
|  7 | mal               | Malayalam         |              3992 |       1.000 |    1.000 | 1.000 | 3992 |    0 | 76152 |    0 |
|  8 | mar_Latn          | Marathi (Latin)   |              3915 |       0.959 |    0.915 | 0.918 | 3584 |  153 | 76076 |  331 |
|  9 | guj_Latn          | Gujarati (Latin)  |              3749 |       0.899 |    0.889 | 0.851 | 3332 |  374 | 76021 |  417 |
| 10 | kan               | Kannada           |              3431 |       1.000 |    1.000 | 1.000 | 3431 |    0 | 76713 |    0 |
| 11 | ben               | Bangla            |              3387 |       0.990 |    1.000 | 0.990 | 3386 |   35 | 76722 |    1 |
| 12 | tam               | Tamil             |              3344 |       1.000 |    1.000 | 1.000 | 3344 |    0 | 76800 |    0 |
| 13 | tel               | Telugu            |              2881 |       1.000 |    1.000 | 1.000 | 2881 |    0 | 77263 |    0 |
| 14 | ori_Latn          | Odia (Latin)      |              2798 |       0.962 |    0.952 | 0.939 | 2663 |  105 | 77241 |  135 |
| 15 | nep_Latn          | Nepali (Latin)    |              2765 |       0.863 |    0.898 | 0.823 | 2484 |  394 | 76985 |  281 |
| 16 | hin               | Hindi             |              2583 |       0.884 |    0.923 | 0.853 | 2385 |  312 | 77249 |  198 |
| 17 | mar               | Marathi           |              2411 |       0.959 |    0.905 | 0.913 | 2183 |   94 | 77639 |  228 |
| 18 | guj               | Gujarati          |              2283 |       1.000 |    1.000 | 1.000 | 2283 |    0 | 77861 |    0 |
| 19 | nep               | Nepali            |              2089 |       0.919 |    0.928 | 0.887 | 1938 |  171 | 77884 |  151 |
| 20 | pan_Latn          | Punjabi (Latin)   |              2085 |       0.933 |    0.855 | 0.864 | 1783 |  129 | 77930 |  302 |
| 21 | asm_Latn          | Assamese (Latin)  |              1731 |       0.980 |    0.966 | 0.964 | 1673 |   34 | 78379 |   58 |
| 22 | eng               | English           |              1564 |       0.997 |    0.998 | 0.996 | 1561 |    4 | 78576 |    3 |
| 23 | ori               | Odia              |              1450 |       1.000 |    1.000 | 1.000 | 1450 |    0 | 78694 |    0 |
| 24 | pan               | Punjabi           |              1213 |       1.000 |    1.000 | 1.000 | 1213 |    0 | 78931 |    0 |
| 25 | urd_Latn          | Urdu (Latin)      |               993 |       0.777 |    0.835 | 0.721 |  829 |  238 | 78913 |  164 |
| 26 | asm               | Assamese          |               925 |       0.999 |    0.962 | 0.980 |  890 |    1 | 79218 |   35 |
| 27 | urd               | Urdu              |               811 |       1.000 |    1.000 | 1.000 |  811 |    0 | 79333 |    0 |