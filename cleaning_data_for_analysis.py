import pandas as pd

tips = pd.read_csv('tips.csv')

#convert data types
tips.sex = tips.sex.astype('category')
tips.smoker = tips.smoker.astype('category')
print(tips.info())


#comvert numberic data

tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')
print(tips.info())