
def n():
    """ Function to add a number to each output """
    count = 0
    for i in str(count):
        print(str(i) + '\n')
        count += 1

from sqlalchemy import MetaData, create_engine

metadata = MetaData()
engine = create_engine('sqlite:///chapter5.sqlite')
connection = engine.connect()

from sqlalchemy import Table, Column, String, Integer

census = Table('census', metadata,
              Column('state', String(30)),
              Column('sex', String(1)),
              Column('age', Integer()),
              Column('pop2000', Integer()),
              Column('pop2008', Integer()),
              )

metadata.create_all(engine)

import csv

f = open('census.csv', newline='')
csv_reader = csv.reader(f)


values_list = []

for row in csv_reader:
    data = {'state': row[0], 'sex': row[1],
     'age': row[2], 'pop2000': row[3],
     'pop2008': row[4]}
    values_list.append(data)

from sqlalchemy import insert

stmt = insert(census)

results = connection.execute(stmt, values_list)
print(results.rowcount)

from sqlalchemy import select, func

stmt = select([census.columns.sex,
    (func.sum(census.columns.pop2008 * census.columns.age) /
    func.sum(census.columns.pop2008)
    ).label('average_age')
])

stmt = stmt.group_by(census.columns.sex)

results = connection.execute(stmt).fetchall()
for result in results:
    print(result.sex, result.average_age)


from sqlalchemy import case, cast, Float

stmt = select([census.columns.state,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2000)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2000), Float) * 100).label('percent_female')
])

stmt = stmt.group_by(census.columns.state)
results = connection.execute(stmt).fetchall()

for result in results:
    print(result.state, result.percent_female)

stmt = select([census.columns.state,
    (census.columns.pop2008 - 
    census.columns.pop2000).label('pop_change')
])

stmt = stmt.group_by(census.columns.state)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(10)

results = connection.execute(stmt).fetchall()

for result in results:
    print('{}:{}'.format(result.state, result.pop_change))
