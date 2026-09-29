import pandas as pd
from pycaret.classification import *

# 1. Excel file load karein
file_name = 'Telco_customer_churn.xlsx'
print("Dataset load ho raha hai...")
data = pd.read_excel(file_name, sheet_name='Telco_Churn')

# 2. Data Cleaning: 'Total Charges' ko numeric mein badlein
if 'Total Charges' in data.columns:
    data['Total Charges'] = pd.to_numeric(data['Total Charges'], errors='coerce')

# 3. PyCaret Setup karein
print("PyCaret setup shuru ho raha hai...")
s = setup(
    data=data, 
    target='Churn Label', 
    ignore_features=['CustomerID', 'Lat Long', 'Churn Reason'], 
    session_id=123, 
    normalize=True, 
    verbose=False
)

# 4. Model train karein (Logistic Regression - Windows ke liye 100% safe aur fast)
print("Model train ho raha hai...")
best_model = create_model('lr')

# 5. Model finalize karein
print("Model finalize ho raha hai...")
final_model = finalize_model(best_model)

# 6. Predictions generate karein
print("Predictions generate ho rahi hain...")
predictions = predict_model(final_model, data=data, raw_score=True)

# 7. Output CSV file save karein
predictions.to_csv('Customer_Churn_Predictions.csv', index=False)
print("✅ Kaam ho gaya! 'Customer_Churn_Predictions.csv' file save ho chuki hai.")