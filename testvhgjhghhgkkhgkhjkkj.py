oldValue = 0
dice_value= 4
currentValue = 0

for i in range(3):
    oldValue = currentValue
    currentValue = oldValue + dice_value #fix def
    print(currentValue)
    dice_value +=1


    #print(type(currentValue))
    #print(currentValue)