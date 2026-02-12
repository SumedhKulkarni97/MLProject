import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataTransformation:
    def __init__(self):
        self.data_path = os.path.join('artifacts', 'preprocessed_data.csv')

    def initiate_data_transformation(self):
        df = pd.read_csv(self.data_path)
        
        X = df.drop(columns=['Churn'], axis=1)
        y = df['Churn']

        # 'stratify=y' ensures both sets have the same % of churned customers
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # We fit only on training data to prevent data leakage
        scaler = StandardScaler()
        
        # Identify numerical columns to scale
        num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
        
        X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
        X_test[num_cols] = scaler.transform(X_test[num_cols])
        
        print(f"Training shape: {X_train.shape}, Test shape: {X_test.shape}")
        
        return X_train, X_test, y_train, y_test
    
if __name__ == "__main__":
    obj = DataTransformation()
    X_train, X_test, y_train, y_test = obj.initiate_data_transformation()