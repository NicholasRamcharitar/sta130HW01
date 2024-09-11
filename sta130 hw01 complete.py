#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
HW01
Chat GPT Links:
https://chatgpt.com/share/5b6af6da-1bf0-4cc2-ad99-3a31b50d19dc
https://chatgpt.com/share/6c2436b4-59c6-4397-b47b-c89f247f3176


"""
import pandas as pd


# In[6]:


### Q1 
import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
missValCol = df.isna().sum()
missValTot = df.isna().sum().sum()
print("Missing Values in Columns")
print(missValCol)
print("Total Missing Values", missValTot)
# As We can see by the output, the data set has missing values


# In[9]:


### Q2 ** come back after chatgpt works
df.shape

df

"""
Since I was told I reached my data analysis limit for the day, I will print df and analyze 
them based on my understanding

Each Observation is a Villager in the game Animal Crossing

row_n seems to be the number of the row of the villager in game files
id is a simpified version of the villager's full_id, and seems like an abbreviated version of the name
name is the villager's name
gender is the villager's gender
species is the villager's species
Birthday is the villager's birth date in the form MM/DD
Song is the villager's favorite song or song associated with the villager
phrase is a catchphrase that the villager says 
full_id is probably what the villager is in the game files, starting with the villager-(name) 
url is a link to a picture of the villager

"""


# In[22]:


# Q3 
print(df.describe())
df['personality'].value_counts()

### clearly with the help of CHATGPT i can look at non numeric variables


# In[24]:


# Q4
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
print(df.shape)
print(df.describe())

### Shape reports 15 columns and 891 rows 
### Desrcibe shows only numerical variables, some of which are are represented as a numerical variable but are actually
### a true/false variable(Boolean) 


# # Q5
# """
# From what the chatbot says 
# shape is an attriubute, not a method so no ()s and prints out the dimensions of teh DF
# describe is aa method so ()s, which performs data analysis on the numerical variables of the DF
# """

# # Q6
# """
# Count is how much of the numerical variable is in the column
# Mean is the the total/num of observations aka the average
# STD is the standard deviation which is the mean distance from the mean
# MIN is the lowest value
# 25% is Q1(Quartile 1) which is the end of the first 25% of the data sorted in order from smallest to largest
# 50% is Q2 aka the median which is the middle number when the data is sorted small to large(if even number of 
# observations take the avg of the two middle numbers)
# 75% is Q3(Quartile 3) which is the end of 75% of the data sorted in order from smallest to largest
# MAX is the largest observations
# """

# In[8]:


#Q7
"""
df.dropna() might be peferred over using del df['col'] when for example you have a particular row you 
would like gone, or certain characteristics of a row you would like gone like a certain number of missing values
would determine if a row gets dropped or not or drop rows with any missing values or to only drop columns with missing
values

now del df['col'] might be preffered if you for example have an entire column that you know has missing rows or 
just do not want anymore.

using del df['col'] before df.dropna() could be important if you want to delete an unwanted column before trying to
remove columns with missing values

"""

import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
url2 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df2 = pd.read_csv(url)
#Let DF be the unchanged set and DF2 be the changed set
del df2['sibsp']
df2.dropna(inplace=True)
print(df2)
print(df)


# In[10]:


"""
Q8

8-1

df.groupby("col1")["col2"].describe() will group column 1 values together and then it will focus on grouping these 
by column 2 and describe will provide summary statistic data on it such as mean etc.

"""
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df.groupby("sex")["age"].describe()


# """
# 8-2
# describe looks at the entire dataset and groupby looks at 2 so the values would be different\
# """
# 

# In[1]:


"""
8-3
A
"""
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df

"""
The CHATGPT Response was Better and more starightforward than the google response that didnt straight up
tell me. A simple issue but  i prefer the chatbot(a)
"""


# In[3]:


"""
8-3
B
"""
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanics.csv"
df = pd.read_csv(url)
df
"""
the chatbot tells me that the url is wrong but i cannot find anything on google, so (a), gives me the correct answer
so (a)
"""


# In[7]:


"""
8-3 
C
"""
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)

DF.groupby("sex")["age"].describe()


"""
Again chatbot provides a clear and consiser explanation than google which is IF i can find a similar situation 
to the error so (a)

"""


# In[8]:


"""
8-3
D
"""
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url
                 
# chatbot tells me exact eror and how to fix it google does not have speccific solutions as the error message is vague and could mean anything
                 


# In[9]:


"""
8-3
E

"""
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df.group_by("sex")["age"].describe()

"""
Google and chatbot were equally good
i found a reddit post about the exact error with the underscore
and chat once again solved  it 
"""


# In[12]:


"""
8-3
F
"""
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df.groupby("sex")["age"].describe()


"""
Google does not tell me anything chat solves it again

"""


# In[ ]:


"""
8-3
G

"""
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
titanic_df.groupby(sex)["age"].describe()

"""
ChatGPT explains how i caused the error and google does not have the precision to tackle my error 
"""


# """
# 9
# 
# YES i have heavily relied on course textbook for this HW and chatbots,  
# not much piazza but i would say the lecture helped me 
# """

# In[ ]:




