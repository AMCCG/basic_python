import pandas as pd

# create a sample dataset with a categorical variable
data = {'color': ['red', 'green', 'blue', 'red', 'green']}
df = pd.DataFrame(data)

print(df)

# calculate the frequency of each category in the categorical variable
freq = df['color'].value_counts(normalize=True)

print(freq)

# replace each category with its frequency
df['color_freq'] = df['color'].map(freq)

# drop the original categorical variable
df = df.drop('color', axis=1)

# print the encoded data
print(df)