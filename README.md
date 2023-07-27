# MachineLearning_SummerChula
Doing classic and neural network model for predicting Alzheimer patients.
Done in Summer 2023 with Aj.Jo\
[training-groundtruth-new.csv](training-groundtruth-new.csv)

Steps Taken:
1. [Create openl3 embedding](create_OpenL3_Embbededing.ipynb)
2. [Train classic model using openl3 embedding](train_ClassicModel.ipynb)
3. [Test the trained classic model and representing the result using confusion matrix](test_ClassicModel.ipynb)
4. Train and test denseNN using vectorization on Google Speech-to-Text (need to change bitrate and channels of audio files)\
   [1. change audio file](change_audio.py)\
   [2. transcibe audio file in bucket](transcribe_in_cloudbucket.py)\
   [3. training](train_denseNN_vectorization.ipynb)
5. Decide to use mfcc as the only extracted feature. Train using CNN (cross Validated and grid searched).\
   [1. CV and Gridsearch](training_cvCNN.ipynb)\
   [2. Use the best parameter from 1. to train](training_CNN.ipynb)
