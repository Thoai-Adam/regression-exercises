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

def wrangle_zillow():
    '''
    Read zillow into a pandas DataFrame from mySQL
    drop columns, drop any rows with Null values, 
    convert columns data types accordingly,
    return cleaned zillow DataFrame.
    '''
    # Acquire data 
    df = get_properties_2017()

    # Drop all rows with NaN values.
    df = df.dropna()
    
    # Convert to correct datatype
    df['yearbuilt'] = df.yearbuilt.astype(int)
    
    # rename columns
    
    df = df.rename(columns={'yearbuilt':'year_built'})
    df = df.rename(columns={'bedroomcnt':'bed_rooms'})
    df = df.rename(columns={'bathroomcnt':'bath_rooms'})
    df = df.rename(columns={'calculatedfinishedsquarefeet':'finished_sqft'})
    

    df = df[df.finished_sqft < 15_000]
    df = df[df.bed_rooms <= 10]
    df = df[df.bath_rooms <= 10]
    df = df[df.taxvaluedollarcnt <= df.taxvaluedollarcnt.quantile(0.75)]


    # split
    train, validate, test = split_data(df)
    
    return train, validate, test
