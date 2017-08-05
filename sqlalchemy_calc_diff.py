
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select, func, desc


def n():
    """ Function to add a number to each output """
    count = 0
    for i in str(count):
        print(str(i) + '\n')
        count += 1


metadata = MetaData()

engine = create_engine(
    'postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')
engine = create_engine('sqlite:///census.sqlite')

connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

print(census.columns.keys())

stmt = select([census.columns.age, (census.columns.pop2008 -
                                    census.columns.pop2000).label('pop_change')])

stmt = stmt.group_by(census.columns.age)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(5)
results = connection.execute(stmt).fetchall()
print(results)

from sqlalchemy import case

stmt = select([
    func.sum(
        case([
            (census.columns.state == 'New York',
             census.columns.pop2008)
        ], else_=0))])
results = connection.execute(stmt).fetchall()
print(results)

from sqlalchemy import case, cast, Float

stmt = select([
    (func.sum(
        case([
            (census.columns.state == 'New York',
             census.columns.pop2008)
        ], else_=0)) /
        cast(
            func.sum
            (census.columns.pop2008),
            Float) * 100).label('ny_percent')
])

results = connection.execute(stmt).fetchall()
print(results)
