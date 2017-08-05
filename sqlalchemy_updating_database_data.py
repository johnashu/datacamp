
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

from sqlalchemy import update, Table, Column, String, Integer, Float, Boolean

# Define a new table with a name, count, amount, and valid column: data
data = Table('extra_employees', metadata,
             Column('name', String(255)),
             Column('id', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Use the metadata to create the table
metadata.create_all(engine1)



"""

not retreving state_fact data

stmt = update(state_fact).values(notes='The Wild West')
stmt = stmt.where(state_fact.columns.census_name_region == 'West')

results = connnection.execute(stmt)

print(results.rowcount)


fips_stmt = select([state_fact.columns.name])
fips_stmt = fips_stmt.where(state_fact.columns.fips_state == flat_census.columns.fips_code)
update_stmt = update(flat_census).values(state_name=fips_stmt)
results = connection.execute(update_stmt)
print(results.rowcount)


"""