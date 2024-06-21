import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Veri kümesini yükle
data = pd.read_excel(r"Emlak_5.xlsx")

# Veri kümesini bağımsız değişkenler (X) ve bağımlı değişken (y) olarak ayırma
X = data.drop('Grup', axis=1)
y = data['Grup']

# Eğitim ve test kümelerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

from sklearn.tree import DecisionTreeClassifier 
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state=0)
classifier.fit(X_train, y_train)



# Tüm veri seti üzerinde tahmin yapma
y_pred = classifier.predict(X_test)

# Sınıflandırma raporunu yazdırma
print("Classification Report:\n", classification_report(y_test, y_pred))

# Karmaşıklık matrisini oluşturun
conf_matrix = confusion_matrix(y_test, y_pred)

# Sonuçları ekrana yazdırın
print("Karmaşıklık Matrisi:\n", conf_matrix)
