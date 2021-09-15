# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:04:40 2020

@author: HengZhi
"""

from keras.models import load_model




NN_model = load_model('Model/_T4new-cell(20-5)-epochs6000-batch_size2-MAE(0.1341).h5')

prediction = NN_model.predict(array) #將你要預測的資料轉乘array，並輸入model