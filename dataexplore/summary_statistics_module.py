import pandas as pd

class SummaryStatistics:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        return self.data.mean()

    def calculate_median(self):
        return self.data.median()

    def calculate_mode(self):
        return self.data.mode().iloc[0]

    def calculate_standard_deviation(self):
        return self.data.std()

    def calculate_variance(self):
        return self.data.var()

    def calculate_quartiles(self):
        return self.data.quantile([0.25, 0.5, 0.75])

    def summarize_missing_values(self):
        return self.data.isnull().sum()
    
    def general_info(self):
        """
        Display general information about the dataset.
        """
        print("General Information:")
        print(self.data.info())
        print("\nNumber of Rows:", self.data.shape[0])
        print("Number of Columns:", self.data.shape[1])

    def summary_statistics(self):
        """
        Display summary statistics for each column in the dataset.
        """
        print("Summary Statistics:")
        summary_stats = self.data.describe(include='all')
        print(summary_stats)

    def missing_data(self):
        """
        Display information about missing data in the dataset.
        """
        print("Missing Data:")
        missing_data = self.data.isnull().sum()
        print(missing_data[missing_data > 0])

# # Example usage:
# data = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [2, 4, None, 3, 5],  # Inserting a missing value for demonstration
#     'C': [5, 4, 3, 2, 1]
# })

# summary_stats = SummaryStatistics(data)
# summary_stats.general_info()
# summary_stats.summary_statistics()
# summary_stats.missing_data()

# # Calculating summary statistics
# mean = summary_stats.calculate_mean()
# median = summary_stats.calculate_median()
# mode = summary_stats.calculate_mode()
# std_dev = summary_stats.calculate_standard_deviation()
# variance = summary_stats.calculate_variance()
# quartiles = summary_stats.calculate_quartiles()

# # Summarizing missing values
# missing_summary = summary_stats.summarize_missing_values()

# print("Mean:", mean)
# print("Median:", median)
# print("Mode:", mode)
# print("Standard Deviation:", std_dev)
# print("Variance:", variance)
# print("Quartiles:")
# print(quartiles)
# print("Missing Values Summary:")
# print(missing_summary)
