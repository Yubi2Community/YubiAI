# Classification performance for yulan-e4-v1 on dakshina-dataset-v1

- Dataset coverage (sentences in supported languages): 197591 (83.62%)
- **Aggregated accuracy: 80.12%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|-------:|-----:|
|  1 | mal               | Malayalam         |             10000 |       1.000 |    1.000 | 1.000 | 9999 |    2 | 187589 |    1 |
|  2 | mar               | Marathi           |             10000 |       0.974 |    0.939 | 0.945 | 9391 |  246 | 187345 |  609 |
|  3 | mar_Latn          | Marathi (Latin)   |              9998 |       0.712 |    0.747 | 0.635 | 7464 | 3020 | 184573 | 2534 |
|  4 | mal_Latn          | Malayalam (Latin) |              9997 |       0.705 |    0.580 | 0.562 | 5799 | 2427 | 185167 | 4198 |
|  5 | hin               | Hindi             |              9949 |       0.943 |    0.974 | 0.931 | 9687 |  586 | 187056 |  262 |
|  6 | hin_Latn          | Hindi (Latin)     |              9945 |       0.479 |    0.341 | 0.328 | 3396 | 3695 | 183951 | 6549 |
|  7 | kan               | Kannada           |              9945 |       0.999 |    1.000 | 0.999 | 9945 |    8 | 187638 |    0 |
|  8 | kan_Latn          | Kannada (Latin)   |              9944 |       0.748 |    0.857 | 0.704 | 8518 | 2863 | 184784 | 1426 |
|  9 | tel               | Telugu            |              9916 |       1.000 |    1.000 | 1.000 | 9916 |    2 | 187673 |    0 |
| 10 | tel_Latn          | Telugu (Latin)    |              9914 |       0.768 |    0.638 | 0.631 | 6326 | 1911 | 185766 | 3588 |
| 11 | guj               | Gujarati          |              9913 |       1.000 |    1.000 | 1.000 | 9912 |    0 | 187678 |    1 |
| 12 | guj_Latn          | Gujarati (Latin)  |              9911 |       0.610 |    0.673 | 0.532 | 6674 | 4261 | 183419 | 3237 |
| 13 | tam               | Tamil             |              9902 |       1.000 |    1.000 | 1.000 | 9902 |    2 | 187687 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              9899 |       0.742 |    0.692 | 0.637 | 6854 | 2377 | 185315 | 3045 |
| 15 | ben_Latn          | Bangla (Latin)    |              9882 |       0.823 |    0.735 | 0.717 | 7262 | 1558 | 186151 | 2620 |
| 16 | ben               | Bangla            |              9882 |       1.000 |    0.981 | 0.990 | 9690 |    4 | 187705 |  192 |
| 17 | pan               | Punjabi           |              9758 |       1.000 |    1.000 | 1.000 | 9757 |    2 | 187831 |    1 |
| 18 | pan_Latn          | Punjabi (Latin)   |              9757 |       0.835 |    0.676 | 0.696 | 6600 | 1304 | 186530 | 3157 |
| 19 | urd               | Urdu              |              9541 |       1.000 |    0.999 | 0.999 | 9531 |    4 | 188046 |   10 |
| 20 | urd_Latn          | Urdu (Latin)      |              9538 |       0.654 |    0.176 | 0.259 | 1680 |  887 | 187166 | 7858 |