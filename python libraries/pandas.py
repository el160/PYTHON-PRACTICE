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
  
  
                 # loading data to a dataframe
import pandas as pd
df = pd.read_csv('data.csv')
print(df)


                      #CSV data frame
#deals with large sets of data
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

# we use the to_string() method to print the entire dataframe if not the first 5 rows and last 5 rows will be printed if the datarame is too large
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

# checking the maximum rows by pd.options.dispaly.max_rows statement
import pandas as pd
print(pd.options.display.max_rows) 


#increasing the number of rows to be displayed
import pandas as pd
pd.options.display.max_rows = 100
df = pd.read_csv("data.csv")
print(df)


                          #ANALYZING DATA FRAMES
#we use the head() method to view the first few rows of a dataframe and also we can specifiy the nmber of rows we want to view
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(5))

#we use the tail () method to view the last few rows of a dataframe and also we can specifiy the nm
# of rows we want to view
import pandas as pd
df = pd.read_csv('data.csv')
print(df.tail(5))

# we can use the info () method to view the summary of the dataframe
import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())


                            #CLEANING DATA
#cleaning data is fixing bad data in the data cell
#bad data could be empty,duplicate,wrong data ,data in wrong format
#removing rows that contain empty cells we use the dropna() function
import pandas as pd
df = pd.read_csv('data.csv') #or
df = pd.read_excel('cleaning.xlsx') # for excell data
new_df = df.dropna()
#removes rows with empty cells and wont change the original data frame
print(new_df.to_string())

# if you want to change the original data fram use inplace=true
import pandas as pd
df = pd.read_csv('data.csv') #or
df = pd.read_excel('cleaning.xlsx') # for excell data
df.dropna(inplace=True) #removes rows with empty cells and changes the original data frame


#we use fillna() method add new items to empty cells so as we dont have to remove the entire row
import pandas as pd
df = pd.read_csv('data.csv') #or
df = pd.read_excel('cleaning.xlsx')
df.fillna(100,inplace=True)


#Replace Only For Specified Columns
#To only replace empty values for one column, specify the column name for the DataFrame:
#Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd
df = pd.read_csv('data.csv')
df = pd.read_excel('cleaning.xlsx')

df["Country"].fillna(130, inplace = True)


#Replace Using Mean, Median, or Mod
#Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
#Calculate the MEAN, and replace any empty values with it
import pandas as pd
df = pd.read_excel("cleaning.xlsx")
x = df['Country'].mean()
df['Country'].fillna(x, inplace=True)

#Calculate the MEDIAN, and replace any empty values with it
import pandas as pd
df = pd.read_excel("cleaning.xlsx")
x = df['Country'].median()
df['Country'].fillna(x, inplace=True)

#Calculate the MODE, and replace any empty values with it
import pandas as pd
df = pd.read_excel("cleaning.xlsx")
x = df['Country'].mode()
df['Country'].fillna(x, inplace=True)