# Multiclass-Skin-Disease-Classification
A Convolution Neural Network Model that can classify whether a person is having Acne and Rosacea Photos, Eczema Photos, Melanoma Skin Cancer Nevi and Moles, Psoriasis pictures Lichen Planus and related diseases, Chickenpox, Measles, Monkeypox or the person is normal with the help of image.

Training data is taken from kaggle:
https://www.kaggle.com/datasets/dipuiucse/monkeypoxskinimagedataset
https://www.kaggle.com/datasets/shubhamgoel27/dermnet

## Portraying the Use of Transfer Learning
Two transfer learning models have been taken for implementation
1) A model is created using DENSENET201 transfer learning, allowing it to easily predict any of the 8 skin disease cases. This project showcases how model highlights room for improvement in DenseNet201.
2) An improved model is created using VGG16 transfer learning, allowing it to easily predict any of the 4 skin disease cases. This project showcases the effectiveness of transfer learning in enhancing classification accuracy.

### Base and Transfer Learning Models
This repository demonstrates the contrast between three models:

1. **Base Model:** A Convolution Neural Network model developed without transfer learning.
2. **Densenet201 Model:** Utilizing VGG16 transfer learning for reducing time for running epochs and make model fit for prediction
3. **Enhanced VGG16 Model:** Utilizing VGG16 transfer learning for improved classification accuracy.

The enhanced model shows the advantages of leveraging pre-trained models like VGG16 to achieve better results in complex classification tasks.

## Results
### Without transfer Learning
![1 1](https://github.com/AkshatJain20092002/Skin-Disease-Classification/assets/106154057/065d3518-2e40-4dee-b5ce-5bd7fc70461b)
![2 2](https://github.com/AkshatJain20092002/Skin-Disease-Classification/assets/106154057/c77f3700-24f9-4b36-923e-5c0238957630)

### With DENSETNET201
![image](https://github.com/AkshatJain20092002/Skin-Disease-Classification/assets/106154057/d16a5ace-fe7a-420a-b553-98b9d123111b)
![image](https://github.com/AkshatJain20092002/Skin-Disease-Classification/assets/106154057/4ee0ca9d-796d-4a5d-8596-72a0c943e5eb)

### With VGG16
![1](https://github.com/AkshatJain20092002/Skin-Disease-Classification/assets/106154057/36da59c0-abd8-49c5-a628-37d055da5938)
![2](https://github.com/AkshatJain20092002/Skin-Disease-Classification/assets/106154057/7c50e56a-4352-4221-9b7d-0e55062a7e39)

## Web Deployment
Use the Flask web app for the deployment of classification of Skin Diseases using transfer learning models - VGG16 and DenseNet201
