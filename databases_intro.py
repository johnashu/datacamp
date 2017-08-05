
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select


def n():
    """ Function to add a number to each output """
    count = 0
    for i in str(count):
        print(str(i) + '\n')
        count += 1


metadata = MetaData()

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
print(engine.table_names())
n()
census = Table('census', metadata, autoload=True, autoload_with=engine)
print(census.columns.keys())
n()
print(repr(metadata.tables['census']))
n()
stmt = select([census])
#stmt = 'SELECT * FROM census'

results = connection.execute(stmt).fetchall()
#result_proxy = connection.execute(stmt)
#results = result_proxy.fetchall()


print(results[10:21])
n()
first_row = results[0]
print(first_row)
n()
print(first_row.keys())
n()
print(first_row.state)
n()


engine = create_engine(
    'postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

print(engine.table_names())
n()
stmt = select([census])

stmt = stmt.where(census.columns.state == 'California')
results_cal = connection.execute(stmt).fetchall()

for result in results_cal:
    print(result.state, result.age)
  

stmt = select([census])

stmt = stmt.where(census.columns.state.startswith('New'))

for result in connection.execute(stmt):
    print(result.state, result.pop2000)

stmt = select([census])

stmt = stmt.where(census.columns.state == 'New York')
results = connection.execute(stmt).fetchall()

for result in results:
    print(result.age, result.sex, result.pop2000)

"""
NO STATES COLUMN..

stmt = select([census])
print(stmt)
stmt =stmt.where(census.columns.state.in_(states))

for result in connection.execute(stmt):
    print(result.state, result.pop2000)
"""

from sqlalchemy import and_, or_


stmt = select([census])

stmt = stmt.where(
    and_(census.columns.state == 'California',
         census.columns.sex != 'M')
)

for result in connection.execute(stmt):
    print(result.age, result.sex)

stmt = select([census])

stmt = stmt.where(
    and_(census.columns.state == 'New York',
         or_(census.columns.age == 21,
             census.columns.age == 37
             )
         )
)

for result in connection.execute(stmt):
    print(result.age, result.state, result.sex)


stmt = stmt.order_by(census.columns.age)
results = connection.execute(stmt).fetchall()

print(results)

stmt = select([census.columns.state, census.columns.sex])
stmt = stmt.order_by(census.columns.state, census.columns.sex)

results = connection.execute(stmt).fetchall()

print(results[0:10])


from sqlalchemy import desc 

stmt = select([census.columns.state])

rev_stmt = stmt.order_by(desc(census.columns.state))

rev_results = connection.execute(rev_stmt).fetchall()

print(rev_results[:10])


stmt =select([census.columns.state, census.columns.age])

stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

results = connection.execute(stmt).fetchall()

print(results[:20])

from sqlalchemy import func

stmt = select([func.sum(census.columns.pop2008)])

results = connection.execute(stmt).scalar()
print(results)

stmt = select([census.columns.sex, 
    func.sum(census.columns.pop2008)])

stmt = stmt.group_by(census.columns.sex)

results = connection.execute(stmt).fetchall()
print(results)

stmt = select([census.columns.sex,
    census.columns.age,
    func.sum(census.columns.pop2008).label('Added')])

stmt = stmt.group_by(census.columns.sex,
    census.columns.age)

results = connection.execute(stmt).fetchall()
print(results[21:36])
print(results[0].keys())


stmt = select([func.count(census.columns.state.distinct())])
distinct_state_count = connection.execute(stmt).scalar()
print(distinct_state_count)
n()
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