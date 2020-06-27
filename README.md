# trashnet
This is the fastai implementation of [Gary Thung](https://github.com/garythung)'s and [Mindy Yang](http://github.com/yangmindy4)'s final project for [Stanford's CS 229: Machine Learning class](http://cs229.stanford.edu). Original paper is availabe [here](http://cs229.stanford.edu/proj2016/poster/ThungYang-ClassificationOfTrashForRecyclabilityStatus-poster.pdf). The dataset is obtained from the original repo. [Link](https://github.com/garythung/trashnet/blob/master/data/dataset-resized.zip) to the dataset.

## Dataset
(Dataset description copied "as it is" from original repo)

This repository contains the dataset that we collected. The dataset spans six classes: glass, paper, cardboard, plastic, metal, and trash. Currently, the dataset consists of 2527 images:
- 501 glass
- 594 paper
- 403 cardboard
- 482 plastic
- 410 metal
- 137 trash

The pictures were taken by placing the object on a white posterboard and using sunlight and/or room lighting. The pictures have been resized down to 512 x 384, which can be changed in `data/constants.py` (resizing them involves going through step 1 in usage). The devices used were Apple iPhone 7 Plus, Apple iPhone 5S, and Apple iPhone SE.

The size of the original dataset, ~3.5GB, exceeds the git-lfs maximum size so it has been uploaded to Google Drive. If you are planning on using the Python code to preprocess the original dataset, then download `dataset-original.zip` from the link below and place the unzipped folder inside of the `data` folder.

**If you are using the dataset, please give a citation of this repository. The dataset can be downloaded [here](http://drive.google.com/drive/folders/0B3P9oO5A3RvSUW9qTG11Ul83TEE).**

### Model description
Pretrained resnet 50 is trained with the help of fastai library. Model was able to achieve the accuracy of 91.034%(previously 88.5%) with 70/13/17 train/val/test split (as done by original author).
In this approach we first train only a couple of layers of resnet 50 while keeping rest of the weights as it is. Then we unfreeze the whole model and train all layers.
