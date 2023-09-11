import pandas as pd
import numpy as np
import os
import env
from env import get_connection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer

def prep_function():
    # connect to sql zillow database

    url = "zillow"

    # use this query to get data    
    sql_query = '''SELECT *
            FROM predictions_2017
            JOIN properties_2017 on properties_2017.parcelid = predictions_2017.parcelid
            JOIN propertylandusetype on propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid;
            '''

    # assign data to data frame
    df = pd.read_sql(sql_query, get_connection(url))

#filter out single family residential as requested
    df= df[df['propertylandusedesc'] == 'Single Family Residential']
    return df

def clean_zillow():
        df= df[df['propertylandusedesc'] == 'Single Family Residential']
    df.shape

# Convert the 'transactiondate' column to datetime
    df['transactiondate'] = pd.to_datetime(df['transactiondate'])

# Define the start and end dates for the range
    start_date = pd.to_datetime('2017-01-01')
    end_date = pd.to_datetime('2017-12-31')

# Filter the DataFrame to keep rows within the specified date range
    df= df[(df['transactiondate'] >= start_date) & (df['transactiondate'] <= end_date)]

    columns_to_keep = ['bathroomcnt',
                   'bedroomcnt',
                   'calculatedfinishedsquarefeet',
                   'yearbuilt',
                   'taxvaluedollarcnt']
    df = df[columns_to_keep]
    
    #dropping more nulls
    df.dropna()
    #1. Rename the columns to be more readable
    df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                          'bathroomcnt':'bathrooms', 
                          'calculatedfinishedsquarefeet':'area', 
                          'taxvaluedollarcnt':'tax_value', })
    
def Do_Da_Split():
        ### Splitting


    train_validate, test = train_test_split(df, test_size=.2, random_state=42)

    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                        random_state=42)