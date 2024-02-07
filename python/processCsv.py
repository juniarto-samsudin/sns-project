import pandas as pd 

df  = pd.read_csv('data.csv')

myDate = df.iloc[:, 0]
myMsg = df.iloc[:, -1]

print(myMsg)