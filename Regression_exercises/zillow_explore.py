import os

import seaborn as sns
import matplotlib.pyplot as plt

def plot_categorical_and_continuous_vars(df, categorical_var, continuous_var):
    """
    Create plots for exploring the relationship between a categorical variable and a continuous variable.

    Parameters:
    df (DataFrame): The DataFrame containing your Zillow data.
    categorical_var (str): The name of the categorical variable.
    continuous_var (str): The name of the continuous variable.

    Returns:
    None
    """
    # Create a box plot to visualize the distribution of the continuous variable for each category in the categorical variable
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=categorical_var, y=continuous_var)
    plt.title(f'Box Plot of {continuous_var} by {categorical_var}')
    plt.xlabel(categorical_var)
    plt.ylabel(continuous_var)
    plt.xticks(rotation=45)
    plt.show()

    # Create a bar plot to visualize the distribution of the categorical variable
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=categorical_var)
    plt.title(f'Count of {categorical_var}')
    plt.xlabel(categorical_var)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
# categorical_var = 'fips'  
# continuous_var = 'taxvaluedollarcnt'  

# plot_categorical_and_continuous_vars(df, categorical_var, continuous_var)



def plot_variable_pairs(df):
    """
    Create a pairplot to visualize relationships between numerical variables in a DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the variables to be plotted.

    Returns:
    None
    """
    # Select only numerical columns for the pairplot
    numerical_columns = df.select_dtypes(include=['number'])

    # Create the pairplot
    sns.pairplot(numerical_columns)
    plt.show()
