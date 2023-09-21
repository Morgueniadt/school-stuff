import random
import time
import sys
import csv

   
   
def introMsgPvP():
    msg = """
     Welcome to Snake and Ladder Game.
     
         Rules:
       1. Initally both the players are at starting position i.e. 0. 
          Take it in turns to roll the dice. 
          Move forward the number of spaces shown on the dice.
       2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
       3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
       4. The first player to get to the FINAL position is the winner.
       5. Hit enter to roll the dice.
     
     """
    print(msg)
    
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),round(sec)))




#initialising variables
finishGame = 100
timeOut = 1
introMessage = 5
player1Place = 0
player2Place = 0
# oldPos = 
# currentPos = 
playerName = " "
pl1=""
pl2=""

firstName = input("Please Enter your First Name:")
lastName = input("Please Enter your Last Name:")
age = int(input("Please enter age:"))

studentInfo = [firstName,lastName, age]

with open("information.csv", "a", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(studentInfo)

simple_or_long = int(input("please select \n(1)simple\n(2)long\nenter your number choice:"))
if simple_or_long == 1:
    snakes = {
    26: 10,
    54: 36,
    60: 23,
    83: 45,
    85: 59,
    90: 48,
    97: 87,
}
    ladders = {
    3: 20,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    73: 86,
}

elif simple_or_long == 2:
    snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}
    ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}


 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def pvpName(): # called second
    playervs1Name = None
    while not playervs1Name:
         playervs1Name = input("please input player one name :").strip()

         playervs2Name = None
         while not playervs2Name:
             playervs2Name = input("please input player two name :").strip()

    print("\nThis match will be played by Player 1", playervs1Name , " and Player 2", playervs2Name)
    return playervs1Name, playervs2Name


def diceRoll(): # called third
    time.sleep(timeOut)
    diceValue = random.randint(1, 6)
#     print(diceValue)
#     print(type(diceValue))
    print("Its a " + str(diceValue))
    return diceValue
    

def snakeBite(oldPos, currentPos, playerName):
    (snakeBite)
    print("\n", playerName ," got bit by a snake and moved down from", str(oldPos)  ," to ", str(currentPos))
    
def ladderClimbed(oldPos, currentPos, playerName):
    (ladderClimbed)
    print("\n", playerName ," found a ladder and climbed from", str(oldPos)  ," to ", str(currentPos))
    
def s_n_l(playerName,currentPos, diceValue): #fix
    time.sleep(timeOut)
    oldPos = currentPos
    #pvp1Position = oldPos
    #pvp2Position = oldPos
    currentPos = oldPos + diceValue #fix def
    #print(type(currentPos))
    #print(currentPos)

    if currentPos > finishGame:#
        need= finishGame - oldPos
        print(f"You need {need} to win this game. Keep trying.")
        return oldPos
      
        
    print(f"\n {playerName} moved to {currentPos} from {oldPos}")
    if currentPos in snakes:
        FinalValue = snakes.get(currentPos)
        snakeBite(currentPos, FinalValue, playerName)
    
    elif currentPos in ladders:
      FinalValue = ladders.get(currentPos)
      ladderClimbed(currentPos, FinalValue, playerName)
     
    else:
        FinalValue = currentPos
        
    return currentPos


# playerName = playerName()
#diceValue = diceRoll() # we have the right dice number here that was rolled


#currentPos = s_n_l(oldPos, currentPos, playerName, diceValue)
# print(currentPos)
# print(type(currentPos))
#currentPosntValue = int(currentPos)
# currentPos = s_n_l
# currentPosntValue = int(currentPos)

