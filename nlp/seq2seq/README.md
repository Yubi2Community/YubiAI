# Fairseq Sequence-2-Sequence Models

## TrueCaser Model for English

* Model to convert given lowercased text to a proper true-cased text
* Trained for only English language
* Used cleaned Wikipedia Dump of ~11Gb and converted into sentences using spacy.
* Training data had .. lowercased wiki sentences as input and original sentences as output.
* Had to create a new SentencePiece Tokenizer for this specific problem. It has 32k bpe tokens.
* Trained on >90 million sentences, two epochs and stopped after perplexity of ~1.15.
* Model used -> `transformer_wmt_en_de_big_t2t` (It has 6 encoders and 6 decoders)
* Pre-requisite (test with following version)
    * `numpy>=1.23.4` (This is required as it was throwing 86 to 80 machine code error.)
    * `torch>=1.13.0`
    * `sentencepiece>=0.1.97`
    * `fairseq=0.12.2`

    ### How to run

    ```python

    from YubiAI.nlp.seq2seq.util import Seq2SeqFairseqWrapper

    seq2seq_model = Seq2SeqFairseqWrapper(use_gpu=False, model_type="TrueCaser_transformer_wmt_en_de_big_t2t")

    text = "national testing agency has issued the indian institute of foreign trade (iift) – mba (international business) 2023 exam city intimation slip."
    seq2seq_model.get_translation(text, to_lower=True, to_char=False)
    ### Output => National Testing Agency has issued the Indian Institute of Foreign Trade (IIFT) – MBA (International Business) 2023 exam city intimation slip.

    ```

    ### Benchmarks
    Benchmarked with 10k wikipedia sentences and 10k news sentences. Used current best [truecaser library](https://pypi.org/project/truecase/). This library uses [NLTK](https://www.nltk.org/index.html) internally and references this [SOTA paper](https://www.cs.cmu.edu/~llita/papers/lita.truecasing-acl2003.pdf). 
    </br> Supposedly, [Grammerly](https://app.grammarly.com/) should be taken for comparison as their plugin seems to work better, also their [paper](https://arxiv.org/pdf/1906.01733.pdf) looks better. But not able to compare it directly without any api.
    </br> Following are BLEU score comparisons - 
    
    | Wiki-dataset  | BLEU score avg | 1-gram | 2-gram | 3-gram | 4-gram |
    | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
    | truecase pypi  | 82.77 | 92.2 | 85.5 | 79.8 | 74.6 |
    | <b>yubiai-truecaser  | <b>97.00 | <b>98.6 | <b>97.5 | <b>96.5 | <b>95.5 |

    | News-dataset  | BLEU score avg | 1-gram | 2-gram | 3-gram | 4-gram |
    | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
    | truecase pypi  | 71.04 | 84.6 | 74.2 | 66.7 | 60.8 |
    | <b>yubiai-truecaser  | <b>89.40 | <b>94.4 | <b>90.5 | <b>87.7 | <b>85.2 |

</br></br>


## Character-2-Text Model for English+Regional Language

* Model to convert given character stream to a proper true-cased text
* Trained for English + top-13 Indian Regional languages
* Used cleaned Wikipedia Dump of ~11Gb + Scrapped ~7Gb regional data.
* Training data had .. lowercased character stream text as input and original sentences as output.
* Had to create a new SentencePiece Tokenizer for this specific problem. It has 48k bpe tokens.
* Trained on >100 million sentences, two epochs and stopped after perplexity of <1.2.
* Model used -> `transformer_wmt_en_de_big_t2t` (It has 6 encoders and 6 decoders)
* Pre-requisite (test with following version)
    * `numpy>=1.23.4` (This is required as it was throwing 86 to 80 machine code error.)
    * `torch>=1.13.0`
    * `sentencepiece>=0.1.97`
    * `fairseq=0.12.2`
* Nothing similar to this model exists so could not benchmark it against any other model.

    ### How to run

    ```python

    from YubiAI.nlp.seq2seq.util import Seq2SeqFairseqWrapper

    seq2seq_model = Seq2SeqFairseqWrapper(use_gpu=False, model_type="character2text_transformer_wmt_en_de_big_t2t")

    text = "y u b i i s b u i l d i n g i n d i a ’ s f i r s t a n d l a r g e s t d e - f a c t o o p e r a t i n g s y s t e m f o r t h e d i s c o v e r y , i n v e s t m e n t , f u l f i l m e n t , a n d c o l l e c t i o n o f a n y d e b t s o l u t i o n ."
    seq2seq_model.get_translation(text, to_lower=True, to_char=True)
    ### Output => Yubi is building India’s first and largest de-facto operating system for the discovery, investment, fulfilment, and collection of any debt solution.

    text = """क ो र ् ट न े घ ो ट ा ल े क े म ा म ल े म े ं ज ा ं च क र र ह ी य ू प ी प ु ल ि स क ी आ र ् थ ि क अ प र ा ध श ा ख ा , ई ड ी , ए स ए फ आ ई ओ क ी ज ा ं च प र अ ं स त ु ष ् ट ी ज त ा ई ।"""
    seq2seq_model.get_translation(text, to_lower=True, to_char=True)
    ### Output => कोर्ट ने घोटाले के कामले में जांच कररही यूपी पुलिस की आर्थिक अपराध शाखा,ईडी,एस एफ आई ओकी जांच पर अंसतुष्टी जताई।

    ```