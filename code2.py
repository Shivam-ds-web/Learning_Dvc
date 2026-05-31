import pandas as pd
import os
data = {
    'Name' : ['Charlie','Sam','John'],
    'Salary' : [20000,30000,40000]
}
dataf = pd.DataFrame(data)
os.makedirs('data2',exist_ok= True)
file_path = os.path.join('data2','sample.csv')
dataf.to_csv(file_path)
print('file Saved successfully')
os.makedirs('S3',exist_ok=True)
# makibng changes in data to check whether dvc is tracking data or not 
new_row = {'Name' : 'Yash','Salary' : 50000}
dataf.loc[len(dataf.index)] = new_row
dataf.to_csv(file_path)
new_row2 = {'Name' : 'Xyz','Salary' : 60000}
dataf.loc[len(dataf.index)] = new_row2
dataf.to_csv(file_path)
print(dataf)