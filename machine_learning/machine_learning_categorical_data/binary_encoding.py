import pandas as pd
import category_encoders as ce

# create a sample dataset with a categorical variable
data = {'color': ['red', 'green', 'blue', 'red', 'green']}
df = pd.DataFrame(data)

# create a binary encoder object and fit it to the data
binary_encoder = ce.BinaryEncoder(cols=['color'])
binary_encoder.fit(df['color'])

# transform the categorical variable using the binary encoder
encoded_data = binary_encoder.transform(df['color'])

# merge the encoded variable with the original dataframe
df = pd.concat([df, encoded_data], axis=1)

# print the encoded data
print(df)
