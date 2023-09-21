# import statistics
# import pandas
# counter = 0
# sumWages = 0
# 
# df = pandas.read_csv('FIFA.csv')
# 
# playerNationality = df['nationality']
# name = df['long_name']
# wage = df['wage_eur']
# 
# meanWages = statistics.mean(wage)
# print("the mean using the formula is", meanWages)
# 
# maxId = df[['wage_eur']].maxId()
# 
# # for i in range(len(wage)):
# #     meanWages += wage[i]
# #     
# # print("the mean is", meanWages / len(wage))
# # print(sumWages)
# 
# print("the highest earning player is", namemaxId = [df[['wage_eur']].idmax()])
# print("he earns", wage[maxId])
# print("he is from", playerNationality[maxId])
# 
# for i in range(100):
#     print(playerNationality[i], name[i], wage[i])
#     
#     
# useful_columns = ['nationality','long_name','wage_eur']
# df[useful_columns].to_csv('new.csv', index=False)

# Using pandas - recommended for larger files
import statistics
import pandas
import matplotlib.pyplot as plt
counter = 0
sumWages = 0
# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('FIFA.csv')
playerNationality = df['nationality']
ListPlayerNationality = playerNationality.tolist()
print(ListPlayerNationality)

name = df['long_name']
wage = df['wage_eur']

info = df.values.tolist()
print(info)

maxWage = max(wage)
print(maxWage)

minWage = min(wage)
print(minWage)

listWage = [maxWage, meanWages, minWage]
print(listWage)
