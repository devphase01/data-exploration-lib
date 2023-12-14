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
