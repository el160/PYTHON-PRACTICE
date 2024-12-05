#Pandas provides a wide range of functions for reading and writing data to and from various file formats, including CSV, Excel, SQL databases, and more.
# It also provides functions for data cleaning, filtering, sorting, merging, and grouping.
# creating pandaas dataframe
import pandas as pd
data = {'Name': ['Tom', 'Nick', 'John'],
        'age':[34,76,32],
        'Origin':['Nyanza','Western','Nairobi']}
df = pd.DataFrame(data)
print(df)

#reading data from csv file
import pandas as pd
df = pd.read_csv('data.csv')
print(df)


#selecting data from a pandas dataframe
import pandas as pd
data = {'Name': ['Tom', 'Nick', 'John'],
        'age':[34,76,32],
        'Origin':['Nyanza','Western','Nairobi']}
df = pd.DataFrame(data)
print(df['name'])  #single column
print(df[['name','age']])#select multiple columns
print(df.loc[0])#select rows by index


                           #panda series
# A pandas Series is a one-dimensional labeled array of values.
# It is similar to a list or an array, but with the added benefit of having a label
import pandas as pd
d = [1,2,3,4]
var = pd.Series(d)
print(var)

                      #panda labels
# Labels are used to identify the values in a pandas Series.
# They can be any type of object, including strings, integers, or even other pandas Series.
import pandas as pd
print(var[0])


#creating panda labels
import pandas as pd
a = [1,2,3,4]
myvar = pd.Series (a,index= ['w','x','y','z'])
print(myvar)
  