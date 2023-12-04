import pandas as pd
import numpy as np

data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

### Question.1
columns = ['H', 'avg', 'HR', 'OBP']

for year in range(2015, 2019):
    print(year)
    years = data[data['year']==year]
    for col in columns:
        ind = years[col].nlargest(10).index
        print(data.loc[ind, ['batter_name', col]])
    print('\n')


### Question.2
years = data[data['year']==2018]
values = years['cp'].unique()
values = values[values != '지명타자']
values = np.sort(values)

for val in values:
    print(val)
    new_data = years[years['cp']==val]['war']
    ind = new_data.argmax()
    ind = new_data.index[ind]
    print(data.loc[ind, ['batter_name', 'war']])
    print('\n')
    
### Question.3
columns = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
feature = data[columns]
label = data['salary']

corr = feature.corrwith(label)

print('highest correlation: ' + corr.index[corr.argmax()])