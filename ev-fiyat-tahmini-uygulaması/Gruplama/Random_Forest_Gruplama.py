# Gerekli kütüphaneleri yükleyin
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import classification_report


# Veri kümesini yükleyin (örneğin, bir CSV dosyasından)
# Veri çerçevesinin içinde "Fiyat" adlı bir sütunun olması gerekmektedir.
# Ayrıca, diğer özellik sütunları da olmalıdır.
data = pd.read_excel(r"Emlak_5.xlsx")

# Bağımsız değişkenleri ve hedef değişkeni seçin
X = data.drop('Grup', axis=1)
y = data['Grup']

# Eğitim ve test setlerini oluşturun
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest modelini oluşturun
rf_model = RandomForestClassifier(n_estimators=100)


# Modeli eğitin
rf_model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapın
y_pred = rf_model.predict(X_test)



# Sınıflandırma raporunu yazdırma
print(classification_report(y_test, y_pred)) 


# Karmaşıklık matrisini oluşturun
conf_matrix = confusion_matrix(y_test, y_pred)

# Sonuçları ekrana yazdırın
print("Karmaşıklık Matrisi:\n", conf_matrix)

