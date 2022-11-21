# Mars orbital image (HiRISE) data classification using Deep Learning

Check out [live demo](https://huggingface.co/spaces/vaidik0508/mars-orbitaldata-classification)

### Fine Tuned ResNet50V2 with Imagenet weights to Mars Orbital (HiRISE) Image data
## Classification example
![Prediction](https://github.com/vaidik0508/Mars-HiRISE--data-classification/blob/main/model/pred.jpg)
In this project, I have done classification of data consists of 6 classes. As below:

Class id  |  Class Name
------- | -------
0  |  Other
1  |  Crater
2  |  Dark Dune
3  |  Slope Dtreak
4  |  Bright Dune
5  |  Swiss Cheese

## About Data
### Mars orbital image (HiRISE) labeled data set version 3
Authors: Kiri L. Wagstaff, Steven Lu, Gary Doran, Lukas Mandrake\
Contact: you.lu@jpl.nasa.gov

This data set contains a total of 73,031 landmarks. 10,433 landmarks were detected and extracted from 180 HiRISE browse images, and 62,598 landmarks were augmented from 10,433 original landmarks. For each original landmark, we cropped a square bounding box that includes the full extent of the landmark plus a 30-pixel margin to left, right, top and bottom. Each cropped landmark was resized to 227x227 pixels, and then was augmented to generate 6 additional landmarks using the following methods:

#### data sample
![data](https://github.com/vaidik0508/Mars-HiRISE--data-classification/blob/main/model/images.jpg)
download raw data : [raw data](https://zenodo.org/record/2538136#.YookYqhBy3A) \
download my cleaned and preprocessed data : [data](https://drive.google.com/file/d/1VZNjIRG3fzmMfpm0kgf3IOSt0QxEn-ty/view?usp=sharing)

## Training History
Gpraphs of SparseCategoricalCrossentropyloss and SparseCategoricalAccuracy for 50 epochs Training
![Training](https://github.com/vaidik0508/Mars-HiRISE--data-classification/blob/main/model/history.jpg)

Attained Training Accuracy : 1 and Validation Accuracy 0.9928
