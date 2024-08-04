import pandas as pd
from sklearn.preprocessing import LabelEncoder

# create a sample dataset with a categorical variable and a target variable
data = {'color': ['red', 'green', 'blue', 'red', 'green'],
        'target': [1, 0, 1, 0, 1]}
df = pd.DataFrame(data)

# create a label encoder object and fit it to the data
label_encoder = LabelEncoder()
label_encoder.fit(df['color'])

# transform the categorical variable using the label encoder
df['color_encoded'] = label_encoder.transform(df['color'])

# create a mean encoder object and fit it to the transformed data
mean_encoder = df.groupby('color_encoded')['target'].mean().to_dict()
print(mean_encoder)

# map the mean encoded values to the categorical variable
df['color_encoded'] = df['color_encoded'].map(mean_encoder)

# print the encoded data
print(df)
