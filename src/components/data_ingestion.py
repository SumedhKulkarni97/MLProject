import kagglehub
import pandas as pd
import os

# kagglehub handles the path automatically. 
print("Downloading dataset from Kaggle...")
download_path = kagglehub.dataset_download("blastchar/telco-customer-churn")

# Find the CSV file
csv_filename = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
full_path = os.path.join(download_path, csv_filename)

# Load the data
try:
    df = pd.read_csv(full_path)
    print(f"Data successfully ingested from: {full_path}")
    print(f"Dataset Shape: {df.shape}")
    
    # Save a copy locally
    os.makedirs('artifacts', exist_ok=True)
    df.to_csv('artifacts/raw_data.csv', index=False)
    
except FileNotFoundError:
    print(f"Error: Could not find {csv_filename} at {download_path}")

if __name__ == "__main__":
    print(df.head())