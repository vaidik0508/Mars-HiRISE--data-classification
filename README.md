# Mars orbital image (HiRISE) data classification using Deep Learning

Check out [live demo](https://mars-data-classifier.herokuapp.com/)

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

## Download data 

#### data
![data](https://github.com/vaidik0508/Mars-HiRISE--data-classification/blob/main/model/images.jpg)
download raw data : [raw data](https://zenodo.org/record/2538136#.YookYqhBy3A) \
download my cleaned data : [data](https://drive.google.com/file/d/1VZNjIRG3fzmMfpm0kgf3IOSt0QxEn-ty/view?usp=sharing)

## Training History
Gpraphs of SparseCategoricalCrossentropyloss and SparseCategoricalAccuracy for 50 epochs Training
![Training](https://github.com/vaidik0508/Mars-HiRISE--data-classification/blob/main/model/history.jpg)

