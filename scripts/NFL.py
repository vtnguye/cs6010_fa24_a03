import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer

# Specify the path to your CSV file
file_path = '../data/raw/NFL.csv'

# Create a DataFrame from the CSV file
df = pd.read_csv(file_path)

number_cols = df.select_dtypes(exclude=['object']).columns
object_cols = df.select_dtypes(include=['object']).columns

number_df = df.select_dtypes(exclude=['object'])
object_df = df.select_dtypes(include=['object'])

# Reorder the DataFrame
df = pd.concat([df[number_cols], df[object_cols]], axis=1)

# Get columns' label
column_labels = df.columns.tolist()
# Remove column labels
# df.columns = [''] * len(df.columns)  # Set column names to empty strings

### ----------------- Median Imputation ----------------- ###

my_imputer = SimpleImputer(strategy='median')
data_with_imputed_values = my_imputer.fit_transform(number_df)
data_with_imputed_values_dataframe = pd.DataFrame(data_with_imputed_values)

# Concatenating along the columns (axis=1)
data_with_imputed_values_dataframe = pd.concat([data_with_imputed_values_dataframe, object_df], axis=1)

# Put labels back to df
# df.columns = column_labels
data_with_imputed_values_dataframe.columns = column_labels
print(data_with_imputed_values_dataframe)

# Fill missing string values with 'Unknown'
data_with_imputed_values_dataframe[object_cols] = data_with_imputed_values_dataframe[object_cols].fillna('Unknown')
print(data_with_imputed_values_dataframe)

# Mean imputation
number_cols = df.select_dtypes(exclude=['object']).columns
object_cols = df.select_dtypes(include=['object']).columns

mean_difference = data_with_imputed_values_dataframe[number_cols].mean() - df[number_cols].mean()
print("\nMean Difference:")
print(mean_difference.round(3))

std_difference = data_with_imputed_values_dataframe[number_cols].std() - df[number_cols].std()
print("\nStandard Deviation Difference:")
print(std_difference.round(3))

corr_difference = data_with_imputed_values_dataframe[number_cols].corr() - df[number_cols].corr()
print("\nCorrelation Difference:")
print(corr_difference.round(3)
      
### ----------------- Forward and Back Fill ----------------- ###

df_bffill = df.copy()

object_columns = df.select_dtypes(include=['object']).columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Fill missing string values with 'Unknown'
df_bffill[object_columns] = df_bffill[object_columns].fillna('Unknown')


# Fill missing numerical values with the bffill method
df_bffill[numerical_columns] = df_bffill[numerical_columns].ffill().bfill()

print("\nMissing Values After Back and Forward Fill:")
print(df_bffill.isna().sum().sum())

# Back and Forward Fill
mean_difference = df_bffill[numerical_columns].mean() - df[numerical_columns].mean()
print("\nMean Difference:")
print(mean_difference.round(3))

std_difference = df_bffill[numerical_columns].std() - df[numerical_columns].std()
print("\nStandard Deviation Difference:")
print(std_difference.round(3))

corr_difference = df_bffill[numerical_columns].corr() - df[numerical_columns].corr()
print("\nCorrelation Difference:")
print(corr_difference.round(3))

### ----------------- Mean Fill ----------------- ###

df_meanfill = df.copy()

object_columns = df.select_dtypes(include=['object']).columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Fill missing string values with 'Unknown'
df_meanfill[object_columns] = df_meanfill[object_columns].fillna('Unknown')

# Fill missing numerical values with the mean of the column
df_meanfill[numerical_columns] = df_meanfill[numerical_columns].fillna(df_meanfill[numerical_columns].mean().round(0))

print("\nMissing Values After Mean Fill:")
print(df_meanfill.isna().sum().sum())

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