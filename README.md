# Leading Causes of Death in the US


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
We used tableau to analyse the data and plot different visualizations as shown below.
For this part of the project we used the Center for Disease Control’s (CDC) National Center for Health Statistics (NCHS) data. The website has a  database of age-adjusted death rates and counts across the United States for the top 10 causes of death. Below are the top 10 causes of death in the US:

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

