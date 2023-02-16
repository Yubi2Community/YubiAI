# Classification performance for gcld3 on dakshina-dataset-v1-gt2

- Dataset coverage (sentences in supported languages): 180013 (82.92%)
- **Aggregated accuracy: 53.59%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |    fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|------:|-------:|-----:|
|  1 | kan               | Kannada           |              9417 |       1.000 |    0.997 | 0.999 | 9392 |     0 | 170596 |   25 |
|  2 | kan_Latn          | Kannada (Latin)   |              9416 |     nan     |    0.000 | 0.000 |    0 |     0 | 170597 | 9416 |
|  3 | guj               | Gujarati          |              9330 |       1.000 |    0.999 | 0.999 | 9319 |     0 | 170683 |   11 |
|  4 | guj_Latn          | Gujarati (Latin)  |              9328 |     nan     |    0.000 | 0.000 |    0 |     0 | 170685 | 9328 |
|  5 | pan               | Punjabi           |              9305 |       1.000 |    0.999 | 0.999 | 9295 |     0 | 170708 |   10 |
|  6 | pan_Latn          | Punjabi (Latin)   |              9305 |     nan     |    0.000 | 0.000 |    0 |     0 | 170708 | 9305 |
|  7 | hin               | Hindi             |              9193 |       0.964 |    0.950 | 0.940 | 8729 |   322 | 170498 |  464 |
|  8 | hin_Latn          | Hindi (Latin)     |              9189 |       0.312 |    0.867 | 0.305 | 7970 | 17563 | 153261 | 1219 |
|  9 | ben_Latn          | Bangla (Latin)    |              9139 |     nan     |    0.000 | 0.000 |    0 |     0 | 170874 | 9139 |
| 10 | ben               | Bangla            |              9137 |       1.000 |    1.000 | 1.000 | 9133 |     0 | 170876 |    4 |
| 11 | mal               | Malayalam         |              9017 |       1.000 |    0.999 | 1.000 | 9012 |     0 | 170996 |    5 |
| 12 | mal_Latn          | Malayalam (Latin) |              9015 |     nan     |    0.000 | 0.000 |    0 |     0 | 170998 | 9015 |
| 13 | tam               | Tamil             |              8818 |       1.000 |    0.998 | 0.999 | 8798 |     0 | 171195 |   20 |
| 14 | tam_Latn          | Tamil (Latin)     |              8817 |     nan     |    0.000 | 0.000 |    0 |     0 | 171196 | 8817 |
| 15 | mar               | Marathi           |              8803 |       0.968 |    0.949 | 0.943 | 8354 |   278 | 170932 |  449 |
| 16 | mar_Latn          | Marathi (Latin)   |              8799 |     nan     |    0.000 | 0.000 |    0 |     0 | 171214 | 8799 |
| 17 | urd               | Urdu              |              8529 |       0.999 |    0.940 | 0.969 | 8019 |     5 | 171479 |  510 |
| 18 | urd_Latn          | Urdu (Latin)      |              8493 |     nan     |    0.000 | 0.000 |    0 |     0 | 171520 | 8493 |
| 19 | tel_Latn          | Telugu (Latin)    |              8482 |     nan     |    0.000 | 0.000 |    0 |     0 | 171531 | 8482 |
| 20 | tel               | Telugu            |              8481 |       1.000 |    0.996 | 0.998 | 8443 |     0 | 171532 |   38 |