def checkWin(playerName, position):
    time.sleep(timeOut)
    if finishGame == position:
        print("\n\n\nThats it.\n\n" + playerName + " won the game.")
        print("Congratulations " + playerName)
        end_time = time.time()
        time_lapsed = end_time - stopwatch
        time_convert(time_lapsed)

        snakesNLadders = [gameChoice,position,checkWin ,time_convert]

        with open("information.csv", "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(snakesNLadders)
                 
            sys.exit(1)

# #def playAgain():
#     if finalGame ==postion:
#         restart = input("would you like to platy again:")
#         if restart == "yes" or restart == "Yes":
#             start()
#         elif restart == "no" or restart == "No":
#             sys.exit(1)
        
def startPvP():
    introMsgPvP()
    time.sleep(introMessage)
    
    
    
    playervs1Name, playervs2Name = pvpName()
    #players = playerName()
    #print(type(players))
    
#     playervs1Name = players[0] 
#     playervs2Name = players[1]
    
    #print("P1", playervs1Name)
    time.sleep(timeOut)
        
    pvp1Position = 0
    pvp2Position = 0

    while True:
        time.sleep(timeOut)
        print(playervs1Name, end= "")
        input_1 = input("Hit the enter to roll dice: ")
        print("\nRolling dice...")
        diceValue = diceRoll()
        time.sleep(timeOut)
        print(playervs1Name ," moving....")
       # here what happens
        pvp1Position = s_n_l(playervs1Name, pvp1Position, diceValue)
       # do i ever get here
        checkWin(playervs1Name, pvp1Position)

        print(playervs2Name, end= "")
        input_2 = input("Hit the enter to roll dice: ")
        print("\nRolling dice...")
        diceValue = diceRoll()
        time.sleep(timeOut)
        print(playervs2Name ," moving....")
        pvp2Position = s_n_l(playervs2Name, pvp2Position, diceValue)
        checkWin(playervs2Name, pvp2Position)

 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def introMsgAivAi():
    msg = """
     Welcome to Snake and Ladder Game.
     
         Rules:
       1. Initally both the Ai's are at starting position i.e. 0. 
          They will take turns to roll the dice. 
          Move forward the number of spaces shown on the dice.
       2. If one lands at the bottom of a ladder, one can move up to the top of the ladder.
       3. If on lands on the head of a snake, one must slide down to the bottom of the snake.
       4. The first computer to get to the FINAL position is the winner.
    
     
     """
    print(msg)
    
def computerName():
    print("Ai.1 is ready")
    print("Ai.2 is ready")
    Comp1name = "Ai.1"
    Comp2name = "Ai.2"

    print("\nThis match will be played by Player 1", Comp1name , " and Player 2", Comp2name)
    return Comp1name, Comp2name


def diceRoll(): 
    time.sleep(timeOut)
    diceValue =  54 #random.randint(1, 6)
    print("Its a " + str(diceValue))
    return diceValue
    

def snakeBite(oldPos, currentPos, computerName):
    (snakeBite)
    print("\n", computerName ," got bit by a snake and moved down from", str(oldPos)  ," to ", str(currentPos))
    
def ladderClimbed(oldPos, currentPos, computerName):
    (ladderClimbed)
    print("\n", computerName ," found a ladder and climbed from", str(oldPos)  ," to ", str(currentPos))
    
def s_n_l(computerName,currentPos, diceValue): 
    time.sleep(timeOut)
    oldPos = currentPos
    currentPos = oldPos + diceValue 

    if currentPos > finishGame:
        need = finishGame - oldPos
        print(f"You need {need} to win this game. Keep trying.")
        return oldPos
      
        
    print(f"\n {computerName} moved to {currentPos} from {oldPos}")
    if currentPos in snakes:
        FinalValue = snakes.get(currentPos)
        snakeBite(currentPos, FinalValue, computerName)
    
    elif currentPos in ladders:
      FinalValue = ladders.get(currentPos)
      ladderClimbed(currentPos, FinalValue, computerName)
     
    else:
        FinalValue = currentPos
        
    return currentPos



def checkWin(computerName, position):
    time.sleep(timeOut)
    if finishGame == position:
        print("\n\n\nThats it.\n\n" + computerName + " won the game.")
        print("Congratulations " + computerName)
        end_time = time.time()
        time_lapsed = end_time - stopwatch
        time_convert(time_lapsed)

        snakesNLadders = [gameChoice,position,checkWin ,time_convert]

        with open("information.csv", "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(snakesNLadders)
                
            sys.exit(1)

def startComputer():
    introMsgAivAi()
    time.sleep(introMessage)
    
    Comp1name, Comp2name = computerName()

    time.sleep(timeOut)
        
    Comp1Position = 0
    Comp2Position = 0

    while True:
        time.sleep(timeOut)
        print("\nRolling dice...")
        diceValue = diceRoll()
        time.sleep(timeOut)
        print(Comp1name ," moving....")
        Comp1Position = s_n_l(Comp1name, Comp1Position, diceValue)
        checkWin(Comp1name, Comp1Position)

        print("\nRolling dice...")
        diceValue = diceRoll()
        time.sleep(timeOut)
        print(Comp2name ," moving....")
        Comp2Position = s_n_l(Comp2name, Comp2Position, diceValue)
        checkWin(Comp2name, Comp2Position)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def introMsgPvAi():
    msg = """
     Welcome to Snake and Ladder Game.
     
         Rules:
       1. Both player and Ai are at the starting position i.e 0
          Take it in turns to roll the dice. 
          Move forward the number of spaces shown on the dice.
       2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
       3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
       4. The first player to get to the FINAL position is the winner.
       5. Hit enter to roll the dice.
     

     
     """
    print(msg)
def PvAiName():
   PvAiname1 = None
   while not PvAiname1:
         PvAiname1 = input("please input player one name :")
         
         print("Ai is ready")

         PvAiName2 = "Ai"

         print("\nThis match will be played by Player 1", PvAiname1 , " and Player 2", PvAiName2)
         return PvAiname1, PvAiName2


def diceRoll(): 
    time.sleep(timeOut)
    diceValue =54  #random.randint(1, 6)
    print("Its a " + str(diceValue))
    return diceValue
    

def snakeBite(oldPos, currentPos, PvAiName):
    (snakeBite)
    print("\n", PvAiName ," got bit by a snake and moved down from", str(oldPos)  ," to ", str(currentPos))
    
def ladderClimbed(oldPos, currentPos, PvAiName):
    (ladderClimbed)
    print("\n", PvAiName ," found a ladder and climbed from", str(oldPos)  ," to ", str(currentPos))
    
def s_n_l(PvAiName,currentPos, diceValue): 
    time.sleep(timeOut)
    oldPos = currentPos
    currentPos = oldPos + diceValue 

    if currentPos > finishGame:
        need= finishGame - oldPos
        print(f"You need {need} to win this game. Keep trying.")
        return oldPos
      
        
    print(f"\n {PvAiName} moved to {currentPos} from {oldPos}")
    if currentPos in snakes:
        FinalValue = snakes.get(currentPos)
        snakeBite(currentPos, FinalValue, PvAiName)
    
    elif currentPos in ladders:
      FinalValue = ladders.get(currentPos)
      ladderClimbed(currentPos, FinalValue, PvAiName)
     
    else:
        FinalValue = currentPos
        
    return currentPos



def checkWin(PvAiName, position):
    time.sleep(timeOut)
    if finishGame == position:
        print("\n\n\nThats it.\n\n" + PvAiName + " won the game.")
        print("Congratulations " + PvAiName)
        end_time = time.time()
        time_lapsed = end_time - stopwatch
        time_convert(time_lapsed)
        

        snakesNLadders = [gameChoice,position,checkWin ,time_convert]

        with open("information.csv", "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(snakesNLadders)
                
            sys.exit(1)

def startPvAi():
    introMsgPvAi()
    time.sleep(introMessage)
    
    
    PvAiname1, PvAiName2 = PvAiName()

    time.sleep(timeOut)
        
    PvAi1Position = 0
    PvAi2Position = 0

    while True:
        time.sleep(timeOut)
        print(PvAiname1, end= "")
        input_1 = input("Hit the enter to roll dice: ") 
        print("\nRolling dice...")
        diceValue = diceRoll()
        time.sleep(timeOut)
        print(PvAiname1 ," moving....")
        PvAi1Position = s_n_l(PvAiname1, PvAi1Position, diceValue)
        checkWin(PvAiname1, PvAi1Position)

        print(PvAiName2, end= "")
        print("\nRolling dice...")
        diceValue = diceRoll()
        time.sleep(timeOut)
        print(PvAiName2 ," moving....")
        PvAi2Position = s_n_l(PvAiName2, PvAi2Position, diceValue)
        checkWin(PvAiName2, PvAi2Position)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
gameChoice = 1 #initialise the variable for while loop enetr


while gameChoice >=1 or gameChoice <=3:
   
    gameChoice = int(input("Would you like to play (1)Plaver versus Player or (2)watch the Ai or (3)play against the Ai ? :\n Please enter 1,2 or 3:"))
    stopwatch = time.time()
    
    #"play PvP"
    if gameChoice == 1:
        startPvP()
    #"watch the Ai"
    elif gameChoice == 2:
        startComputer()
    #Ai V Comp
    elif gameChoice == 3:
        startPvAi()



