myList =[ 85, 24, 55, 45, 22, 31, 96, 22]

searchItem = 22
locationIndex = -1

for index in range(len(myList)):
    if myList[index] == searchItem:
        locationIndex = index
        
print(locationIndex)

if(locationIndex == -1):
    print("not in the list")