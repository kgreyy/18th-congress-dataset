from pandas_profiling import ProfileReport
import pandas as pd
import matplotlib
matplotlib.use('Agg')
df = pd.read_csv('congress_bill_association_eda.csv', encoding='utf-8', low_memory=False)
profile = ProfileReport(df)
profile.to_file("Analysis.html")