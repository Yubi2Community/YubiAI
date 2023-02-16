# Classification performance for fasttext-compressed on dakshina-dataset-v1

- Dataset coverage (sentences in supported languages): 197591 (83.62%)
- **Aggregated accuracy: 48.58%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|-------:|-----:|
|  1 | mal               | Malayalam         |             10000 |       0.998 |    0.999 | 0.998 | 9991 |   17 | 187574 |    9 |
|  2 | mar               | Marathi           |             10000 |       0.983 |    0.876 | 0.919 | 8758 |  154 | 187437 | 1242 |
|  3 | mar_Latn          | Marathi (Latin)   |              9998 |     nan     |    0.000 | 0.000 |    0 |    0 | 187593 | 9998 |
|  4 | mal_Latn          | Malayalam (Latin) |              9997 |     nan     |    0.000 | 0.000 |    0 |    0 | 187594 | 9997 |
|  5 | hin               | Hindi             |              9949 |       0.894 |    0.978 | 0.885 | 9729 | 1158 | 186484 |  220 |
|  6 | hin_Latn          | Hindi (Latin)     |              9945 |     nan     |    0.000 | 0.000 |    0 |    0 | 187646 | 9945 |
|  7 | kan               | Kannada           |              9945 |       0.999 |    1.000 | 0.999 | 9943 |    9 | 187637 |    2 |
|  8 | kan_Latn          | Kannada (Latin)   |              9944 |     nan     |    0.000 | 0.000 |    0 |    0 | 187647 | 9944 |
|  9 | tel               | Telugu            |              9916 |       1.000 |    0.999 | 1.000 | 9910 |    0 | 187675 |    6 |
| 10 | tel_Latn          | Telugu (Latin)    |              9914 |     nan     |    0.000 | 0.000 |    0 |    0 | 187677 | 9914 |
| 11 | guj               | Gujarati          |              9913 |       1.000 |    0.999 | 0.999 | 9903 |    0 | 187678 |   10 |
| 12 | guj_Latn          | Gujarati (Latin)  |              9911 |     nan     |    0.000 | 0.000 |    0 |    0 | 187680 | 9911 |
| 13 | tam               | Tamil             |              9902 |       1.000 |    1.000 | 1.000 | 9902 |    3 | 187686 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              9899 |     nan     |    0.000 | 0.000 |    0 |    0 | 187692 | 9899 |
| 15 | ben_Latn          | Bangla (Latin)    |              9882 |     nan     |    0.000 | 0.000 |    0 |    0 | 187709 | 9882 |
| 16 | ben               | Bangla            |              9882 |       0.999 |    0.995 | 0.996 | 9832 |   13 | 187696 |   50 |
| 17 | pan               | Punjabi           |              9758 |       1.000 |    0.999 | 1.000 | 9752 |    1 | 187832 |    6 |
| 18 | pan_Latn          | Punjabi (Latin)   |              9757 |     nan     |    0.000 | 0.000 |    0 |    0 | 187834 | 9757 |
| 19 | urd               | Urdu              |              9541 |       0.991 |    0.867 | 0.921 | 8274 |   73 | 187977 | 1267 |
| 20 | urd_Latn          | Urdu (Latin)      |              9538 |     nan     |    0.000 | 0.000 |    0 |    0 | 188053 | 9538 |