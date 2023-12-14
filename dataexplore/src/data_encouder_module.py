import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class DataEncoder:
    def __init__(self, data):
        self.data = data
        self.label_encoder = LabelEncoder()
        self.one_hot_encoder = OneHotEncoder()

    def label_encode(self, column):
        """
        Apply Label Encoding to a specific column.
        """
        self.data[column] = self.label_encoder.fit_transform(self.data[column])

    def one_hot_encode(self, column):
        """
        Apply One-Hot Encoding to a specific column.
        """
        one_hot_encoded = pd.get_dummies(self.data[column], prefix=column)
        self.data = pd.concat([self.data, one_hot_encoded], axis=1)
        self.data.drop(column, axis=1, inplace=True)

    def ordinal_encode(self, column, mapping_dict):
        """
        Apply Ordinal Encoding to a specific column based on a provided mapping dictionary.
        """
        self.data[column] = self.data[column].map(mapping_dict)

# Example usage:
# Assuming 'df' is your DataFrame
data = {
    'ID': [1, 2, 3, 4, 5],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
    'Salary': [60000, 80000, 75000, 70000, 90000]
}

df = pd.DataFrame(data)
  
# Create an instance of DataEncoder
data_encoder = DataEncoder(df)

# Example of Label Encoding for the 'Gender' column
data_encoder.label_encode('Gender')

# Example of One-Hot Encoding for the 'City' column
data_encoder.one_hot_encode('City')

# Example of Ordinal Encoding for the 'Education' column
education_mapping = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
data_encoder.ordinal_encode('Education', education_mapping)

# Display the modified DataFrame
print(data_encoder.data)
