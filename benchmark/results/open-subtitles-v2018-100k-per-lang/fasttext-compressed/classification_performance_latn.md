# Classification performance for fasttext-compressed on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 508349 (27.60%)
- **Aggregated accuracy: 91.23%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|------:|-----:|-------:|------:|
|  1 | eng               | English    |             99932 |       0.923 |    0.931 | 0.892 | 92988 | 7795 | 400622 |  6944 |
|  2 | mal               | Malayalam  |             99331 |       1.000 |    0.970 | 0.985 | 96364 |    3 | 409015 |  2967 |
|  3 | ben               | Bangla     |             98549 |       0.999 |    0.952 | 0.975 | 93789 |   50 | 409750 |  4760 |
|  4 | hin               | Hindi      |             97336 |       1.000 |    0.819 | 0.900 | 79701 |   29 | 410984 | 17635 |
|  5 | urd               | Urdu       |             45315 |       1.000 |    0.770 | 0.870 | 34908 |    8 | 463026 | 10407 |
|  6 | tam               | Tamil      |             38761 |       0.999 |    0.976 | 0.987 | 37847 |   24 | 469564 |   914 |
|  7 | tel               | Telugu     |             29125 |       1.000 |    0.968 | 0.983 | 28186 |   14 | 479210 |   939 |