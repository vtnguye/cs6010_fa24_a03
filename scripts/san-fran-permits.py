import pandas as pd


# Dataset Summary
file_path = '../data/raw/Building_Permits.csv'
df = pd.read_csv(file_path)

print(df.describe())

# Data Cleaning
# Missing data:

missing_data = df.isna().sum()
total_missing = df.isna().sum().sum()
missing_data_columns = missing_data[missing_data > 0]

print("\nTotal Missing Values:" + str(total_missing))
print("\nColumns with Missing Values:")
print(missing_data_columns)
print("\nNumber of Columns with Missing Values: " + str(missing_data_columns.count()))

missing_data_columns_percentage = missing_data_columns / df.shape[0] * 100
print("\nColumns with Missing Values Percentage of Overall:")
print(missing_data_columns_percentage)

df_bffill = df.copy()
df_meanfill = df.copy()

object_columns = df.select_dtypes(include=['object']).columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Fill missing string values with 'Unknown'
df_bffill[object_columns] = df_bffill[object_columns].fillna('Unknown')
df_meanfill[object_columns] = df_meanfill[object_columns].fillna('Unknown')

# Fill missing numerical values with the mean of the column
df_meanfill[numerical_columns] = df_meanfill[numerical_columns].fillna(df_meanfill[numerical_columns].mean().round(0))

# Fill missing numerical values with the bffill method
df_bffill[numerical_columns] = df_bffill[numerical_columns].bfill().ffill()

# Double check if there are any missing values
print("\nMissing Values After Fill:")
print("Mean Fill:")
print(df_meanfill.isna().sum().sum())
print("Bffill Fill:")
print(df_bffill.isna().sum().sum())

# Statistical impact of filling missing values
# Mean Fill
mean_difference = df_meanfill[numerical_columns].mean() - df[numerical_columns].mean()
print("\nMean Difference:")
print(mean_difference.round(3))

std_difference = df_meanfill[numerical_columns].std() - df[numerical_columns].std()
print("\nStandard Deviation Difference:")
print(std_difference.round(3))

corr_difference = df_meanfill[numerical_columns].corr() - df[numerical_columns].corr()
print("\nCorrelation Difference:")
print(corr_difference.round(3))

# Bffill Fill
mean_difference = df_bffill[numerical_columns].mean() - df[numerical_columns].mean()
print("\nMean Difference:")
print(mean_difference.round(3))

std_difference = df_bffill[numerical_columns].std() - df[numerical_columns].std()
print("\nStandard Deviation Difference:")
print(std_difference.round(3))

corr_difference = df_bffill[numerical_columns].corr() - df[numerical_columns].corr()
print("\nCorrelation Difference:")
print(corr_difference.round(3))