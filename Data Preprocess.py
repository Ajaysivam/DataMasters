import pandas as  pd
import csv

dt=pd.read_csv("C:\\Users\\91887\\Desktop\\recession.csv")
dt['Percentage']=dt['Percentage'].interpolate(method='linear')
dt['Funds_Raised']=dt['Funds_Raised'].interpolate(method='linear')
dt['Census Count']=dt['Census Count'].interpolate(method='linear')

df=pd.DataFrame(dt)
output='C:\\Users\\91887\\Desktop\\procdata.xlsx'
df.to_excel(output,index=False)
