import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dob_job_application_filings_subset.csv')
df_subset = pd.read_csv('dob_job_application_filings_subset.csv')


# anaylise
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df_subset.head())
print(df_subset.tail())

# analzye using .info()

print(df.info())

df1 = df.State.value_counts(dropna=False).head()
print(df1)

df2 = df.Paid.value_counts(dropna=False).head()
print(df2)

print(df['Borough'].value_counts(dropna=False))
print(df['State'].value_counts(dropna=False))
print(df['Site Fill'].value_counts(dropna=False))


# Data Visualisation


df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
plt.show()

# boxplots

df.plot(kind='scatter', x='Proposed Height', y='Existing Zoning Sqft', rot=70)
plt.show()


df.boxplot(column='Proposed Height', by='Existing Zoning Sqft', rot=90)
plt.show()


# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()


df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()


# Reshape Data Using Melt

