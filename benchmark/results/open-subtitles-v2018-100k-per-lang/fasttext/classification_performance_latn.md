# Classification performance for fasttext on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 508349 (27.60%)
- **Aggregated accuracy: 92.82%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|------:|-----:|-------:|------:|
|  1 | eng               | English    |             99932 |       0.973 |    0.939 | 0.944 | 93868 | 2582 | 405835 |  6064 |
|  2 | mal               | Malayalam  |             99331 |       1.000 |    0.974 | 0.987 | 96736 |   15 | 409003 |  2595 |
|  3 | ben               | Bangla     |             98549 |       1.000 |    0.961 | 0.980 | 94669 |   35 | 409765 |  3880 |
|  4 | hin               | Hindi      |             97336 |       0.999 |    0.872 | 0.931 | 84916 |   84 | 410929 | 12420 |
|  5 | urd               | Urdu       |             45315 |       1.000 |    0.782 | 0.877 | 35420 |    4 | 463030 |  9895 |
|  6 | tam               | Tamil      |             38761 |       0.998 |    0.978 | 0.987 | 37916 |   60 | 469528 |   845 |
|  7 | tel               | Telugu     |             29125 |       0.999 |    0.972 | 0.985 | 28322 |   41 | 479183 |   803 |