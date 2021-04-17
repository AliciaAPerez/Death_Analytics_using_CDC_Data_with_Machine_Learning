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

### Tableau (ADD GIFS LATER)
Ultimately, the objective is to identify the leading cause of death in the United States since 1999, and then identify the states with the highest deaths recorded. TThis analysis was broken down as see below.

#### Leading causes of Death
We used tableau to analyse the data and plot different visualizations as shown below.
For this part of the project we used the Center for Disease Control’s (CDC) National Center for Health Statistics (NCHS) data. The website has a  database of age-adjusted death rates and counts across the United States for the top 10 causes of death. Although the causes of deaths changed positions as they years went by (19999-2017), the 10 causes below reamined at the top.Below are the top 10 causes of death in the US:

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

#### States with the highest deaths and a map of the age adjusted death rates

We examined a trend at the state for the age adjested death rates. The minimum and maximum recorded  age rates across all states and years were used to compute the results and observe the changes over time. In the map below, orange represents the lowest death counts per age adjusted , while blue represents the highest. The cbar chart below the map represents the  top 10 states with the highest deaths recorded over time.

* California
* Florida
* Texas
*  New York


# Machine Learning 
"resident", "education", "sex", "age", "marital_status", "injury_at_work", "manner_of_death", "race", "hispanic"






