# Classification performance for fasttext on dakshina-dataset-v1

- Dataset coverage (sentences in supported languages): 197591 (83.62%)
- **Aggregated accuracy: 49.02%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|-------:|-----:|
|  1 | mal               | Malayalam         |             10000 |       0.995 |    1.000 | 0.994 | 9997 |   54 | 187537 |    3 |
|  2 | mar               | Marathi           |             10000 |       0.991 |    0.909 | 0.944 | 9092 |   82 | 187509 |  908 |
|  3 | mar_Latn          | Marathi (Latin)   |              9998 |     nan     |    0.000 | 0.000 |    0 |    0 | 187593 | 9998 |
|  4 | mal_Latn          | Malayalam (Latin) |              9997 |     nan     |    0.000 | 0.000 |    0 |    0 | 187594 | 9997 |
|  5 | hin               | Hindi             |              9949 |       0.927 |    0.984 | 0.920 | 9786 |  766 | 186876 |  163 |
|  6 | hin_Latn          | Hindi (Latin)     |              9945 |     nan     |    0.000 | 0.000 |    0 |    0 | 187646 | 9945 |
|  7 | kan               | Kannada           |              9945 |       0.988 |    1.000 | 0.988 | 9944 |  118 | 187528 |    1 |
|  8 | kan_Latn          | Kannada (Latin)   |              9944 |     nan     |    0.000 | 0.000 |    0 |    0 | 187647 | 9944 |
|  9 | tel               | Telugu            |              9916 |       0.999 |    1.000 | 0.999 | 9915 |   11 | 187664 |    1 |
| 10 | tel_Latn          | Telugu (Latin)    |              9914 |     nan     |    0.000 | 0.000 |    0 |    0 | 187677 | 9914 |
| 11 | guj               | Gujarati          |              9913 |       1.000 |    0.999 | 1.000 | 9908 |    2 | 187676 |    5 |
| 12 | guj_Latn          | Gujarati (Latin)  |              9911 |     nan     |    0.000 | 0.000 |    0 |    0 | 187680 | 9911 |
| 13 | tam               | Tamil             |              9902 |       0.999 |    1.000 | 0.999 | 9902 |    8 | 187681 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              9899 |     nan     |    0.000 | 0.000 |    0 |    0 | 187692 | 9899 |
| 15 | ben_Latn          | Bangla (Latin)    |              9882 |     nan     |    0.000 | 0.000 |    0 |    0 | 187709 | 9882 |
| 16 | ben               | Bangla            |              9882 |       0.992 |    0.997 | 0.991 | 9854 |   76 | 187633 |   28 |
| 17 | pan               | Punjabi           |              9758 |       1.000 |    1.000 | 1.000 | 9755 |    3 | 187830 |    3 |
| 18 | pan_Latn          | Punjabi (Latin)   |              9757 |     nan     |    0.000 | 0.000 |    0 |    0 | 187834 | 9757 |
| 19 | urd               | Urdu              |              9541 |       0.988 |    0.912 | 0.943 | 8704 |  105 | 187945 |  837 |
| 20 | urd_Latn          | Urdu (Latin)      |              9538 |     nan     |    0.000 | 0.000 |    0 |    0 | 188053 | 9538 |