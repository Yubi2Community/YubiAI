# Classification performance for yulan-e4-v2 on dakshina-dataset-v1

- Dataset coverage (sentences in supported languages): 197591 (83.62%)
- **Aggregated accuracy: 88.48%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|------:|-----:|-------:|-----:|
|  1 | mal               | Malayalam         |             10000 |       1.000 |    1.000 | 1.000 | 10000 |    0 | 187591 |    0 |
|  2 | mar               | Marathi           |             10000 |       0.991 |    0.913 | 0.946 |  9128 |   82 | 187509 |  872 |
|  3 | mar_Latn          | Marathi (Latin)   |              9998 |       0.929 |    0.798 | 0.832 |  7980 |  607 | 186986 | 2018 |
|  4 | mal_Latn          | Malayalam (Latin) |              9997 |       0.883 |    0.898 | 0.841 |  8975 | 1191 | 186403 | 1022 |
|  5 | hin               | Hindi             |              9949 |       0.935 |    0.967 | 0.920 |  9623 |  669 | 186973 |  326 |
|  6 | hin_Latn          | Hindi (Latin)     |              9945 |       0.503 |    0.542 | 0.415 |  5387 | 5323 | 182323 | 4558 |
|  7 | kan               | Kannada           |              9945 |       1.000 |    1.000 | 1.000 |  9945 |    1 | 187645 |    0 |
|  8 | kan_Latn          | Kannada (Latin)   |              9944 |       0.880 |    0.934 | 0.853 |  9288 | 1271 | 186376 |  656 |
|  9 | tel               | Telugu            |              9916 |       0.999 |    1.000 | 0.999 |  9916 |    6 | 187669 |    0 |
| 10 | tel_Latn          | Telugu (Latin)    |              9914 |       0.840 |    0.873 | 0.792 |  8651 | 1644 | 186033 | 1263 |
| 11 | guj               | Gujarati          |              9913 |       1.000 |    1.000 | 1.000 |  9912 |    0 | 187678 |    1 |
| 12 | guj_Latn          | Gujarati (Latin)  |              9911 |       0.786 |    0.872 | 0.743 |  8639 | 2351 | 185329 | 1272 |
| 13 | tam               | Tamil             |              9902 |       1.000 |    1.000 | 1.000 |  9902 |    1 | 187688 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              9899 |       0.913 |    0.943 | 0.888 |  9336 |  895 | 186797 |  563 |
| 15 | ben_Latn          | Bangla (Latin)    |              9882 |       0.922 |    0.879 | 0.867 |  8686 |  738 | 186971 | 1196 |
| 16 | ben               | Bangla            |              9882 |       0.999 |    0.999 | 0.999 |  9871 |    6 | 187703 |   11 |
| 17 | pan               | Punjabi           |              9758 |       1.000 |    1.000 | 1.000 |  9758 |    1 | 187832 |    0 |
| 18 | pan_Latn          | Punjabi (Latin)   |              9757 |       0.890 |    0.755 | 0.777 |  7363 |  913 | 186921 | 2394 |
| 19 | urd               | Urdu              |              9541 |       0.999 |    1.000 | 0.999 |  9538 |    5 | 188045 |    3 |
| 20 | urd_Latn          | Urdu (Latin)      |              9538 |       0.815 |    0.308 | 0.425 |  2935 |  668 | 187385 | 6603 |