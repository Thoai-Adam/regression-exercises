import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from env import get_connection  # Make sure these variables are defined in env.py
from sklearn.model_selection import train_test_split

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

def visualize_data2(df):
    cols = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt', 'yearbuilt', 'taxamount', 'fips']
    plt.figure(figsize = (3,2))
    sns.histplot(data = df, x=cols)
    plt.title(f'Distribution of {col}')
    plt.show
    
    
def apply_scaling(df_train, df_validate, df_test, scaler):
    # Columns to scale
    cols_to_scale = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt', 'yearbuilt', 'taxamount']

    # Fit scaler on training data and transform all data splits
    scaler.fit(df_train[cols_to_scale])
    df_train[cols_to_scale] = scaler.transform(df_train[cols_to_scale])
    df_validate[cols_to_scale] = scaler.transform(df_validate[cols_to_scale])
    df_test[cols_to_scale] = scaler.transform(df_test[cols_to_scale])

    return df_train, df_validate, df_test



def prepare_zillow_data():
    # Acquire and clean data
    df = acquire_data()
    df_cleaned = clean_and_impute_data(df)

    # Visualize cleaned data
    visualize_data(df_cleaned)

    # Split data into train, validate, and test sets

    # Apply scaling using MinMaxScaler
    df_train_scaled, df_validate_scaled, df_test_scaled = apply_scaling(df_train, df_validate, df_test, MinMaxScaler())

    return df_train_scaled, df_validate_scaled, df_test_scaled


def train_val_test(df, seed = 42):
    
    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed)
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed)
    
    return train, val, test




def columns_scaling(df):
        # Columns to scale
        cols_to_scale = ['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt', 'yearbuilt', 'taxamount']

        # Fit scaler on training data and transform all data splits
        StandardScaler.fit(df_train[cols_to_scale])
        df_train[cols_to_scale] = scaler.transform(df_train[cols_to_scale])
        df_validate[cols_to_scale] = scaler.transform(df_validate[cols_to_scale])
        df_test[cols_to_scale] = scaler.transform(df_test[cols_to_scale])

        return df_train, df_validate, df_test
    
    
    
def prepare_zillow_data():
    # Acquire and clean data
    df = acquire_data()
    df_cleaned = clean_and_impute_data(df)

    # Visualize cleaned data
    visualize_data(df_cleaned)

    # Split data into train, validate, and test sets

    # Apply scaling using MinMaxScaler
    df_train_scaled, df_validate_scaled, df_test_scaled = apply_scaling(df_train, df_validate, df_test, MinMaxScaler())

    return df_train_scaled, df_validate_scaled, df_test_scaled


def scale_data(train, val, test, to_scale):
    #make copies for scaling
    train_scaled = train.copy()
    validate_scaled = val.copy()
    test_scaled = test.copy()
    #make the thing
    scaler = MinMaxScaler()
    #fit the thing
    scaler.fit(train[to_scale])
    #use the thing
    train_scaled[to_scale] = scaler.transform(train[to_scale])
    validate_scaled[to_scale] = scaler.transform(val[to_scale])
    test_scaled[to_scale] = scaler.transform(test[to_scale])
    return train_scaled, validate_scaled, test_scaled