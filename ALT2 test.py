# fifa 1 using pandas

import statistics
import pandas


df = pandas.read_csv('apple1.csv')

category = df['Category']
iphone = df ['iPhone']
YOY_growth = df['YOY_growth']

print(category,iphone,YOY_growth)