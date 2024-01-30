# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:20 2024

@author: Mokgadi Precious Mph
"""

"""
storing data in Python
1. Lists
2. Dictionaries
3. Data Frames - specific to pandas
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan

"""

age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]

print(age)

"""
[30, 25, 29, 46, 22]
"""

print(age[0])

"""
30
"""

print(age[1])

"""
25
"""

print(min(age))

"""
22
"""

print(max(age))


"""
46
"""


print(sum(age))


"""
152
"""


print(len(age))


"""
5
"""

"""
[30, 25, 29, 46, 22]
"""

avg = sum(age)/len(age)
print(avg)


"""
30.4
"""

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M","F","M"]

c1 = "South Africa"
c2 = "Lesotho"

print(age[0:3])

"""
[30, 25, 29, 46, 22]
"""

age.append(100)

print(age)

"""
[30, 25, 29, 46, 22, 100]

"""

mammals = {"cat":"a cute animal","lion":"king of the jungle","elephant":"a gigantic herbivore"}
print(mammals["cat"])

"""
a cute animal
"""
import pandas as pd

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes':Size_nm
    }





"""
df = dataframe
"""


import pandas as pd

df = pd.DataFrame.from_dict(fruit_sizes)

print(df['fruits'])
"""
0     apple
1    banana
2    orange
3     grape
4      kiwi
Name: fruits, dtype: object
"""

print(df['sizes'])
"""
0     9.8
1    10.1
2    13.2
3     8.7
4    20.5
Name: sizes, dtype: float64
"""

print(df['sizes'].min())
"""
8.7
"""

print(df['sizes'].mean())
"""
12.459999999999999
"""

print(df.describe())
"""
           sizes
count   5.000000
mean   12.460000
std     4.795102
min     8.700000
25%     9.800000
50%    10.100000
75%    13.200000
max    20.500000
"""

print(df["sizes"] > 10)
"""
0    False
1     True
2     True
3    False
4     True
Name: sizes, dtype: bool
"""

print = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace=True)
