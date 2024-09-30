# Assignment 03: Basic Cleaning

This assignment involves basic data cleaning tasks on two datasets: the **NFL Dataset** and the **San Francisco Building Permits Dataset**. The goal is to handle missing values, correct data inconsistencies, and prepare the data for further analysis.

## Sidenotes:
1. Since the some of the outputs are too large, I've removed thoses large outputs cells

## Datasets:
1. **NFL Dataset**: Contains various statistics about NFL players, teams, and game performances.
2. **San Francisco Building Permits Dataset**: Provides details on building permits issued in San Francisco, including permit types, project descriptions, addresses, and compliance information.

## Objectives:
1. Summarize Dataset
2. Identify and Handle Missing Data
3. Impute Missing Values
4. Identify Statistical Impact of Data Imputation


## Reflection

In this assignment, we have to perform those tasks:
- Read the raw data from CSV file
- Learn about and describe the data, for instance:
  - Learn a few first rows and columns of the dataframe.
  - Learn some basice statistic of the data like: count, mean, std, min, 25%, 50%, 75%, max.
  - Learn the columns' name and the meaning/definition of them.
- Deal with missing values:
  - See the number/percentage of NaN in each rows/columns.
  - See the number/percentage of rows/columns with NaN values.
- Try to drop all rows/columns containing missing values, and we end up having 0 rows in the dataframe.
- Impute data using median imputation method.
  - Firstly, we order the columns in the dataframe, move all string columns to the back.
  - Secondly, we save the labels of the dataframe to a list, and then remove the labels from the dataframe.
  - Thirdly, we save columns with 'object' datatype to a different dataframe.
  - Forthly, we remove all columns with 'object' datatype from the original dataframe.
  - Fifthly, we perform imputation on the dataframe with only numerical data.
  - Sixthly, we concatinate the two dataframes (numerical dataframe and object dataframe).
  - Seventhly, we add the labels back to the dataframe.
- Try to impute data using KNN method.
  - Due to the large data size (rows and columns) the computation for each missing value can take significant time. Each imputation requires searching through the entire dataset, leading to cumulative delays.
- Fill missing values using back fill and forward fill method.
- Fill missing values using mean fill method.
- Calcualate mean, standard deviation, and correlation difference after impute/back-forward fill/mean fill.

## Reflection Questions
### NFL Dataset:
1. What do I believe I did well on this assignment?
    - I tried KNN imputation but the running time is too long due to a large dataset.
    - I could count, get the percentage, consider dropping and filling for different types missing values (e.g: numberical, categorical and string data) in the dataframe. 
    - I applied different imputation techniques: 
      - Median impute
      - Back fill + forward fill for numberical, categorical and string data
      - Mean fill for numerical data. 
      - For categorical data, I filled missing values with "unknown". 
    - Before applying imputation, I fixed the dataframe, for instance:
      - Remove all columns with 'object' datatype
      - Putting the labels/string columns back to the dataframe after imputing

2. What was the most challenging part of this assignment?
    - The KNN imputation took too much time to run due to a large dataset.
    - Learning the meaning/definition of columns and then figure out the reason why the values are missing.
3. What would have made this assignment a better experience?
    - A better explaination of the meaning/definition of the columns would much help me understanding the dataset.
4. What do I need help with?
    - I need help in how to reduce the dataset size so that KNN imputation would not take too much time to run.
    - I'd need guidance on how to handle correlations and statistical comparisons between original and imputed datasets. I could use some better imputation methods to fill missing values where back fill or mean fill method may not be approriate.
5. What did I actually learn by doing this assignment? Why does it matter?
    - I learned how to manipulate the dataframe to meet my needs (e.g: removing specific columns, save the labels, put the labels/columns back after imputing).
    - Datasets always have missing data, it is important to understand why the data is missing.
      - Is it not recorded by mistakes, or
      - Is it intentionally left as a blank.
    - I learned there were many ways to fill the missing values and dropping the rows/columns with missing data is sometimes not a good idea
    - I learned that it is important to keep the statistics of the dataset after filling the missing values.

### San Fran Permits Dataset:
1. What do I believe I did well on this assignment?
    - I could identify and handle the missing values in my dataset. I applied different imputation techniques: back fill + front fill, and mean fill for numerical data. For categorical data, I filled missing values with "Unknown". 
2. What was the most challenging part of this assignment?
    - It is challenging to identify why there are so many missing values. There are terminologies that I had to look up to better comprehend the dataset columns.
3. What would have made this assignment a better experience?
    - A detailed documentation/README on the dataset would help.
4. What do I need help with?
    - I'd need guidance on how to handle correlations and statistical comparisons between original and imputed datasets. I could use some better imputation methods to fill missing values where back fill or mean fill method may not be approriate.
5. What did I actually learn by doing this assignment? Why does it matter?
    - I learn that Cleaning data is a crucial process. Most raw dataset is incomplete and inconsistent, which would hinder the ability to analyze data and draw conclusion. This exercise taught me how to approach and clean dataset based on its unique characteristics.