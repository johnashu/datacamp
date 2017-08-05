
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sqlalchemy import MetaData, Table, create_engine, select, func, and_


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
print(engine1.table_names())

connection = engine1.connect()
employees = Table('employees', metadata, autoload=True, autoload_with=engine1)
extra_employees = Table('extra_employees', metadata, autoload=True, autoload_with=engine1)

#print(employees.columns.keys())
#print(census.columns.keys())
print(extra_employees.columns.keys())

from sqlalchemy import delete

stmt = select([
    func.count(extra_employees.columns.name)
])

connection.execute(stmt).scalar()
delete_stmt = delete (extra_employees)
result_proxy = connection.execute(delete_stmt)
print(result_proxy.rowcount)

stmt = delete(employees).where(employees.columns.id == 3)

result_proxy = connection.execute(stmt)
print(result_proxy.rowcount)


#extra_employees.drop(engine)
#print(extra_employees.exists(engine))

#metadata.drop_all(engine)
#print(engine.table_names)


from sqlalchemy import delete, select

stmt = delete(census)


results = connection.execute(stmt)

print(results.rowcount)

stmt = select([census])

print(connection.execute(stmt).fetchall())


stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

to_delete = connection.execute(stmt).scalar()

stmt_del = delete(census)

stmt_del = stmt_del.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

results = connection.execute(stmt_del)
print(results.rowcount, to_delete)

