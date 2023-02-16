# Classification performance for langid on dakshina-dataset-v1

- Dataset coverage (sentences in supported languages): 197591 (83.62%)
- **Aggregated accuracy: 47.62%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|------:|-----:|-------:|-----:|
|  1 | mal               | Malayalam         |             10000 |       1.000 |    1.000 | 1.000 | 10000 |    0 | 187591 |    0 |
|  2 | mar               | Marathi           |             10000 |       0.898 |    0.849 | 0.832 |  8493 |  960 | 186631 | 1507 |
|  3 | mar_Latn          | Marathi (Latin)   |              9998 |     nan     |    0.000 | 0.000 |     0 |    0 | 187593 | 9998 |
|  4 | mal_Latn          | Malayalam (Latin) |              9997 |     nan     |    0.000 | 0.000 |     0 |    0 | 187594 | 9997 |
|  5 | hin               | Hindi             |              9949 |       0.888 |    0.854 | 0.825 |  8497 | 1076 | 186566 | 1452 |
|  6 | hin_Latn          | Hindi (Latin)     |              9945 |     nan     |    0.000 | 0.000 |     0 |    0 | 187646 | 9945 |
|  7 | kan               | Kannada           |              9945 |       1.000 |    1.000 | 1.000 |  9945 |    0 | 187646 |    0 |
|  8 | kan_Latn          | Kannada (Latin)   |              9944 |     nan     |    0.000 | 0.000 |     0 |    0 | 187647 | 9944 |
|  9 | tel               | Telugu            |              9916 |       1.000 |    1.000 | 1.000 |  9916 |    0 | 187675 |    0 |
| 10 | tel_Latn          | Telugu (Latin)    |              9914 |     nan     |    0.000 | 0.000 |     0 |    0 | 187677 | 9914 |
| 11 | guj               | Gujarati          |              9913 |       1.000 |    1.000 | 1.000 |  9913 |    1 | 187677 |    0 |
| 12 | guj_Latn          | Gujarati (Latin)  |              9911 |     nan     |    0.000 | 0.000 |     0 |    0 | 187680 | 9911 |
| 13 | tam               | Tamil             |              9902 |       1.000 |    1.000 | 1.000 |  9902 |    0 | 187689 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              9899 |     nan     |    0.000 | 0.000 |     0 |    0 | 187692 | 9899 |
| 15 | ben_Latn          | Bangla (Latin)    |              9882 |     nan     |    0.000 | 0.000 |     0 |    0 | 187709 | 9882 |
| 16 | ben               | Bangla            |              9882 |       1.000 |    0.982 | 0.991 |  9701 |    1 | 187708 |  181 |
| 17 | pan               | Punjabi           |              9758 |       1.000 |    1.000 | 1.000 |  9758 |    2 | 187831 |    0 |
| 18 | pan_Latn          | Punjabi (Latin)   |              9757 |     nan     |    0.000 | 0.000 |     0 |    0 | 187834 | 9757 |
| 19 | urd               | Urdu              |              9541 |       1.000 |    0.836 | 0.911 |  7977 |    2 | 188048 | 1564 |
| 20 | urd_Latn          | Urdu (Latin)      |              9538 |     nan     |    0.000 | 0.000 |     0 |    0 | 188053 | 9538 |