# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:20:24 2020

@author: HengZhi
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
# In[] 設定玉選取的關鍵特徵數量
first_feature_of_Ra = 6
# In[] 讀取檔案
savepath = r'/key/'
filepath = r'/KEY.csv'
load= pd.read_csv(filepath)
# In[] 副程式
def FeatureScore(X,Y):
    X = X.T
#    lin_reg = LinearRegression()
#    lin_reg.fit(x1, y)
    lasso_reg = Lasso(alpha=0.1)
    lasso_reg.fit(X, Y)
    score = lasso_reg.score(X,Y)
#    elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
#    elastic_net.fit(x1, y)
    return score

def ALL_FeatureScore(Featurename):
    score_list = []
    for i in range(len(load.columns)-1):
        Feature_X = np.array(load.iloc[:,i])
        Feature_X = Feature_X[np.newaxis]
        Feature_Y = list(load[Featurename])
        score_list.append((load.columns[i],FeatureScore(Feature_X,Feature_Y)))
    return score_list

def KeyFeatureSet(number,Feature):
    header = []
    data_save = pd.DataFrame([])
    for j in range(number):
        header.append(Feature[j][0])
        data_save = pd.concat([data_save,load[header[j]]],axis = 1)
    return data_save

def Savedata(data,workpiece):
    data.to_csv('%s/python_%s_KEY_data.csv' %(savepath,workpiece))
# In[] 主程式 -行49為Y名稱
Feature_name = "Roughness_Ra(um)"
KeyFeature_Ra = KeyFeatureSet(first_feature_of_Ra,sorted(ALL_FeatureScore(Feature_name), key = lambda s:s[1], reverse = True))
KeyFeature_score=sorted(ALL_FeatureScore(Feature_name), key = lambda s:s[1], reverse = True)
# In[] 主程式(存檔)
Savedata(KeyFeature_Roughness_Ra(um),"20200521")