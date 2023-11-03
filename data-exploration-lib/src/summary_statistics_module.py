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

# Example usage:
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, None, 3, 5],  # Inserting a missing value for demonstration
    'C': [5, 4, 3, 2, 1]
})

summary_stats = SummaryStatistics(data)

# Calculating summary statistics
mean = summary_stats.calculate_mean()
median = summary_stats.calculate_median()
mode = summary_stats.calculate_mode()
std_dev = summary_stats.calculate_standard_deviation()
variance = summary_stats.calculate_variance()
quartiles = summary_stats.calculate_quartiles()

# Summarizing missing values
missing_summary = summary_stats.summarize_missing_values()

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Quartiles:")
print(quartiles)
print("Missing Values Summary:")
print(missing_summary)
