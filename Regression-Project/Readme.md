#### Read Me Now!!

# Zillow Regression Project

## Goals : 
    * ML Regression model 
        * predict property tax assessed values
    * Key drivers of property
        * why some properties have much higher value than other when they are located so close to each other?
        * Why are some properties valued so differently from others when they havenearly the same physical attributes but only differ in location?
        * Is having 1 bathroom worse for property value than having 2 bedrooms?
    * Report and Conclusion
        * delivery replicatable report and outcomes
        * make recommendation
## Descriptions
    * We want to be able to predict the property tax assessed values('taxvaluedollarcnt') of Single Family Properties that had a transaction during 2017. We need to make a better model with new feature with non-linear regression algorithm, or different model for each county. Identify the states and counties these properties are located in.


## Planning
    1) properties that had a transaction in 2017! 
        *filter data in SQL with predictions_2017, properties_2017, and propertylandusetype
    2) Remove landtaxvaluedollarcnt, structuretaxvaluedollarcnt, and taxamount columns. Drop/impute null values. Feature engineering. Encode categorical variables. Normalize or Scale as needed
    3) Train-Test Split
    4) Find baseline and apply regression model selection
    5) Fit the train selected regression model
    6) Evaluate model's performance like Mean Absolute Error, Mean Squared Error, R-squared
    7) FIND Key driver
    8) Interpretation of visual and recommendation 
    9) Prep Report and slide


## Initial Hypotheses or Questions of data
    


#### Hyperlink to acquire module (.py)
[hyperlink](https://www.markdownguide.org/)
#### Hyperlink to prepare module (.py)
[hyperlink](https://www.markdownguide.org/)
#### Hyperlink to scratch notebook (.ipny)
[hyperlink](https://www.markdownguide.org/)
#### Hyperlink to final project
[hyperlink](https://www.markdownguide.org/)

#### Data Dictionary
| Variable Name | Description | Data Type |
|---------|:-------------|:--------------:||
| parcelid | Unique identifier for the property | Numeric |
| propertylandusetypeid | Type of land use for the property | Numeric |
| transactiondate | Date of property transaction | Date |
| bathromcnt | Numer of bathrooms | numeric |
| bedroomcnt | number of bedrooms | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |
| Default | Left | Center |

Certainly, here is the modified data dictionary without the "Non-Null Count" column:

| Column Name                      | Description                                                       | Data Type |
|----------------------------------|-------------------------------------------------------------------|-----------|
| id                               | Unique identifier for the property                                | int64     |
| parcelid                         | Unique identifier for the parcel                                  | int64     |
| logerror                         | Logarithmic error of the property's Zestimate                     | float64   |
| transactiondate                  | Date of the property transaction                                  | object    |
| airconditioningtypeid             | Type of air conditioning system                                   | float64   |
| architecturalstyletypeid          | Type of architectural style                                       | float64   |
| basementsqft                      | Square footage of basement area                                  | float64   |
| bathroomcnt                       | Number of bathrooms                                              | float64   |
| bedroomcnt                        | Number of bedrooms                                               | float64   |
| buildingclasstypeid               | Type of building class                                           | float64   |
| buildingqualitytypeid             | Quality rating of the building                                   | float64   |
| calculatedbathnbr                 | Calculated number of bathrooms                                   | float64   |
| decktypeid                        | Type of deck                                                     | float64   |
| finishedfloor1squarefeet          | Square footage of finished floor 1                               | float64   |
| calculatedfinishedsquarefeet      | Calculated finished square footage of the property                | float64   |
| finishedsquarefeet12              | Finished square footage of the property (12)                      | float64   |
| finishedsquarefeet13              | Finished square footage of the property (13)                      | float64   |
| finishedsquarefeet15              | Finished square footage of the property (15)                      | float64   |
| finishedsquarefeet50              | Square footage of finished floor 50                               | float64   |
| finishedsquarefeet6               | Square footage of finished floor 6                                | float64   |
| fips                             | Federal Information Processing Standards (FIPS) code for the county| float64   |
| fireplacecnt                      | Number of fireplaces                                             | float64   |
| fullbathcnt                       | Number of full bathrooms                                         | float64   |
| garagecarcnt                      | Number of garage spaces                                          | float64   |
| garagetotalsqft                   | Total square footage of garages                                   | float64   |
| hashottuborspa                    | Whether the property has a hot tub or spa                         | float64   |
| heatingorsystemtypeid             | Type of heating or cooling system                                | float64   |
| latitude                          | Latitude coordinates of the property                              | float64   |
| longitude                         | Longitude coordinates of the property                             | float64   |
| lotsizesquarefeet                 | Square footage of the lot                                        | float64   |
| poolcnt                           | Number of pools on the property                                  | float64   |
| poolsizesum                       | Total pool square footage                                        | float64   |
| pooltypeid10                      | Type 10 pool                                                     | float64   |
| pooltypeid2                       | Type 2 pool                                                      | float64   |
| pooltypeid7                       | Type 7 pool                                                      | float64   |
| propertycountylandusecode         | County land use code                                             | object    |
| propertylandusetypeid             | Type of land use for the property                                | float64   |
| propertyzoningdesc                | Description of property zoning                                    | object    |
| rawcensustractandblock            | Raw census tract and block identifier                            | float64   |
| regionidcity                      | City identifier                                                  | float64   |
| regionidcounty                    | County identifier                                                | float64   |
| regionidneighborhood              | Neighborhood identifier                                          | float64   |
| regionidzip                       | ZIP code of the property                                         | float64   |
| roomcnt                           | Number of rooms                                                  | float64   |
| storytypeid                       | Type of story (e.g., basement, attic)                            | float64   |
| threequarterbathnbr               | Number of three-quarter bathrooms                                | float64   |
| typeconstructiontypeid            | Type of construction material used                               | float64   |
| unitcnt                           | Number of units on the property                                  | float64   |
| yardbuildingsqft17                | Square footage of yard building (17)                              | float64   |
| yardbuildingsqft26                | Square footage of yard building (26)                              | float64   |
| yearbuilt                         | Year the property was built                                      | float64   |
| numberofstories                   | Number of stories in the property                                 | float64   |
| fireplaceflag                     | Flag indicating the presence of a fireplace                       | float64   |
| structuretaxvaluedollarcnt        | Assessed value of the property structure in dollars               | float64   |
| taxvaluedollarcnt                 | Assessed property value in dollars                                | float64   |
| assessmentyear                    | Year of property assessment                                      | float64   |
| landtaxvaluedollarcnt             | Assessed value of the land in dollars                             | float64   |
| taxamount                         | Property tax amount in dollars                                    | float64   |
| taxdelinquencyflag                | Flag indicating tax delinquency                                   | object    |
| taxdelinquencyyear                | Year of tax delinquency                                           | float64   |
| censustractandblock               | Census tract and block identifier                                 | float64   |
| propertylandusedesc               | Description of property land use                                  | object    |

This data dictionary includes the column names, descriptions, and data types for the columns in the dataset. You can use this dictionary as a reference to understand the dataset's structure and variables.

#### How to reproduce the project
* Bulleted item 1
    * Bulleted subitem 1
* Bulleted item 2
***
1. Ordered item 1  
    1.1. Ordered subitem 1  
2. Ordered item 2
***
- [ ] Unchecked box
- [x] Checked box

#### Key Findings:
