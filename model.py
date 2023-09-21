def theromostatModel(actual, target):
        if(actual < target):
           return 1
        else:
           return 0
        
tempOnOrOff = theromostatModel(20,20)
           
print(tempOnOrOff)