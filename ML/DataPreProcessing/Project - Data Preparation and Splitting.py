import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

# Step 1: Load Dataset
df = pd.read_csv("employees.csv")
print("First 5 rows:\n", df.head())

# Step 2: Features & Label
X = df.drop("Promotion_Eligibility", axis=1)
y = df["Promotion_Eligibility"]

print("\nFeatures:\n", X.head())
print("\nLabel:\n", y.head())

# Step 3: Encoding Categorical Data
# Label Encoding: Gender
df["Gender_Label"] = df["Gender"].map({"Male": 0, "Female": 1})
print("\nAfter Label Encoding Gender:\n", df[["Name","Gender","Gender_Label"]].head())

# One-Hot Encoding: Department
df_onehot = pd.get_dummies(df, columns=["Department"])
print("\nAfter One-Hot Encoding Department:\n", df_onehot.head())

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, df["Promotion_Eligibility"], test_size=0.2, random_state=42)
print("\nTrain shape:", X_train.shape, y_train.shape)
print("Test shape:", X_test.shape, y_test.shape)

# Step 5: Feature Scaling
# Normalization
minmax = MinMaxScaler()
X_normalized = minmax.fit_transform(X.select_dtypes(include='number'))
print("\nAfter Normalization:\n", X_normalized[:5])

# Standardization
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X.select_dtypes(include='number'))
print("\nAfter Standardization:\n", X_standardized[:5])


