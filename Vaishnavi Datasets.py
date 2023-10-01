# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt from sklearn.model_selection

import train_test_split from sklearn.preprocessing 

import LabelEncoder from sklearn.ensemble 

import RandomForestClassifier from sklearn.metrics 

import accuracy_score, confusion_matrix

# Step 2: Import the dataset from Excel
loan_data = pd.read_excel('loan-prediction.xlsx')

# Step 3: Understanding the data
print(loan_data.head())  
print(loan_data.info())  
# Step 4: Deal with missing values
loan_data.fillna(method='ffill', inplace=True)  # Forward-fill missing values

# Step 5: Data Visualization (if necessary)
# Step 6: Divide the dataset into training and test datasets
X = loan_data.drop('Loan_Status', axis=1)
y = loan_data['Loan_Status']

# Identify columns with mixed data types (int and str)
mixed_type_columns = X.select_dtypes(include=['int', 'object']).columns

# Convert columns with mixed data types to strings
for column in mixed_type_columns:
    X[column] = X[column].astype(str)

# Use label encoding to convert categorical variables to numeric
label_encoder = LabelEncoder()
X_encoded = X.apply(label_encoder.fit_transform)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Step 7: Build the machine learning model (Random Forest Classifier)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Step 8: Fit the model on the training dataset
model.fit(X_train, y_train)

# Step 9: Test the model and find accuracy
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print(f"Training Accuracy: {train_accuracy}")
print(f"Testing Accuracy: {test_accuracy}")

# Step 10: Create a confusion matrix
confusion_mat = confusion_matrix(y_test, y_test_pred)
print("Confusion Matrix:")
print(confusion_mat)
