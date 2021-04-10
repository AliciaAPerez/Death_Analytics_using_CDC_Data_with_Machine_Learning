import pandas as pd
import matplotlib.pyplot as plt
from dbconfig import USER, PASSWORD, ADDRESS, PORT, DATABASE
from sqlalchemy import create_engine
connection_string = (f'postgresql://{USER}:{PASSWORD}@{ADDRESS}:{PORT}/{DATABASE}')
def getdata():

    engine = create_engine(connection_string)
    cn = engine.connect()
    # List the following details of each employee: 
    #   employee number, last name, first name, sex, and salary.
    df = pd.read_sql('''
    select * from cdc_death_table limit 1000;''',
    cn)
    # print(df.values.tolist())
    cn.close()
    return str(df.values.tolist())