
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select, func, desc
from sqlalchemy import case, cast, Float


def n():
    """ Function to add a number to each output """
    count = 0
    for i in str(count):
        print(str(i) + '\n')
        count += 1


metadata = MetaData()
engine = create_engine(
    'mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
n()
print(engine.table_names())


stmt = select([
    func.sum(
        case([
            (census.columns.state == 'New York',
             census.columns.pop2008)
        ], else_=0))])
results = connection.execute(stmt).fetchall()
n()
print(results)


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
n()
print(results)



stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

stmt = stmt.group_by(census.columns.state)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(5)
results = connection.execute(stmt).fetchall()

for result in results:
    print('{}:{}'.format(result.state, result.pop_change))

n()

female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0)
)

total_pop2000 = cast(func.sum(census.columns.pop2000), Float)
stmt = select([female_pop2000 / total_pop2000 * 100])
percent_female = connection.execute(stmt).scalar()

print(percent_female)

