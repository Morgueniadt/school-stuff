# #tennis 1 - read in the information from the CSV file
# import csv # import csv library
# with open('tennis.csv', 'r') as file: #  basic reaing of a csv file 
#     reader = csv.reader(file)
#    # next(reader) This code eliminates the first line
#     for row in reader:
#         print(row)

#tennis 1 - read in the information from the CSV file
import csv # import csv library
   
def playTennis(outlook, humidity, wind, temp = None):
    if outlook == "Overcast":
        return "Yes"
    elif outlook == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    else:
        if wind == "Strong":
            return "No"
        else:
            return "Yes"
        
overcastCounter = 0
sunnyCounter = 0

with open('tennis.csv', 'r') as file:
    reader = csv.reader(file)
   # next(reader) This code eliminates the first line
    for row in reader:
        print(row)
        print("row information")
        print(row[1],row[2],row[3], row[4])
        shouldIPlay = playTennis(row[1],row[2],row[3], row[4])
        #list the day in the final result
        print("day", row[0],shouldIPlay)
        

#calculations
#how many sunny days were there

        print(row)
        print("row information")
        print(row[1])
        if row[1] == "Overcast":
            overcastCounter +=1
        elif row[1] == "Sunny":
            sunnyCounter += 1
        else:
            pass

print("overcast Days", overcastCounter)
print("Sunny Days",sunnyCounter)