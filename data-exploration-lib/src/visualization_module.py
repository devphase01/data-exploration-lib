import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizor:
  def __init__(self, df):
    """
    Initialize the DataVisualizor with a pandas DataFrame.
    """
    self.dataframe = df
  

  def plot_histogram(self, column, bins=10):
    """
    Plots a histogram for the specified column.
        
    Parameters:
    column (str): The column name for which to plot the histogram.
    bins (int): Number of bins for the histogram.
    """
    if column in self.dataframe.columns:
      self.dataframe[column].hist(bins=bins)
      plt.xlabel(column)
      plt.ylabel("Frequency")
      plt.title(f"Histogram of {column}")
      plt.show()
    else:
      raise ValueError(f"Column '{column}' not found in DataFrame.")
  

  def plot_scatter(self, x_column, y_column):
    if x_column in self.dataframe.columns and y_column in self.dataframe.columns:
      plt.scatter(self.dataframe[x_column], self.dataframe[y_column])
      plt.xlabel(x_column)
      plt.ylabel(y_column)
      plt.title(f"Scatter Plot of {x_column} vs {y_column}")
      plt.show()
    else:
      raise ValueError(f"One or both columns '{x_column}', '{y_column}' not found in DataFrame.")
    

  def plot_boxplot(self, column):
    """
    Plots a boxplot for the specified column.
    
    Parameters:
    column (str): The column name for which to plot the boxplot.
    """
    if column in self.dataframe.columns:
        sns.boxplot(x=self.dataframe[column])
        plt.title(f"Boxplot of {column}")
        plt.show()
    else:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

  def plot_correlation_matrix(self):
      """
      Plots a heatmap of the correlation matrix of the DataFrame.
      """
      corr_matrix = self.dataframe.corr()
      sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
      plt.title("Correlation Matrix Heatmap")
      plt.show()

iris = sns.load_dataset('iris')

# Assuming you have defined the DataVisualizor class as shown previously
visualizer = DataVisualizor(iris)

# Histogram of the sepal length
visualizer.plot_histogram('sepal_length')

# Scatter plot of sepal length vs. sepal width
visualizer.plot_scatter('sepal_length', 'sepal_width')

# Boxplot of petal length
visualizer.plot_boxplot('petal_length')

iris_numeric = iris.drop(columns='species')
visualizer = DataVisualizor(iris_numeric)

# Correlation matrix heatmap
visualizer.plot_correlation_matrix()
