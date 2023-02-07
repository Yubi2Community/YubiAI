###
### Author : Swapnil Ashok Jadhav (github:swapaj)
### Created Date : 28th Oct. 2022
###

from fairseq.models.roberta import RobertaModel
import numpy as np
import re

model = RobertaModel.from_pretrained("/path/to/dir/finetuned_model_files", 
                                     checkpoint_file="checkpoint_best.pt", 
                                     data_name_or_path="./bin_data", 
                                     bpe="sentencepiece")
model.eval()
### If gpu is available uncomment below line
### model.cuda() 

label_fn = lambda label: model.task.label_dictionary.string([label + model.task.label_dictionary.nspecial])

def get_results(input_text, clf_header_name="clf_head_name"):
    """
    Generic classfication function .. which returns classes with scores. 
    Higher the score is better.
    """
    input_text = re.sub("\s+", " ", input_text)
    input_text = input_text.lower().strip()
    tokens = model.encode(input_text)
    outprob = model.predict(clf_header_name, tokens[:510]).tolist()[0]
    min_prob = np.min(outprob)
    outprob_norm = [x-min_prob for x in outprob]
    sum_prob = np.sum(outprob_norm)
    outprob_norm = [x*1.0/sum_prob for x in outprob_norm]
    outclass = [label_fn(i) for i in range(len(outprob))]

    outmap_norm = dict(zip(outclass, outprob_norm))
    outmap_norm = {k: v for k, v in sorted(outmap_norm.items(), key=lambda item: item[1], reverse=True)}
    outmap_og = dict(zip(outclass, outprob))
    outmap_og = {k: v for k, v in sorted(outmap_og.items(), key=lambda item: item[1], reverse=True)}
    
    return outmap_norm, outmap_og