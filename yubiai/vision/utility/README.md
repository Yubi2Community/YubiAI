# Vision Utility Functions

## Preprocessing
* Added functions which are used very repetetively in image preprocessing with lot of custom controls will be there in this module
for example - 
    * image rotation
    * image flip
    * image resize
    * image random crop
* This will be a single wrapper for all the preprocessing functions

## Example code

Output will be numpy array .. which can be loaded to see the image.

```python

from yubiai.vision.utility.preprocess import image_preprocessing

preprocessing_object = image_preprocessing()
image_path = "/home/ubuntu/some_image.jpeg"

output_image = preprocessing_object.preprocess( image_path=image_path,
                                                random_crop=False,
                                                resize_image=False,
                                                flip_image=False,
                                                rotate_image = False,
                                                print_white_pix_precent = False,
                                                flip_horizontal=False,
                                                flip_vertical=False,
                                                resize_image_height=256,
                                                resize_image_width=256,
                                                rotate_skew = 0,
                                                rotate_random = False,
                                                rotate_reshape = True,
                                                cropped_image_height=256,
                                                cropped_image_width=256,
                                                random_crop_white_percent = 98,
                                                random_crop_white_increment = False)

```

## Image Generator

Added functions which are used very repetetively in Generating ramdom images with lot of custom controls will be there in this module
for example  - 
* multiple image rotate
* multiple random crops

* This will be a single wrapper for all the image generator functions

## Example code

Output will be a generator .. which can be iterated to load the image and information on the image.


```python

from yubiai.vision.utility.preprocess import image_preprocessing

preprocessing_object = image_preprocessing()

image_path = "/home/ubuntu/some_image.jpeg"

output_image_gen = preprocessing_object.image_generator(image_path=image_path,
                                                        cropped_image_height=256,
                                                        cropped_image_width=256,   
                                                        random_crop_white_percent = 70,
                                                        random_crop_white_increment = True,
                                                        rotate_random = False,
                                                        multiple_rotated_images = False,
                                                        multiple_random_crops = True,
                                                        rotate_reshape = True,
                                                        n_random = 30,
                                                        n_rotated = 10,
                                                        rotate_skew = 30,        
                                                        seed = 5)
for i in range(10):
    img, img_info = next(output_image_gen)
    print(img_info)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

```
