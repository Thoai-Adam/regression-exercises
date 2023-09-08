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
