# Classification performance for gcld3 on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 508349 (27.60%)
- **Aggregated accuracy: 85.32%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|------:|-----:|-------:|------:|
|  1 | eng               | English    |             99932 |       0.997 |    0.689 | 0.814 | 68859 |  188 | 408229 | 31073 |
|  2 | mal               | Malayalam  |             99331 |       1.000 |    0.964 | 0.982 | 95802 |    0 | 409018 |  3529 |
|  3 | ben               | Bangla     |             98549 |       1.000 |    0.969 | 0.984 | 95534 |    0 | 409800 |  3015 |
|  4 | hin               | Hindi      |             97336 |       0.986 |    0.753 | 0.849 | 73314 | 1011 | 410002 | 24022 |
|  5 | urd               | Urdu       |             45315 |       0.994 |    0.786 | 0.876 | 35632 |  198 | 462836 |  9683 |
|  6 | tam               | Tamil      |             38761 |       1.000 |    0.962 | 0.981 | 37296 |    2 | 469586 |  1465 |
|  7 | tel               | Telugu     |             29125 |       1.000 |    0.937 | 0.967 | 27287 |    0 | 479224 |  1838 |