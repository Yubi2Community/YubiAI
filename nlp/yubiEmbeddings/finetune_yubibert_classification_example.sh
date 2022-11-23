###
### Author : Swapnil Ashok Jadhav (github:swapaj)
### Created Date : 28th Oct. 2022
###

#### Need at-least 1 gpu to fine-tune faster.
#### Python >=3.7 and nvidia-cuda-drivers + pytorch >= 1.8 installed 
#### (using aws deep learning ami is better)
#### Copy train.txt, train.label and valid.txt, valid.label to the same folder
####     ".txt" file contains text per line .. lowercased, no new-line characters
####     ".label" file contains label per line .. no whitespace

##########################################
#### Install required python packages ####
##########################################
pip install "sentencepiece>=0.1.97" "fairseq==0.12.2"

###########################################
#### Get files from yubibert model zip ####
###########################################
wget http://54.151.93.61:8989/yubi_ds_capability/models/yubibert_e4_micro.zip .
unzip yubibert_e4_micro.zip
cp yubibert_e4_micro/sentencepiece* .
cp yubibert_e4_micro/bin_data/dict.txt .
cp yubibert_e4_micro/checkpoint_best.pt .
mv checkpoint_best.pt og_yubibert_e4_micro.pt
rm -rf yubibert_e4_micro*

##############################################
#### Make foldr for raw data and binaries ####
##############################################
mkdir raw_data
mkdir bin_data
cp train.label raw_data/
cp valid.label raw_data/

##################################################
#### Install sentencepiece command line tools ####
##################################################
git clone https://github.com/google/sentencepiece.git 
cd sentencepiece
mkdir build
cd build
cmake ..
make -j $(nproc)
sudo make install
sudo ldconfig -v

##########################################################################
#### Convert input text into tokenised text using sentencepiece model ####
##########################################################################
spm_encode --model=sentencepiece.bpe.model --output_format=piece < train.txt > raw_data/train.txt.bpe
spm_encode --model=sentencepiece.bpe.model --output_format=piece < valid.txt > raw_data/valid.txt.bpe

###########################################
#### Create fairseq preprocessed files ####
###########################################
fairseq-preprocess --only-source --trainpref raw_data/train.label --validpref raw_data/valid.label --destdir bin_data/label/ --workers 4
fairseq-preprocess --only-source --trainpref raw_data/train.txt.bpe --validpref raw_data/valid.txt.bpe --destdir bin_data/input0 --workers 4 --srcdict dict.txt

###############################################################
#### Set env variables (change according to your settings) ####
###############################################################
TOTAL_NUM_UPDATES=100000
WARMUP_UPDATES=1000
LR=1e-05
HEAD_NAME="clf_head_name" ## Classification head name, give some uniq name. To be used in code later.
NUM_CLASSES=2 ## No of classes 
MAX_SENTENCES=8
ROBERTA_PATH=og_yubibert_e4_micro.pt

########################################################################
#### Finetune yubibert_e4_micro (change according to your settings) ####
########################################################################
CUDA_VISIBLE_DEVICES=0 fairseq-train ./bin_data/ --restore-file $ROBERTA_PATH \ 
--max-positions 512 --max-sentences $MAX_SENTENCES  --max-tokens 16384 \ 
--task sentence_prediction --reset-optimizer --reset-dataloader --reset-meters \ 
--required-batch-size-multiple 1 --init-token 0 --separator-token 2 \ 
--encoder-layers 4 --encoder-embed-dim 512 --encoder-ffn-embed-dim 2048 \ 
--encoder-attention-heads 16 --arch roberta_base --criterion sentence_prediction \ 
--classification-head-name $HEAD_NAME --num-classes $NUM_CLASSES --dropout 0.1 \ 
--attention-dropout 0.1 --weight-decay 0.1 --optimizer adam \ 
--adam-betas "(0.9, 0.98)" --adam-eps 1e-06 --clip-norm 0.0 --lr-scheduler \ 
polynomial_decay --lr $LR --total-num-update $TOTAL_NUM_UPDATES --warmup-updates \ 
$WARMUP_UPDATES --fp16 --fp16-init-scale 4 --threshold-loss-scale 1 \ 
--fp16-scale-window 128 --max-epoch 8 --best-checkpoint-metric accuracy \ 
--maximize-best-checkpoint-metric --find-unused-parameters  --update-freq 2 \ 
--skip-invalid-size-inputs-valid-test

########################################################################
#### Finetune yubibert_e8_small (change according to your settings) ####
########################################################################
CUDA_VISIBLE_DEVICES=0 fairseq-train ./bin_data/ --restore-file $ROBERTA_PATH \ 
--max-positions 512 --max-sentences $MAX_SENTENCES  --max-tokens 16384 \ 
--task sentence_prediction --reset-optimizer --reset-dataloader --reset-meters \ 
--required-batch-size-multiple 1 --init-token 0 --separator-token 2 \ 
--encoder-layers 8 --arch roberta_base --criterion sentence_prediction \ 
--classification-head-name $HEAD_NAME --num-classes $NUM_CLASSES --dropout 0.1 \ 
--attention-dropout 0.1 --weight-decay 0.1 --optimizer adam \ 
--adam-betas "(0.9, 0.98)" --adam-eps 1e-06 --clip-norm 0.0 --lr-scheduler \ 
polynomial_decay --lr $LR --total-num-update $TOTAL_NUM_UPDATES --warmup-updates \ 
$WARMUP_UPDATES --fp16 --fp16-init-scale 4 --threshold-loss-scale 1 \ 
--fp16-scale-window 128 --max-epoch 8 --best-checkpoint-metric accuracy \ 
--maximize-best-checkpoint-metric --find-unused-parameters  --update-freq 2 \ 
--skip-invalid-size-inputs-valid-test

#######################################################
#### Create final output folder to be used in code ####
#######################################################
mkdir finetuned_model_files
mv sentencepiece* finetuned_model_files/
mv checkpoints/checkpoint_best.pt finetuned_model_files/
mv bin_data finetuned_model_files/ 
rm -f finetuned_model_files/bin_data/*/train.*