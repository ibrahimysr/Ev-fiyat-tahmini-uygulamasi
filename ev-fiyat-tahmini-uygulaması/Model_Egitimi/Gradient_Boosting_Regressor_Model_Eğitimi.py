import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

df_2 = pd.read_excel(r"Emlak_3.xlsx")
df = df_2.copy() 


#logaritmik dönüşüm yapıyorum
df['Fiyat'] = np.log1p(df['Fiyat'])



print('Hedef değişken(Fiyat) ile en iyi ilişkisi olan değişkeni bulalım')
corr = df.corr()
corr.sort_values(['Fiyat'], ascending = False, inplace = True)

print(corr.Fiyat)  



y = df['Fiyat'] 
del df['Fiyat'] 

X = df.values
y = y.values 

#test verilerini ayırma 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 7)


#modeli egitme 
GBR = GradientBoostingRegressor(n_estimators = 200, max_depth = 5)  

GBR.fit(X_train, y_train)
print('Doğruluk Oranı: ', GBR.score(X_test, y_test)*100) # yüzde 77





