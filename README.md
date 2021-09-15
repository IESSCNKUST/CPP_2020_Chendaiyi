# CPP_2020_Chendaiyi

本專案為"組件製程參數Component-process-parameters"之相關資料，
其主要研究題目為： 
開發估測金屬積層製造粗糙度之關鍵特徵搜尋與應用方法
Development of Key Feature Searching and Application Methods for Estimating Roughness of Additive Manufacturing

摘要：
當進行金屬積層製造時，製程中的相關參數會存在許多因素導致加工品質不穩定以及加工工件毀損。本研究便是為解決製程過程中之因表面粗糙度不佳，導致加工品質較差而建立的方法。

本研究開發估測粗糙度之關鍵特徵搜尋與應用方法，特點為特徵萃取與模型建立。在關鍵特徵尋找上，首先為增強模型的準確性與可解釋性，利用LASSO(Least absolute shrinkage and selection operator)算法進行特徵篩選選出與粗糙度關聯度最高之關鍵特徵。在模型建立上，經由類神經網路(Neural Network，NN)學習與建立模型。利用篩選出的關鍵特徵，進行表面粗糙度模型的預測。


領域：
金屬積層製造

目標：
以本研究物件SUS420粉末為例，在雷射功率160瓦特至270瓦特，以及雷射速度600mm/s至850mm/s的製程參數中，可於尚未進行實際製程前，便提前預知下一層表面粗糙度，並其預測表面粗糙度的MAPE穩定在5%以內。

文件類別：
1.KeyFeature為篩選關鍵特徵
2.NN為模型建立
3.LoadNN_Model為載入建立好的模型並執行預測
