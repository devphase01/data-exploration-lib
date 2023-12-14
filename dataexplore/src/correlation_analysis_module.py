import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

class CorrelationAnalysis:
    def __init__(self, data):
        self.data = data

    def calculate_correlation(self):
        return self.data.corr()

    def generate_correlation_matrix(self):
        return self.data.corr()

    def visualize_correlation_matrix(self):
        plt.figure(figsize=(10, 8))
        correlation_matrix = self.data.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix Heatmap')
        plt.show()

    def calculate_pearson_correlation(self, x, y):
        pearson_corr, _ = pearsonr(self.data[x], self.data[y])
        return pearson_corr

    def calculate_spearman_correlation(self, x, y):
        spearman_corr, _ = spearmanr(self.data[x], self.data[y])
        return spearman_corr

    def test_correlation_significance(self, x, y):
        # Perform significance testing for correlation
        # You might need to handle cases for non-numeric columns
        if pd.api.types.is_numeric_dtype(self.data[x]) and pd.api.types.is_numeric_dtype(self.data[y]):
            pearson_corr, _ = pearsonr(self.data[x], self.data[y])
            spearman_corr, _ = spearmanr(self.data[x], self.data[y])
            return pearson_corr, spearman_corr
        else:
            return "Non-numeric columns. Cannot perform correlation significance testing."

# # Example usage:
# data = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 4, 6, 8, 10],
#     'C': [5, 4, 3, 2, 1]
# })

# correlation_analysis = CorrelationAnalysis(data)

# # Calculate correlation coefficients
# correlation_coefficients = correlation_analysis.calculate_correlation()
# print("Correlation Coefficients:")
# print(correlation_coefficients)

# # Generate correlation matrix
# correlation_matrix = correlation_analysis.generate_correlation_matrix()
# print("\nCorrelation Matrix:")
# print(correlation_matrix)

# # Visualize correlation matrix (heatmap)
# correlation_analysis.visualize_correlation_matrix()

# # Calculate Pearson correlation coefficient
# pearson_corr = correlation_analysis.calculate_pearson_correlation('A', 'B')
# print("\nPearson Correlation Coefficient between A and B:", pearson_corr)

# # Calculate Spearman correlation coefficient
# spearman_corr = correlation_analysis.calculate_spearman_correlation('A', 'B')
# print("Spearman Correlation Coefficient between A and B:", spearman_corr)

# # Test correlation significance
# correlation_significance = correlation_analysis.test_correlation_significance('A', 'B')
# print("\nCorrelation Significance Testing (Pearson, Spearman):", correlation_significance)
