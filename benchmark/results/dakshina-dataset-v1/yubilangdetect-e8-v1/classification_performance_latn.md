# Classification performance for yubilangdetect-e8-v1 on dakshina-dataset-v1

- Dataset coverage (sentences in supported languages): 197591 (83.62%)
- **Aggregated accuracy: 87.17%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|------:|-----:|-------:|-----:|
|  1 | mal               | Malayalam         |             10000 |       1.000 |    1.000 | 1.000 | 10000 |    0 | 187591 |    0 |
|  2 | mar               | Marathi           |             10000 |       0.990 |    0.907 | 0.942 |  9067 |   88 | 187503 |  933 |
|  3 | mar_Latn          | Marathi (Latin)   |              9998 |       0.915 |    0.796 | 0.819 |  7955 |  739 | 186854 | 2043 |
|  4 | mal_Latn          | Malayalam (Latin) |              9997 |       0.862 |    0.897 | 0.821 |  8971 | 1439 | 186155 | 1026 |
|  5 | hin               | Hindi             |              9949 |       0.928 |    0.971 | 0.915 |  9657 |  750 | 186892 |  292 |
|  6 | hin_Latn          | Hindi (Latin)     |              9945 |       0.491 |    0.417 | 0.366 |  4152 | 4302 | 183344 | 5793 |
|  7 | kan               | Kannada           |              9945 |       1.000 |    1.000 | 1.000 |  9945 |    0 | 187646 |    0 |
|  8 | kan_Latn          | Kannada (Latin)   |              9944 |       0.842 |    0.937 | 0.818 |  9313 | 1751 | 185896 |  631 |
|  9 | tel               | Telugu            |              9916 |       1.000 |    1.000 | 1.000 |  9916 |    0 | 187675 |    0 |
| 10 | tel_Latn          | Telugu (Latin)    |              9914 |       0.804 |    0.868 | 0.758 |  8604 | 2093 | 185584 | 1310 |
| 11 | guj               | Gujarati          |              9913 |       1.000 |    1.000 | 1.000 |  9913 |    0 | 187678 |    0 |
| 12 | guj_Latn          | Gujarati (Latin)  |              9911 |       0.783 |    0.848 | 0.732 |  8409 | 2329 | 185351 | 1502 |
| 13 | tam               | Tamil             |              9902 |       1.000 |    1.000 | 1.000 |  9901 |    0 | 187689 |    1 |
| 14 | tam_Latn          | Tamil (Latin)     |              9899 |       0.890 |    0.942 | 0.866 |  9324 | 1153 | 186539 |  575 |
| 15 | ben_Latn          | Bangla (Latin)    |              9882 |       0.903 |    0.888 | 0.854 |  8772 |  939 | 186770 | 1110 |
| 16 | ben               | Bangla            |              9882 |       0.999 |    0.999 | 0.999 |  9874 |    9 | 187700 |    8 |
| 17 | pan               | Punjabi           |              9758 |       1.000 |    1.000 | 1.000 |  9758 |    1 | 187832 |    0 |
| 18 | pan_Latn          | Punjabi (Latin)   |              9757 |       0.884 |    0.733 | 0.762 |  7151 |  936 | 186898 | 2606 |
| 19 | urd               | Urdu              |              9541 |       0.999 |    1.000 | 0.999 |  9540 |    5 | 188045 |    1 |
| 20 | urd_Latn          | Urdu (Latin)      |              9538 |       0.787 |    0.212 | 0.319 |  2020 |  547 | 187506 | 7518 |