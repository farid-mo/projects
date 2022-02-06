# -*- coding: utf-8 -*-
"""
ImageAI tutorial

https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Classification/README.md

Created on Sun Feb 6 2022

@author: Farid
"""
from imageai.Prediction import ImagePrediction
import os

# Execution path
execution_path = os.getcwd()

# Load the model
prediction = ImagePrediction()
prediction.setModelTypeAsMobileNetV2()
h5_file_path = os.path.join(execution_path, "mobilenet_v2.h5")
prediction.setModelPath(h5_file_path)
prediction.loadModel()

# Prediction with condidence
path = os.path.join(execution_path, "house.jpg")
predictions, probabilities = prediction.classifyImage(path, result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(f"{eachPrediction} : {eachProbability:.2f} %")
