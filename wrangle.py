import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from env import get_connection  # Make sure these variables are defined in env.py

def acquire_data():
    url = get_connection('zillow')
    query = '''
            SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet,
                   taxvaluedollarcnt, yearbuilt, taxamount, fips
            FROM properties_2017
            JOIN propertylandusetype
                ON properties_2017.propertylandusetypeid = propertylandusetype.propertylandusetypeid
            WHERE propertylandusetype.propertylandusedesc = 'Single Family Residential';
            '''
    df = pd.read_sql(query, url)
    return df

def clean_and_impute_data(df):
    # Drop rows with null values in specified columns
    columns_to_drop_null = ['bedroomcnt', 'bathroomcnt', 'taxvaluedollarcnt']
    df.dropna(subset=columns_to_drop_null, inplace=True)
    
    # Impute null values with means for specified columns
    columns_to_impute = ['calculatedfinishedsquarefeet', 'yearbuilt', 'taxamount']
    for column in columns_to_impute:
        mean_value = df[column].mean()
        df[column].fillna(mean_value, inplace=True)
    
    return df

def visualize_data(df):
    plt.figure(figsize=(16, 3))

    # List of columns
    cols = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt', 'yearbuilt', 'taxamount', 'fips']

    for i, col in enumerate(cols):
        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, 10, plot_number)

        # Title with column name.
        plt.title(col)

        # Display histogram for column.
        df[col].hist(bins=5)

        # Hide gridlines.
        plt.grid(False)

    plt.figure(figsize=(10, 14))

    # Create boxplots for all but fips.
    sns.boxplot(data=df.drop(columns=['fips']))
    plt.show()

def main():
    df = acquire_data()
    cleaned_df = clean_and_impute_data(df)
    visualize_data(cleaned_df)

if __name__ == "__main__":
    main()
