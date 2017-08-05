
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

engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

print(census.columns.keys())

stmt = select([census.columns.state, func.count(census.columns.age)])
stmt = stmt.group_by(census.columns.state)
results = connection.execute(stmt).fetchall()

print(results)
n()
print(results[0].keys())
n()


pop2008_sum = func.sum(census.columns.pop2008).label('population')
stmt = select([census.columns.state, pop2008_sum])
stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()
print(results)
n()
print(results[0].keys())
n()

df = pd.DataFrame(results)

df.columns = results[0].keys()
print(df)

df[10:20].plot.barh()
plt.show()

df.plot.bar()
plt.show()
