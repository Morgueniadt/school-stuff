import pandas as pd
import matplotlib.pyplot as plt
# 
# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# columns = ["name", "position"]
# df = pd.read_csv("SnakesLadders.csv", usecols=columns)
# print("Contents in csv file:", df)
# plt.plot(df.name, df.position)
# plt.show()


# Initialize the lists for X and Y
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