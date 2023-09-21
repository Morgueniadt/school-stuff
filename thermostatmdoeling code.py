import csv

def ThermostatModel(actual, target):
    if(actual < target):
        return "On"
    else:
        return "Off"
    
# TempOnOrOff = ThermostatModel(3,20)
# print(TempOnOrOff)
# ThermostatModel(4,20)
# print(TempOnOrOff)

with open('temp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        tempOnOrOff = ThermostatModel(int(row[0]),int(row[1]))
        print(tempOnOrOff)
        
