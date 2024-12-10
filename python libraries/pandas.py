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


       #Cleaning Data of Wrong Format
#Cleaning data of wrong format is a common task in data cleaning. Here are some ways to do
#it:
#Remove leading and trailing whitespaces from a column
import pandas as pd
df = pd.read_csv('data.csv')
df['column_name'] = df['column_name'].str.strip()
#Remove leading and trailing whitespaces from all columns
import pandas as pd
df = pd.read_csv('data.csv')
df = df.apply(lambda x: x.str.strip())
#Remove leading and trailing whitespaces from a column and convert it to lower case
import pandas as pd
df = pd.read_csv('data.csv')
df['column_name'] = df['column_name'].str.strip().str.lower()
##can remove the entire row thats not matching up using dropna() method
import pandas as pd
df = pd.read_csv('data.csv')
df.dropna(subset=['column_name'], inplace=True)


       #Removing Duplicates
#we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row:
#To remove duplicates, use the drop_duplicates() method.

df.duplicated()
                             # Data Correlations
# pandas use corr () method to show relationship between two columns
# 1 to 1 means a perfect correlation ie if one value increases in one column another value increases in the other column
# 0.9 means a good correlation ie if one value increases in one column another value increases in the other column
# -0.9 sames 0.9 but if one value increases in one column another value decreases in the other column
#0.2 means a bad correlation in that increase of values in one colum does neccessarily mean increase of value in other column
# the corr() method avoids nun numeric values
df.corr ()


                      #pandas plotting
# we use plot() method to show visual representation of the the values
# we use pyplot a matpltlib module to show the visuals
#we use the kind method to specify which type of graph we want 
#we can also specifiy what should be on the x and y axis in the event of a graph that nedds both axis
import pandas as pd
import matplotlib.pyplot  as plt
df = pd.read_csv('data.csv')
df.plot()
plt.show()

    # scatter plot 
kind = 'scatter' 
x = 'duration'
y = 'calories'
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
df.plot(kind='scatter',x='duration',y='calories')
plt.show()


  # Histogram
kind = 'hist'
df['duration'].plot(kind='hist')








