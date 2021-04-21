# Leading Causes of Death in the US

![alt text](https://github.com/AliciaAPerez/Death_Analytics_using_CDC_Data_with_Machine_Learning/blob/main/Images/Backgroung%20image.jpg "Bacgkgroung")

## Goal
To analyse the distribution of death in the United States and investigate the trends at a micro level for each state.

## Background
According to data from the National Center for Health Statistics (NCHS), which is overseen by the Center for Disease Control (CDC), one of the leading causes of death in the United States is heart disease. The CDC provides data for each recorded death that occured on the US territory, including the causes of death, the age adjusted death rate, the location etc. For this project, we selected we selected among other datasets, the the age-adjusted death rates for the 10 leading causes of death in the United States. The objective of this project is to analyse the causes of deaths distribution across the leading states in the US and point out any trend that might among a certain demographic.In addition, we also want to be able to predict the death of an indivisual by using machine learning to create a model capable of understanding our data and rendering the information needed. The analysis also covers at a very micro level what variables significantly affect  life expectancy in the United States.Verified reporting of this data starts as early as  1999.

Americans die each year and the leading causes of death account for a large portion of mortality. This project aims at providing a visula representation of what the leading of causes of deaths are for Americans and which states have the highest number of deaths and what is the cause of death. Additionally, analysis also take a look at factors such as  age and population size for each state. The main purpose of the Heroku app is to provide an informative and straightforward representation of data on the leading causes of death to not only to educate but also to make people interested.

## Technologies Used
* Pandas
* Flask
* SQLAlchemy
* Postgres
* HTML
* CSS
* Bootstrap
* Heroku
* Google collab


By informing the common American about the leading causes of death in the United States, the hope is that more people will realize that there remains a high demand for research and support for preventative measures. 
For those who want more statistics and general information on American health, these are useful resources:

## Data Sources:
The primary source of data for this objective comes from the NCHS. This dataset contains information for the top 10 leading causes of death, and was used to identify heart disease as the leading cause.
* NCHS: https://data.cdc.gov/NCHS/NCHS-Leading-Causes-of-Death-United-States/bi63-dtpu. 
* Kaggle:https://www.kaggle.com/cdc/mortality
* Kaggle:https://www.kaggle.com/cdc/nchs-death-rates-and-causes-of-death
* Kaggle:https://www.kaggle.com/ronitf/heart-disease-uci
* Please see: https://wonder.cdc.gov/wonder/help/mcd-expanded.html
* https://www.cdc.gov/nchs/data/dvs/Multiple-Cause-Record-Layout-2019-508.pdf

## ETL Process
* Pyspark was utilized to clean data and create data frames
* Dataframes were connected to SQL using Postgres and a Death Database was created

## Data Routes
* Flask was used to created connection to the Postgres database
* Routes were used to query the database and create a dictionary

## Website Design
* Deployment: 
* Bootstrap was used to create a theme for the page

# Analysis

### Tableau 
Ultimately, the objective is to identify the leading cause of death in the United States since 1999, and then identify the states with the highest deaths recorded. 
We used tableau to analyse the data and plot different visualizations as shown below. This analysis was broken down as see below.


#### Age Adjusted Death Rate
Northern states like Minnesota and Dakota have lowest the age adjusted death rates. Southern states (Louisiana, Kentucky) have the highest heart disease death rates over the years and Wyoming is among the highest with suicide rate on the national level.

#### Leading causes of Death
As can be seen below, the leading cause of death in the United States  is heart disease, close behind is cancer followed by unintentional injuries.

* Heart Disease
* Cancer
*  Unintentional Injuries
* Chronic Lower Respiratory Disease (CLRD)
* Stroke
* Alzheimer’s Disease
* Diabetes
* Influenza & Pneumonia
* Kidney Disease
* Suicide

#### Top 10 leading causes of Death
The leading cause of death in the United States is heart disease and remained at the first position throughout the years. There are little changes in position between the other causes, but in general, these are the top 10 ranked: Heart Disease, Cancer, Unintentional Injuries, Chronic Lower Respiratory Disease (CLRD), Stroke, Alzheimer’s Disease, Diabetes, Influenza & Pneumonia, Kidney Disease, Suicide

# Machine Learning 

## Heart Disease Prediction 
Predict whether a patient should be diagnosed with Heart Disease. Examine trends & correlations within our data. Determine which features are most important to Heart Disease diagnosis. We used Machine Learning algorithm where we can train our AI to learn & improve from experience. 

![alt text](/Images/heartdiseasemodel2.PNG "Heart Disease Prediction")


## Cause of Death Prediction

The Machine Learning for the cause of death utilized 2015 causes of death data from the CDC.  The data initially had over two million rows of data, but there were over 3,000 causes of death utilized. Some causes of death only had one entry, and they would not be very helpful. As a starting point, only the deaths with over 10,000 entires were utilized. That was 60 causes of death. Those were further grouped together by their kind. For example, lung cancer and breast cancer were listed as separate entities. Eventually, the data was whittled down to ten causes of death for this project. More could be done later once more refinement is gained with the machine learning model with using so much information. 

The following ten ICD codes were used (in order of frequency, with most frequent at the top and decreasing). 

1) I251: Heart Failure, Heart Attack, Heart Disease  
2) C349: Cancer  
3) J449: COPD  
4) F03: Dementia  
5) G309: Alzheimer's Disease  
6) J189: Pneumonia or other Lung Disease  
7) A419: Sepsis  
8) E149: Diabetes  
9) G20: Parkinson's Disease  
10) X44: Accidental Poisoning By and Exposure to Drugs and Other Biological Substances  

Keras was used to make the machine learning model. It was converted into a tensorflowjs file to be used in javascript to be brought to the website. 
After the data had been cleaned up and ready to be put into the model, there were 962411 rows of data. 721808 were used for training and 240603 for testing. 

The final model used layers 

(/Images/deathpred2.png)  
