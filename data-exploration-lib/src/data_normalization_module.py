import numpy as np
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    MaxAbsScaler,
    RobustScaler,
)


class DataScaler:
    def __init__(self, method="standard"):
        """
        A class for standardizing and normalizing data.

        Parameters:
        - method (str): The standardization/normalization method ('standard', 'minmax', 'maxabs', 'robust').
        """
        self.method = method
        self.scaler = self._get_scaler()

    def _get_scaler(self):
        if self.method == "standard":
            return StandardScaler()
        elif self.method == "minmax":
            return MinMaxScaler()
        elif self.method == "maxabs":
            return MaxAbsScaler()
        elif self.method == "robust":
            return RobustScaler()
        else:
            raise ValueError(f"Unsupported method: {self.method}")

    def fit_transform(self, data):
        """
        Calculates parameters and transforms data according to the selected method.

        Parameters:
        - data (numpy.ndarray): Input data for standardization/normalization.

        Returns:
        - numpy.ndarray: Transformed data.
        """
        return self.scaler.fit_transform(data)


"""
# Create an instance of the DataScaler class with a standardization method
>scaler = DataScaler(method="standard")

# Let's say we have data (numpy.ndarray)
>input_data = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

# Transforming data using the standardization method
>scaled_data = scaler.fit_transform(input_data)

# Displaying the result
>print(scaled_data)
[[-1.22474487 -1.22474487 -1.22474487]
[ 0.          0.          0.        ]
[ 1.22474487  1.22474487  1.22474487]]
"""
