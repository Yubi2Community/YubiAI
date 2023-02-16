# Classification performance for langdetect on open-subtitles-v2018-100k-per-lang

- Dataset coverage (sentences in supported languages): 508349 (27.60%)
- **Aggregated accuracy: 90.41%**

<h2 id="supported-languages">Considered Languages for Evaluation (27)</h2>

hin (Hindi), ben (Bangla), guj (Gujarati), pan (Punjabi), mal (Malayalam), kan (Kannada), tam (Tamil), tel (Telugu), ori (Odia), mar (Marathi), asm (Assamese), nep (Nepali), urd (Urdu), eng (English), hin_Latn (Hindi (Latin)), ben_Latn (Bangla (Latin)), guj_Latn (Gujarati (Latin)), pan_Latn (Punjabi (Latin)), mal_Latn (Malayalam (Latin)), kan_Latn (Kannada (Latin)), tel_Latn (Telugu (Latin)), tam_Latn (Tamil (Latin)), mar_Latn (Marathi (Latin)), ori_Latn (Odia (Latin)), nep_Latn (Nepali (Latin)), urd_Latn (Urdu (Latin)), asm_Latn (Assamese (Latin))

<h2 id="metrics-per-language">Stats per language</h2>

|    | language_alpha3   | language   |   sentences_count |   precision |   recall |    f1 |    tp |   fp |     tn |    fn |
|---:|:------------------|:-----------|------------------:|------------:|---------:|------:|------:|-----:|-------:|------:|
|  1 | eng               | English    |             99932 |       0.996 |    0.750 | 0.854 | 74954 |  280 | 408137 | 24978 |
|  2 | mal               | Malayalam  |             99331 |       1.000 |    0.983 | 0.991 | 97613 |    0 | 409018 |  1718 |
|  3 | ben               | Bangla     |             98549 |       1.000 |    0.985 | 0.993 | 97120 |    0 | 409800 |  1429 |
|  4 | hin               | Hindi      |             97336 |       1.000 |    0.842 | 0.914 | 81930 |    0 | 411013 | 15406 |
|  5 | urd               | Urdu       |             45315 |       1.000 |    0.907 | 0.951 | 41114 |    0 | 463034 |  4201 |
|  6 | tam               | Tamil      |             38761 |       1.000 |    0.986 | 0.993 | 38232 |    2 | 469586 |   529 |
|  7 | tel               | Telugu     |             29125 |       1.000 |    0.983 | 0.991 | 28617 |    0 | 479224 |   508 |