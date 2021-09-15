# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:05:13 2020

@author: Tusy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from keras import backend as K
from sklearn.model_selection import train_test_split

# In[] 
modelsave_path = r'D:\PythonCode\MisLab\NN\Model'
data_path = r"D:\PythonCode\MisLab\NN\dataset\20200109newfeature.csv"

# In[] read data
df = pd.read_csv(data_path)
dfx = np.array(df.iloc[:,1:6])
dfy = np.array([df.iloc[:,-1]]).T

x_train, x_test, y_train, y_test = train_test_split(dfx, dfy, test_size = 0.3)

# In[] NN
#K.clear_session()


def baseline_model():
    model = Sequential() #,kernel_initializer='normal'
    model.add(Dense(20,kernel_initializer='normal', input_dim=5, activation='relu'))
    model.add(Dense(10, activation='relu' ))
    model.add(Dense(1, activation='relu' )) #'linear' 'sigmoid'
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae']) #binary_crossentropy #mean_squared_error
    return model

estimator = KerasRegressor(build_fn=baseline_model, epochs=500, batch_size=3)
estimator.fit(x_train,y_train)

# In[] predict
predict_y = estimator.predict(x_test)
predict_y = estimator.predict(x_train)

plt.plot(predict_y, label="Predict")
plt.plot(y_test, label="Real")
plt.legend()
plt.show()
# In[] Save Model
estimator.model.save(modelsave_path+r"\10-12-(2500-5).h5")