# coconutdiseaseProject

Discription about the project


Currently, coconut disease detection systems are not very effective as they use traditional detection techniques which are less effective and some models lack proper comparisons between traditional and deep learning (DL) models, leading to poor performance metrics. To address these issues, the proposed work compares the traditional and deep learning models, with a focus on improving performance metrics. By adjusting the training process (epochs), the new system significantly increases the accuracy and reliability of disease detection, henceforth lead to better disease management and improve yield.  It also features a user-friendly web interface, making it easier for people to use. 
This proposed work outlines the development of a coconut disease detection system that integrates deep learning model with a user-friendly web interface. The dataset utilized in the project is sourced from Kaggle, which includes images of coconut plants exhibiting six different diseases such as Bud Root Dropping, Bud Rot, Stem Bleeding, CCI Caterpillar, gray Leaf Spot, Yellowing of Leaf.  The images are processed and augmented such that the trained models are capable of accurately identifying various disease types. The deep learning models VGG16, DenseNet201, Xception, ResNet, Inception, and MobileNetV2 are compared with traditional ML models. The performance of traditional ML classifiers: Random Forest, Logistic Regression, KNN, SVM using GLCM and SIFT features has been proved to better than DL models.
The project is implemented using Python, with a deep learning and ML models developed using Tensor Flow and Keras and many more for detecting diseases in coconut crops. The user interface is built with Flask, providing an accessible platform for users to upload images and interact with the system. 
The proposed work is validated through evaluation metrics, including confusion matrices and ROC curves.  VGG-16 DL model exhibited highest performance by achieving 99% accuracy rate and RF, KNN and Logistic regression with  SIFT features  exhibited cent percent accuracy in detection of 6 type of coconut diseases. 
SIFT features proved to be better than GLCM features for traditional ML models and VGG16 proved to be best among DL models for coconut disease detection.  Further future enhancements could involve developing a full-featured mobile application equipped with real-time image processing capabilities.





