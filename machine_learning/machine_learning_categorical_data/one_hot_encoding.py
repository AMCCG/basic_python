import pandas as pd

# Creating a sample dataset with a categorical variable
data = {'color': ['red', 'green', 'blue', 'red', 'green']}
df = pd.DataFrame(data)

print(df)

# Performing one-hot encoding
one_hot_encoded = pd.get_dummies(df['color'], prefix='color')
print(one_hot_encoded)

# Combining the encoded data with the original data
df = pd.concat([df, one_hot_encoded], axis=1)

print(df)

# Drop the original categorical variable
df = df.drop('color', axis=1)

# Print the encoded data
print(df)