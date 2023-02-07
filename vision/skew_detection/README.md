# Document Skew Detection

## Quadrant Detection
* We trained model to detect if skewed angle lies in `Q1` or `Q2` or `Q3` or `Q4`
* Millions of skewed images used to train the model
* `ResNet101v2` was used with some extra layers at the end. Fine-tuned with all layers open.
* Took 3+ days on `g5dn.12xlarge` instance for each run.
* Two models are trained
    * `Quad4Detection_ResNet101V2_0-90`
        * Q1 -> 0-90 degree angles
        * Q2 -> 90-180 degree angles
        * Q3 -> 180-270 degree angles
        * Q4 -> 270-360 degree angles
    * `Quad4Detection_ResNet101V2_45-135`
        * Q1 -> 45-135 degree angles
        * Q2 -> 135-225 degree angles
        * Q3 -> 225-315 degree angles
        * Q4 -> 315-360 & 0-45 degree angles
* Accuracy on validation test was ~96-97% 
* Accuracy improves when we take >5 random patches of original images and take votes
* 23k images test set `classification report`

    | Quadrant | precision | recall | f1-score | support |
    | -------- | --------- | ------ | -------- | ------- |
    | Q1 | 0.99 | 0.97 | 0.98 | 5524 | 
    | Q2  | 0.98 | 0.98 | 0.98 | 5408 | 
    | Q3  | 0.98 | 0.98 | 0.98 | 5459 | 
    | Q4  | 0.97 | 0.99 | 0.98 | 5465 |
    | accuracy | | | 0.98 | 21856 |
    | macro avg | 0.98 | 0.98 | 0.98 | 21856 | 
    | weighted avg | 0.98 | 0.98 | 0.98 | 21856 | 

## Angle Detection
* We trained model to detect if skewed angle lies in `Q1` i.e. return value between 0 and 90 degrees
* Quadrant should corrected before this step.
* Millions of skewed images used to train the model
* `ResNet101v2` was used with some extra layers at the end. Fine-tuned with all layers open.
* Took 3+ days on `g5dn.12xlarge` instance for each run.
* MAE was ~1 degree angle when we stopped the training.
* Two models are trained
    * `SkewDetection_ResNet101V2_0-90` : Detects angle between 0 to 90 
    * `SkewDetection_ResNet101V2_45-135` : Detects angle between -45 to 45
* For better and easier inference `0-90` models for both quad and skew should be run together. 
* Similarly `45-135` models should be run together.
* Our model performance
    * On 23k Set `MAE - 5.35` and `RMSE - 7.47` for our model 
    * Skewness from 0 to 360 degrees converted to 0-90 degrees with `Quadrant Detection` model
* Comparison with [jdeskew model](https://github.com/phamquiluan/jdeskew)
    * `jdeskew` works for skew from -45 to 45 so reduced the testset to ~7.4k images with this restriction
    * Our model works better far away from 0 degree. `jdeskew` works well near 0 degree and worse far from it. Strange behaviours and we hope to explore more.
    * Saying that ... our model works for 0-90 degree and with quadrant detection actually works for 0-360 degrees.

    | model | RMSE | MAE |
    | ----- | ---- | --- | 
    | jdeskew | 23.91 | 16.72 |
    | yubi-skew-detection | 22.16 | 13.31 |

## How to run

```python

from YubiAI.vision.skew_detection.document_skew_detection import YubiDocSkewDetector

skew_detector = YubiDocSkewDetector(qudrant_model="Quad4Detection_ResNet101V2_0-90", 
                                    skew_model="SkewDetection_ResNet101V2_0-90", 
                                    use_gpu=False)
imagepath = "/home/ubuntu/some_image.jpeg"

### To detect the Quadrant
skew_detector.predict_qudrant(imagepath)
# 1/1 [==============================] - 1s 1s/step
# {'detected_quadrant': 'Q4', 'quadrant_prob': 100.0}

### To correct the image quadrant to Q1
skew_detector.rotate_to_first_qudrant(imagepath, 'Q4', saveimage=True)
# array([[[192,  27,  34],
#         [192,  27,  34],
#         [187,  29,  34],
#         ...,
#         [138,  84,  52],
#         [150,  96,  64],
#         [158, 104,  72]]], dtype=uint8)

### Detect the angle/skewness of given image
skew_detector.predict_angle(imagepath)
# 1/1 [==============================] - 1s 1s/step
# {'average_angle': 84.52632, 'angle_preds': [84.57919, 84.667244, 84.79881, 84.62079, 84.37254, 84.31932, 84.61099, 83.88075, 84.6366, 84.77704]}

### Correct the angle of given image
skew_detector.rotate_to_correct_angle(imagepath, 84.52632, saveimage=True)
# array([[[255, 255, 255],
#         [255, 255, 255],
#         [255, 255, 255],
#         ...,
#         [255, 255, 255],
#         [255, 255, 255],
#         [255, 255, 255]]], dtype=uint8)


### Sample Code Given as end-2-end solution
skew_detector.correct_image_skew_sample_code(imagepath)

```