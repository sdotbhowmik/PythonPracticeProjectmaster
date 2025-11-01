import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler

#step 1: Create sample data
data = {
    "Age":[18,25,40,50,60],
    "Salary":[20000, 50000, 100000, 150000, 200000]
}

df = pd.DataFrame(data)
print("Original Data:\n",df)

#step 2: Feature Scaling, apply Min-Max Scaler (0-1)
minmax_scaler = MinMaxScaler()
df_minmax = pd.DataFrame(minmax_scaler.fit_transform(df),columns=df.columns)
print("\nAfter Min-Max Scaling\n",df_minmax)

#step 3: Feature Scaling, apply Standard Scaler (mean=0, std=1)
stand_scaler = StandardScaler()
df_standard = pd.DataFrame(stand_scaler.fit_transform(df),columns=df.columns)
print("\nAfter Standardization:\n",df_standard)