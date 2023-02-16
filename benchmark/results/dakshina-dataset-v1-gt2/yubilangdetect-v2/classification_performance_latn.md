# Classification performance for yubilangdetect-v2 on dakshina-dataset-v1-gt2

- Dataset coverage (sentences in supported languages): 180013 (82.92%)
- **Aggregated accuracy: 90.87%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|-------:|-----:|
|  1 | kan               | Kannada           |              9417 |       1.000 |    1.000 | 1.000 | 9417 |    1 | 170595 |    0 |
|  2 | kan_Latn          | Kannada (Latin)   |              9416 |       0.915 |    0.957 | 0.897 | 9011 |  832 | 169765 |  405 |
|  3 | guj               | Gujarati          |              9330 |       1.000 |    1.000 | 1.000 | 9330 |    0 | 170683 |    0 |
|  4 | guj_Latn          | Gujarati (Latin)  |              9328 |       0.809 |    0.910 | 0.778 | 8490 | 2008 | 168677 |  838 |
|  5 | pan               | Punjabi           |              9305 |       1.000 |    1.000 | 1.000 | 9305 |    1 | 170707 |    0 |
|  6 | pan_Latn          | Punjabi (Latin)   |              9305 |       0.911 |    0.785 | 0.810 | 7307 |  718 | 169990 | 1998 |
|  7 | hin               | Hindi             |              9193 |       0.982 |    0.989 | 0.977 | 9095 |  165 | 170655 |   98 |
|  8 | hin_Latn          | Hindi (Latin)     |              9189 |       0.554 |    0.564 | 0.456 | 5179 | 4169 | 166655 | 4010 |
|  9 | ben_Latn          | Bangla (Latin)    |              9139 |       0.949 |    0.930 | 0.917 | 8503 |  454 | 170420 |  636 |
| 10 | ben               | Bangla            |              9137 |       1.000 |    1.000 | 1.000 | 9136 |    1 | 170875 |    1 |
| 11 | mal               | Malayalam         |              9017 |       1.000 |    1.000 | 1.000 | 9017 |    0 | 170996 |    0 |
| 12 | mal_Latn          | Malayalam (Latin) |              9015 |       0.909 |    0.939 | 0.883 | 8465 |  849 | 170149 |  550 |
| 13 | tam               | Tamil             |              8818 |       1.000 |    1.000 | 1.000 | 8818 |    0 | 171195 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              8817 |       0.939 |    0.979 | 0.929 | 8629 |  563 | 170633 |  188 |
| 15 | mar               | Marathi           |              8803 |       0.996 |    0.976 | 0.984 | 8589 |   36 | 171174 |  214 |
| 16 | mar_Latn          | Marathi (Latin)   |              8799 |       0.952 |    0.874 | 0.891 | 7686 |  388 | 170826 | 1113 |
| 17 | urd               | Urdu              |              8529 |       1.000 |    1.000 | 1.000 | 8527 |    3 | 171481 |    2 |
| 18 | urd_Latn          | Urdu (Latin)      |              8493 |       0.866 |    0.317 | 0.448 | 2692 |  415 | 171105 | 5801 |
| 19 | tel_Latn          | Telugu (Latin)    |              8482 |       0.864 |    0.932 | 0.837 | 7901 | 1248 | 170283 |  581 |
| 20 | tel               | Telugu            |              8481 |       0.999 |    1.000 | 0.999 | 8481 |    6 | 171526 |    0 |