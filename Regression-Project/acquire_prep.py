import pandas as pd
import numpy as np
import os
import env
from env import get_connection
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer

def get_db_url(database):
    return f'mysql+pymysql://{user}:{pwd}@{host}/{database}'

--------------------------------------------------------------------------------
# create helper function to get the necessary connection url.
def get_db_connection(database):
    return get_connection(database)

# connect to sql zillow database
def acquire_db():
    url = "zillow"

    # use this query to get data    
    sql_query = '''SELECT *
                FROM predictions_2017
                JOIN properties_2017 on properties_2017.parcelid = predictions_2017.parcelid
                JOIN propertylandusetype on propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid;
                '''

    # assign data to data frame
    df = pd.read_sql(sql_query, get_connection(url))
    return df
--------------------------------------------------------------------------------

def prep():
    
    #filter out single family residential as requested
    df= df[df['propertylandusedesc'] == 'Single Family Residential']
    df.shape

    # Convert the 'transactiondate' column to datetime
    df['transactiondate'] = pd.to_datetime(df['transactiondate'])

    # Define the start and end dates for the range
    start_date = pd.to_datetime('2017-01-01')
    end_date = pd.to_datetime('2017-12-31')

    # Filter the DataFrame to keep rows within the specified date range
    df= df[(df['transactiondate'] >= start_date) & (df['transactiondate'] <= end_date)]
    
    
    #filter out single family residential as requested
    df= df[df['propertylandusedesc'] == 'Single Family Residential']
    df.shape
    # Acquire data 
    df = get_properties_2017()

    # Drop all rows with NaN values.
    df = df.dropna()
    
    # Convert to correct datatype
    df['yearbuilt'] = df.yearbuilt.astype(int)
    
    # rename columns
    
    df = df.rename(columns={'yearbuilt':'year'})
    df = df.rename(columns={'bedroomcnt':'bed'})
    df = df.rename(columns={'bathroomcnt':'bath'})
    df = df.rename(columns={'calculatedfinishedsquarefeet':'sqft'})
    

    df = df[df.finished_sqft < 15_000]
    df = df[df.bed_rooms <= 10]
    df = df[df.bath_rooms <= 10]
    df = df[df.taxvaluedollarcnt <= df.taxvaluedollarcnt.quantile(0.75)]
    
    #filter out single family residential as requested
    df= df[df['propertylandusedesc'] == 'Single Family Residential']

    
    
    # split
    train, validate, test = split_data(df)
    
    return train, validate, test




    ###### split data #############
    


def split_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames.
    return train, validate, test DataFrames.
    '''
    
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123)
    return train, validate, test