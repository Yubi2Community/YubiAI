# Document Image Class Detection

## Document vs Non-Documents Classification
* Model to detect if given image is document or not
* We used ~30k document images and ~50k different kinds of images
* Various models used and currently two models are provided
    * `doc-vs-nondoc_Xception_block_12-14`
        * We finetuned Xception model last 3 block
    * `doc-vs-nondoc_vit-b16_layer15`
        * We finetuned vit model last 2 transformer blocks
* Performance of both models was good on validation set.

    | model | Validation Accuracy |
    | ----- | ------------------- | 
    | Xception_12-14 | 99.8% |
    | VIT-b16_layer16 | 99.6% |


## NSFW Image Classification
* Model to detect if given image is document or Safe vs Non-Safe image
* We used >1million images totally with classes `'anime', 'docimage', 'explicit', 'gore_violence', 'non-explicit', 'sexy'`
* Various models used and currently two models are provided
    * `nsfw_detection_ResNet101V2`
        * We finetuned with all layers open for training
    * `nsfw_detection_Xception_block_12-14`
        * We finetuned Xception model last 3 block
    * `nsfw_detection_Xception_block_13-14`
        * We finetuned Xception model last 2 block
    * `nsfw_detection_vit-b16_layer16`
        * We finetuned vit model last 2 transformer blocks
* Performance of all models captured on validation set.

    | model | Validation Accuracy |
    | ----- | ------------------- | 
    | ResNet101V2 | 79% |
    | Xception_block_12-14 | 85% |
    | Xception_block_13-14 | 86% |
    | VIT-b16_layer16 | 83% |


## How to run

```python

from yubiai.vision.document_image_detection.image_classification import DocDetection, NSFWDetection

docimgpath  = "/path/of/an/test/docimage.jpg"
nondocimgpath  = "/path/of/an/test/non-docimage.jpg"

docmodel = DocDetection(model_type="doc-vs-nondoc_Xception_block_12-14", use_gpu=False)
nsfwmodel = NSFWDetection(model_type="nsfw_detection_Xception_block_12-14", use_gpu=False)

docmodel.classify(docimgpath)
### Output : {'document': 100.0, 'nondocument': 0.0}
nsfwmodel.classify(docimgpath)
### Output : {'anime': 0.0, 'docimage': 99.98, 'explicit': 0.0, 'gore_violence': 0.0, 'non-explicit': 0.01, 'sexy': 0.0} 

docmodel.classify(nondocimgpath)
### Output : {'document': 0.0, 'nondocument': 100.0}
nsfwmodel.classify(nondocimgpath)
### Output : {'anime': 0.0, 'docimage': 0.0, 'explicit': 0.06, 'gore_violence': 0.0, 'non-explicit': 62.18, 'sexy': 37.75} 

```