# import pandas as pd

# data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
#         'Age': [25, 30, 22, 35, 28], 
#         'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
#         'Salary': [50000, 55000, 40000, 70000, 48000]}

# df = pd.DataFrame(data)
# # Display the entire DataFrame
# print(df)

# # age_column=df['Age']
# # print(age_column)

# # columns = df[['Age','Name','Salary']]
# # print(columns)

# # data=df[df['Age']>25]
# # print(data)

# row = df.loc[[1,2]]
# print(row)


# import pandas as pd

# data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#          'Age': [27, 24, 22, 32],
#          'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#          'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
#          'Age': [17, 14, 12, 52],
#          'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#          'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# df = pd.DataFrame(data1)

# df1 = pd.DataFrame(data2)
# print(df)
# print(df1)

# frame = [df,df1]
# res=pd.concat(frame,ignore_index=True)
# print(res)


# import pandas as pd

# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# df = pd.DataFrame(data1,index=[0, 1, 2, 3])

# name = pd.Series([1000, 2000, 3000, 4000], name='Salary')

# print(df, "\n\n", name)

# res = pd.concat([df,name],axis=1)
# print(res)


import numpy as np
import pandas as pd

df = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'],
                            "Gender": ["", "", ""],
                            "Age": [0, 0, 0]})

df['Department'] = np.nan
print(df)
df.dropna(axis=1,inplace=True)
print(df)

df.replace("",np.nan,inplace=True)
print(df)
df.dropna(axis=1,inplace=True)
print(df)

df.replace(0,np.nan,inplace=True)
print(df)
df.dropna(axis=1,inplace=True)
print(df)