import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


class DistributionAnalyzer:
    def __init__(self, data, num_bins=20):
        """
        A class for analyzing data distribution.

        Parameters:
        - data (numpy.ndarray): Input data for distribution analysis.
        - num_bins (int): The number of bins for the histogram (20 by default).
        """
        self.data = data
        self.num_bins = num_bins

    def plot_histogram(self):
        """
        Plotting a histogram of data distribution.
        """
        plt.hist(self.data, bins=self.num_bins, color="blue", alpha=0.7)
        plt.title("Histogram of data distribution")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()

    def plot_probability_density_function(self):
        """
        Plotting the probability density function (PDF).
        """
        mu, std = norm.fit(self.data)
        plt.hist(self.data, bins=self.num_bins, density=True, color="blue", alpha=0.7)

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, "k", linewidth=2)

        title = "Approximation of the distribution: mu = %.2f, std = %.2f" % (mu, std)
        plt.title(title)
        plt.xlabel("Value")
        plt.ylabel("Probability density")
        plt.show()

    def plot_cumulative_distribution_function(self):
        """
        Plotting a cumulative distribution function (CDF).
        """
        sorted_data = np.sort(self.data)
        y = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

        plt.step(sorted_data, y, color="blue", where="mid")
        plt.title("Cumulative distribution function")
        plt.xlabel("Value")
        plt.ylabel("Probability")
        plt.show()

    def plot_qq_plot(self):
        """
        Plotting a Q-Q plot to check the normality of the distribution.
        """
        sorted_data = np.sort(self.data)
        theoretical_quantiles = norm.ppf(
            np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        )

        plt.scatter(theoretical_quantiles, sorted_data, color="blue", alpha=0.7)
        plt.title("Q-Q plot")
        plt.xlabel("Theoretical quantiles")
        plt.ylabel("Sorted data")
        plt.show()


"""
# Example of use:
# Create an instance of the DataDistributionAnalyzer class with input data and the number of bins
data_analyzer = DistributionAnalyzer(data=np.random.random(1000), num_bins=30)

# Building a histogram
data_analyzer.plot_histogram()

# Building a probability density function (PDF)
data_analyzer.plot_probability_density_function()

# Building a cumulative distribution function (CDF)
data_analyzer.plot_cumulative_distribution_function()

# Building a Q-Q graph
data_analyzer.plot_qq_plot()
"""
