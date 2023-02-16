# Classification performance for pycld2 on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 508349 (27.60%)
- **Aggregated accuracy: 82.45%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|------:|-----:|-------:|------:|
|  1 | eng               | English    |             99932 |       0.999 |    0.745 | 0.853 | 74428 |   81 | 408336 | 25504 |
|  2 | mal               | Malayalam  |             99331 |       1.000 |    0.983 | 0.991 | 97644 |    0 | 409018 |  1687 |
|  3 | ben               | Bangla     |             98549 |       1.000 |    0.648 | 0.786 | 63868 |    0 | 409800 | 34681 |
|  4 | hin               | Hindi      |             97336 |       1.000 |    0.870 | 0.930 | 84683 |    0 | 411013 | 12653 |
|  5 | urd               | Urdu       |             45315 |       1.000 |    0.695 | 0.820 | 31508 |    0 | 463034 | 13807 |
|  6 | tam               | Tamil      |             38761 |       1.000 |    0.988 | 0.994 | 38290 |    2 | 469586 |   471 |
|  7 | tel               | Telugu     |             29125 |       1.000 |    0.986 | 0.993 | 28703 |    0 | 479224 |   422 |