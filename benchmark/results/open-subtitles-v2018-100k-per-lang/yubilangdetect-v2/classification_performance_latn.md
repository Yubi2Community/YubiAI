# Classification performance for yubilangdetect-v2 on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 508349 (27.60%)
- **Aggregated accuracy: 95.55%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|------:|-----:|-------:|------:|
|  1 | eng               | English    |             99932 |       0.989 |    0.942 | 0.960 | 94179 | 1004 | 407413 |  5753 |
|  2 | mal               | Malayalam  |             99331 |       1.000 |    0.983 | 0.991 | 97628 |   44 | 408974 |  1703 |
|  3 | ben               | Bangla     |             98549 |       1.000 |    0.972 | 0.986 | 95806 |    1 | 409799 |  2743 |
|  4 | hin               | Hindi      |             97336 |       0.994 |    0.890 | 0.937 | 86668 |  514 | 410499 | 10668 |
|  5 | urd               | Urdu       |             45315 |       1.000 |    0.983 | 0.991 | 44534 |    0 | 463034 |   781 |
|  6 | tam               | Tamil      |             38761 |       1.000 |    0.987 | 0.993 | 38249 |   19 | 469569 |   512 |
|  7 | tel               | Telugu     |             29125 |       0.999 |    0.984 | 0.992 | 28673 |   17 | 479207 |   452 |