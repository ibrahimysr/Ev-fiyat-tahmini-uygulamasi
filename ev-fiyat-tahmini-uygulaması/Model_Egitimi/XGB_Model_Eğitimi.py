import pandas as pd
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn import model_selection  

df_2 = pd.read_excel(r"Veriler//Çalışma_verisi.xlsx")
df = df_2.copy()

X = df.drop(["Grup"], axis = 1)
y = df["Grup"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 144)
"""
# GridSearchCV 

params = {"colsample_bytree":[0.4,0.5,0.6],
         "learning_rate":[0.01,0.02,0.09],
         "max_depth":[2,3,4,5,6],
         "n_estimators":[100,200,500,2000]}

xgb = XGBRegressor()

grid = GridSearchCV(xgb, params, cv = 10, n_jobs = -1, verbose = 2)

grid.fit(X_train, y_train)

print(grid.best_params_) # (colsample_bytree = 0.6, learning_rate = 0.02, max_depth = 5, n_estimators = 2000) 

"""
xgb1 = XGBRegressor(colsample_bytree = 0.6, learning_rate = 0.02, max_depth = 5, n_estimators = 2000) 
model_xgb = xgb1.fit(X_train, y_train) 
 
print(model_xgb.score(X_test, y_test)) #73
print(model_xgb.score(X_train, y_train)) #83
#print(np.sqrt(-1*(cross_val_score(model_xgb, X_test, y_test, cv=10, scoring='neg_mean_squared_error'))).mean()) # valide edilmiş (doğrulanmış hata oranımızı buluyoruz)

importance = pd.DataFrame({"Importance": model_xgb.feature_importances_},
                         index=X_train.columns)

print(importance)
