#insertion sort
#book page 215

#myList = [85,24,63,45,17,31,96,50]
myList = [9,7,6,15,17,10,11]
for index in range(1,len(myList)):
    print(myList)
    itemInsert = myList[index]
    position = index
    while position > 0 and myList [position - 1] > itemInsert:
        myList[position]=myList[position -1]
        position -= 1
        myList[position] = itemInsert
    
print(myList)