# Improving Livestock Health with Deep Learning: a benchmark study

This code base contains the code used to pre-process and modeling images taken at 34 poultry farms in Tanzania. We have four classes: healthy, Coccidiosis (`cocci`), Newcastle disease (`ncd`), and Salmonella (`salmo`).

The full published processed annotated dataset can be found on [Zenodo](http://doi.org/10.5281/zenodo.4628934). The dataset of poultry fecal images contains four classes for three main computer vision tasks:

- Object Detection
- Segmentation
- Image Classification

### 1. Data Pre-processing
Data was collected using Open Data Kit ([ODK](https://getodk.org/)) app on Android smartphones and stored on Google drive. Code use to for data pre-processing include:

* [`download_files.py`](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/Codes_Final/download_files.py): used Google Drive Downloader to download fecal images dataset from URLs captured by ODK.
* [`filelist_img.py`](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/Codes_Final/filelist_img.py): used to produce a `.csv` with a list of all files in a given folder. It maintains the original files names of downloaded image files before renaming them.
* [`rename_img.py`](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/Codes_Final/rename_img.py): used to rename files in a given folder in the format `classname.filenumber.extension` e.g. healthy.25.jpg and produces a `.csv` file containing a list of new filename and old filename.

### 2. Modeling
We used a dataset of 1,500 images for modeling:
* Image Classification [baseline model](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/Codes_Final/Poultry_baseline_classification.ipynb) on Keras
  * Classifier for three classes of salmonella, coccidiosis and healthy.
  * Accuracy of 94.12%


* Machine Learning [Application model](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/Codes_Final/ML_App_image_classification.ipynb) for image classification of poultry diseases using TensorFlow Lite Model Maker.
   * Used MobileNet architecture for training
   * Accuracy of 96.8% training and 96.67% on testing
   * MobileNet V1 had same accuracy as MobileNet V2 on test dataset
   * Exported the `model.tflite` file of MobileNet V1 for deployment on Android.

### 3. Deployment
Android Studio 4.1.3 for TensorFlow Lite model deployment:
* Added the `tflite` model to starter [Android app](https://github.com/tensorflow/examples/tree/master/lite/codelabs/flower_classification/android/start)
* Built the project and produced the [APK file](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/img/app-debug.apk) for installation on Android smartphones.
* The final Android Project can be found [here](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/TFLite_PoultryApp).

![inference](https://github.com/ezinne359/AI4D-Poultry-Dataset/blob/main/img/Inference.png)
### References
[Image Classification](https://www.tensorflow.org/tutorials/images/classification)

[TensorFlow Lite Model Maker](https://www.tensorflow.org/lite/guide/model_maker)

[Android Image Classification example](https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android#0)
