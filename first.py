a=12
print(a)

b="Madhuri Pujari"
print(b)


# train random forest model for prediction
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split    
# Load the dataset
data = pd.read_csv('dataset.csv')
# Preprocess the data (handle missing values, encode categorical variables, etc.)
# For example, let's assume 'target' is the column we want to predict               
X = data.drop('target', axis=1)  # Features
y = data['target']  # Target variable\
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train the Random Forest model             
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train) 
# Make predictions on the test set
predictions = model.predict(X_test)
# Evaluate the model (e.g., accuracy, confusion matrix, etc.)
from sklearn.metrics import accuracy_score, confusion_matrix
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
