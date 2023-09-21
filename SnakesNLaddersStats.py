#Snakes and Ladders My Statistics

#reading back from my File:
import csv # call in the CSV library to do the work in bgd
import pandas as pd
import matplotlib.pyplot as plt
import csv #import to use the csv module
gameModesList = []
rollsOverallList = []
FinalPosition = []
minutesList = []
secondsList = []
allgames = []

with open('snakesladders.csv', mode="r") as csv_file: # r is read
    reader = csv.reader(csv_file) 

    for item in reader:
#PUT EACH INDIVIDUAL COLUMN INTO ITS OWN LIST
        gameModesList.append(item[0])
        rollsOverallList.append(item[1])
        FinalPosition.append(item[2])
        minutesList.append(item[4])
        secondsList.append(item[5])

#get rid of headings
del gameModesList[0]
del rollsOverallList[0]
del FinalPosition[0]
del minutesList[0]
del secondsList[0]


#get a list of all game times
for i in range(len(minutesList)):
   gameTime = minutesList[i] + secondsList[i]
   allgames.append(gameTime)

#get the maxGameTime
maxGameTime = max(allgames)
#getMinGameTime
minGameTime = min(allgames)
print(maxGameTime)
print(minGameTime)

data = pd.read_csv('SnakesLadders.csv')
  
df = pd.DataFrame(data)
  
X = list(df.iloc[:, 2])
Y = list(df.iloc[:, 3])
  
# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.xlabel("players")
plt.ylabel("Number of dice rolls")  
# Show the plot
plt.show()
