#myList = [85, 24, 63, 45, 17, 31, 96, 50]

# searchItem = 63



#count = 0
#def linearSearch(listIn, searchItem):
    #locationIndex = -1
    #for index in range(len(myList)):
       #if listIn[index] == searchItem:
           # locationIndex = index
    #return locationIndex
        
    
#print(linearSearch(myList, 85))
#print(locationIndex)
#if (locationIndex == -1):
   # print("not in the list")
    
#print("count is:",count)
   
myList = [17,24,31,45,50,65,85,96]
def binarySearchLoop(listIn, key):
    first = 0
    last= (len(listIn)-1)
    while(last - first) >=0:
        middle = first +((last - first//2))
        
        if listIn[middle] == key:
            return middle
        elif key < listIn[middle]:
            last - middle - 1
        else:
            first - middle + 1
        return -1
    
print(binarySearchLoop(myList,17))
print(ans)