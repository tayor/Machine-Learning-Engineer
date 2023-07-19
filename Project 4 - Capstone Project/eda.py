import pandas as pd
from pandas_profiling import ProfileReport
import os

if not os.path.exists('eda-reports'):
    os.mkdir('eda-reports')

files = [ 'Udacity_AZDIAS_052018', 'Udacity_CUSTOMERS_052018', 'Udacity_MAILOUT_052018_TEST', 'Udacity_MAILOUT_052018_TRAIN']

for i in range(len(files)):
    df = pd.read_csv('data/'+ files[i]+ '.csv', sep=';')
    profile = ProfileReport(df, title=str(files[i])+' Report', html={'style':{'full_width':True}})
    profile.to_file(output_file='eda-reports/'+str(files[i])+".html")