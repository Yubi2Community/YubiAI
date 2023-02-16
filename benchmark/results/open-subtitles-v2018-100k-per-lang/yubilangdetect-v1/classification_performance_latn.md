# Classification performance for yubilangdetect-v1 on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 508349 (27.60%)
- **Aggregated accuracy: 95.29%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|------:|-----:|-------:|------:|
|  1 | eng               | English    |             99932 |       0.983 |    0.950 | 0.958 | 94971 | 1666 | 406751 |  4961 |
|  2 | mal               | Malayalam  |             99331 |       0.999 |    0.980 | 0.988 | 97337 |  146 | 408872 |  1994 |
|  3 | ben               | Bangla     |             98549 |       0.999 |    0.957 | 0.977 | 94339 |   86 | 409714 |  4210 |
|  4 | hin               | Hindi      |             97336 |       0.999 |    0.889 | 0.941 | 86512 |   59 | 410954 | 10824 |
|  5 | urd               | Urdu       |             45315 |       1.000 |    0.979 | 0.989 | 44364 |    2 | 463032 |   951 |
|  6 | tam               | Tamil      |             38761 |       0.999 |    0.987 | 0.992 | 38249 |   40 | 469548 |   512 |
|  7 | tel               | Telugu     |             29125 |       0.992 |    0.983 | 0.984 | 28641 |  221 | 479003 |   484 |