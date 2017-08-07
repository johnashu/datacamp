merge_by_city = pd.merge(revenue, managers, on='city')
print(merge_by_city)
merge_by_id = pd.merge(revenue, managers, on='branch_id')
print(merge_by_id)

combined = pd.merge(revenue, managers, left_on='city', right_on='branch')
print(combined)

revenue['state'] = ['TX','CO','IL','CA']


managers['state'] = ['TX','CO','CA','MO']


combined = pd.merge(revenue, managers, on=['branch_id', 'city', 'state'])

print(combined)



revenue_and_sales = pd.merge(revenue, sales, how='right', on=['city', 'state'])

print(revenue_and_sales)

sales_and_managers = pd.merge(sales, managers, how='left', left_on=['city', 'state'], right_on=['branch', 'state'])

print(sales_and_managers)



merge_default = pd.merge(sales_and_managers, revenue_and_sales)
print(merge_default)

merge_outer = pd.merge(sales_and_managers, revenue_and_sales, how='outer')

print(merge_outer)

merge_outer_on = pd.merge(sales_and_managers, revenue_and_sales, on=['city', 'state'], how='outer')
print(merge_outer_on)