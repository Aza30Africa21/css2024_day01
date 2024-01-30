# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:04:09 2024

@author: Mokgadi Precious Mph
"""

# Variables

# valid variables
x = 50
age = 50
_age = 50
my_age = 50
mYagE = 50
my_age_2 = 50

# non valid names

2age = 50
my_age = 50


# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)


# Using Lists
age = [30,40,30,49,22,35,22,46,29,25,39]   
print(age)

# Lists indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
print(age[11])


# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)


# Storing Text
C2 = M
C3 = M
C4 = F
# cannot run because it  does not have open and close commas

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

# Gender list

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])
print(gender[-3])
print(gender[-7])


# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)
print(my_list[:])
my_list.append("pi")
print(my_list)
my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))
print(my_list[0:3])


person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'
print(person['phone'])


# Creating a DataFrame
import pandas as pd
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
print(df[df['age'] > 30])
print(df[1:4])


# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)

df['new_Mokgadi'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_Mokgadi'], inplace=True)
print(df)
