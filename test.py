import pandas as pd
from dataexplore.src.summary_statistics_module import SummaryStatistics

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 1, 5, 4],
}

df = pd.DataFrame(data)

SummaryStatistics(df)
