import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import pickle

# Load the iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target labels

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
acc = accuracy_score(y_test, y_pred)

print(f'Model accuracy is {acc * 100:.2f}%')

# Optionally: save the model with pickle for later use
with open('iris_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

# Visualize feature importance (Optional)
plt.figure(figsize=(10, 6))
sns.barplot(x=iris.feature_names, y=model.feature_importances_)
plt.title('Feature Importance')
plt.ylabel('Importance')
plt.show()
