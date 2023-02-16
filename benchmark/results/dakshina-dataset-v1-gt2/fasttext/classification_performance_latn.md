# Classification performance for fasttext on dakshina-dataset-v1-gt2

- Dataset coverage (sentences in supported languages): 180013 (82.92%)
- **Aggregated accuracy: 49.66%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language          |   sentences_count |   precision |   recall |    f1 |   tp |   fp |     tn |   fn |
|---:|:------------------|:------------------|------------------:|------------:|---------:|------:|-----:|-----:|-------:|-----:|
|  1 | kan               | Kannada           |              9417 |       0.989 |    1.000 | 0.989 | 9417 |  105 | 170491 |    0 |
|  2 | kan_Latn          | Kannada (Latin)   |              9416 |     nan     |    0.000 | 0.000 |    0 |    0 | 170597 | 9416 |
|  3 | guj               | Gujarati          |              9330 |       1.000 |    1.000 | 1.000 | 9330 |    2 | 170681 |    0 |
|  4 | guj_Latn          | Gujarati (Latin)  |              9328 |     nan     |    0.000 | 0.000 |    0 |    0 | 170685 | 9328 |
|  5 | pan               | Punjabi           |              9305 |       1.000 |    1.000 | 1.000 | 9305 |    1 | 170707 |    0 |
|  6 | pan_Latn          | Punjabi (Latin)   |              9305 |     nan     |    0.000 | 0.000 |    0 |    0 | 170708 | 9305 |
|  7 | hin               | Hindi             |              9193 |       0.974 |    0.995 | 0.972 | 9151 |  244 | 170576 |   42 |
|  8 | hin_Latn          | Hindi (Latin)     |              9189 |     nan     |    0.000 | 0.000 |    0 |    0 | 170824 | 9189 |
|  9 | ben_Latn          | Bangla (Latin)    |              9139 |     nan     |    0.000 | 0.000 |    0 |    0 | 170874 | 9139 |
| 10 | ben               | Bangla            |              9137 |       0.993 |    1.000 | 0.993 | 9136 |   65 | 170811 |    1 |
| 11 | mal               | Malayalam         |              9017 |       0.996 |    1.000 | 0.996 | 9017 |   36 | 170960 |    0 |
| 12 | mal_Latn          | Malayalam (Latin) |              9015 |     nan     |    0.000 | 0.000 |    0 |    0 | 170998 | 9015 |
| 13 | tam               | Tamil             |              8818 |       1.000 |    1.000 | 1.000 | 8818 |    3 | 171192 |    0 |
| 14 | tam_Latn          | Tamil (Latin)     |              8817 |     nan     |    0.000 | 0.000 |    0 |    0 | 171196 | 8817 |
| 15 | mar               | Marathi           |              8803 |       0.998 |    0.970 | 0.983 | 8539 |   20 | 171190 |  264 |
| 16 | mar_Latn          | Marathi (Latin)   |              8799 |     nan     |    0.000 | 0.000 |    0 |    0 | 171214 | 8799 |
| 17 | urd               | Urdu              |              8529 |       0.990 |    0.962 | 0.970 | 8203 |   87 | 171397 |  326 |
| 18 | urd_Latn          | Urdu (Latin)      |              8493 |     nan     |    0.000 | 0.000 |    0 |    0 | 171520 | 8493 |
| 19 | tel_Latn          | Telugu (Latin)    |              8482 |     nan     |    0.000 | 0.000 |    0 |    0 | 171531 | 8482 |
| 20 | tel               | Telugu            |              8481 |       0.999 |    1.000 | 0.999 | 8481 |   10 | 171522 |    0 |