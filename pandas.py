# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:40:11 2024

@author: Mokgadi Precious Mph
"""


import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())
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

file = pandas.read_csv("iris.csv")

print(file)

print(file.info())

print(file.describe())
"""

     sepal_length  sepal_width  petal_length  petal_width         species
0             5.1          3.5           1.4          0.2     Iris-setosa
1             4.9          3.0           1.4          0.2     Iris-setosa
2             4.7          3.2           1.3          0.2     Iris-setosa
3             4.6          3.1           1.5          0.2     Iris-setosa
4             5.0          3.6           1.4          0.2     Iris-setosa
..            ...          ...           ...          ...             ...
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica
"""

file = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file)

print(file.info())

print(file.describe())

"""

"""

file = pandas.read_csv("diab_data.csv")
                      
print(file)

print(file.info())

print(file.describe())
"""
     preg_count  glucose  bp  skinfold  insulin   BMI  predigree  age  class
0             6      148  72        35        0  33.6      0.627   50      1
1             1       85  66        29        0  26.6      0.351   31      0
2             8      183  64         0        0  23.3      0.672   32      1
3             1       89  66        23       94  28.1      0.167   21      0
4             0      137  40        35      168  43.1      2.288   33      1
..          ...      ...  ..       ...      ...   ...        ...  ...    ...
763          10      101  76        48      180  32.9      0.171   63      0
764           2      122  70        27        0  36.8      0.340   27      0
765           5      121  72        23      112  26.2      0.245   30      0
766           1      126  60         0        0  30.1      0.349   47      1
767           1       93  70        31        0  30.4      0.315   23      0
"""

file = pandas.read_csv("housing_data.csv")

print(file)

print(file.info())
"""
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   0.00632  505 non-null    float64
 1   18       505 non-null    float64
 2   2.31     505 non-null    float64
 3   0        505 non-null    float64
 4   0.538    505 non-null    float64
 5   6.575    505 non-null    float64
 6   65.2     505 non-null    float64
 7   4.09     505 non-null    float64
 8   1        505 non-null    int64  
 9   296      505 non-null    float64
 10  15.3     505 non-null    float64
 11  396.9    505 non-null    float64
 12  4.98     505 non-null    float64
 13  24       451 non-null    float64
 
"""

print(file.describe())     
         
column_names =["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]

file = pandas.read_csv("housing_data.csv", names = ["A","B"])


       