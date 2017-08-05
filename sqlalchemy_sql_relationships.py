
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
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)
n()
print(engine.table_names())


stmt = select([census.columns.pop2008,
               state_fact.columns.abbreviation])

result = connection.execute(stmt).fetchall()
print(result[0:10])
"""
stmt = select([func.sum(census.columns.pop2008)])
stmt = stmt.select_from(census.join(state_fact))
stmt = stmt.where(state_fact.columns.circuit_court == '10')
results = connection.execute(stmt).scalar()
print(results)
"""

stmt = select([func.sum(census.columns.pop2000)])
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name))

stmt = stmt.where(
    state_fact.columns.census_division_name == 'East South Central'
)
results = connection.execute(stmt).scalar()

print(results)

stmt = select([func.count(census.columns.state.distinct())])
distinct_state_count = connection.execute(stmt).scalar()
print(distinct_state_count)


stmt = select([census.columns.state, func.count(census.columns.age)])
stmt = stmt.group_by(census.columns.state)
results = connection.execute(stmt).fetchall()
print(results)
print(results[0].keys())

pop2008_sum = func.sum(census.columns.pop2008).label('population')
stmt = select([census.columns.state, pop2008_sum])
stmt = stmt.group_by(census.columns.state)

results = connection.execute(stmt).fetchall()
print(results)
print(results[0].keys())

stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])
result = connection.execute(stmt).first()

for key in result.keys():
    print(key, getattr(result, key))



stmt = select([census, state_fact])
stmt = stmt.select_from(census.join(
    state_fact, census.columns.state == state_fact.columns.name))
result = connection.execute(stmt).first()
for key in result.keys():
    print(key, getattr(result, key))


stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008),
    state_fact.columns.census_division_name
])
stmt = stmt.select_from(
    census.join(state_fact, census.columns.state == state_fact.columns.name)
)

stmt = stmt.group_by(state_fact.columns.name)

results = connection.execute(stmt).fetchall()

for record in results:
    print(record)

"""
while results:
    partial_results = results_proxy.fetchmany(50)

    if partial_results == []:
        results = False

    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

results_proxy.close()
print(state_count)
"""