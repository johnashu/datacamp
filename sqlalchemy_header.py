
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select, func


def n():
    """ Function to add a number to each output """
    count = 0
    for i in str(count):
        print(str(i) + '\n')
        count += 1


metadata = MetaData()

engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

engine1 = create_engine('sqlite:///employees.sqlite')
connection = engine1.connect()
employees = Table('employees', metadata, autoload=True, autoload_with=engine1)

print(employees.columns.keys())
print(census.columns.keys())

