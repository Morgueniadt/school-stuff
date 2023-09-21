import random
import time
import sys
def introMsg():
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
    
#initialising variables
finishGame = 100
spaceBewtweenMesages = 1
introMessage = 5
player1Place = 0
player2Place = 0
# oldValue = 0
# currentValue = 0
playerName = " "
DICE = 6
pl1=""
pl2=""


#snakes dictionaires,definfing where snakes go
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
# ladders dictionaries , deifning where ladders go
ladders = {
    1: 100,
    2: 100,
    3: 100,
    4: 100,
    5: 100,
    6: 100,
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
   
def playerName(): # called second
    player1name = None
    while not player1name:
         player1name = input("please input player one name :")

    player2name = None
    while not player2name:
         player2name = input("please input player two name :")

    print("\nThis match will be played by Player 1", player1name , " and Player 2", player2name)
    return player1name, player2name



def diceRoll(): # called third
    time.sleep(spaceBewtweenMesages)
    dice_value = random.randint(1, DICE)
#     print(dice_value)
#     print(type(dice_value))
    print("Its a " + str(dice_value))
    return dice_value
    

def snakeBite(oldValue, currentValue, playerName):
    print(snakeBite)
    print("\n", playerName ," got bit by a snake and moved down from", str(oldValue)  ," to ", str(currentValue))
    
def ladderClimbed(oldValue, currentValue, playerName):
    print(ladderClimbed)
    print("\n", playerName ," found a ladder and climbed from", str(oldValue)  ," to ", str(currentValue))
    
def snakes_and_ladders(playerName,currentValue, dice_value): #fix
    time.sleep(spaceBewtweenMesages)
    oldValue = currentValue
   #player1Position = oldValue
   #player2Position = oldValue
    currentValue = oldValue + dice_value #fix def
    #print(type(currentValue))
    #print(currentValue)

    if currentValue > finishGame:#
        need= finishGame - currentValue
        print(f"You need {need} to win this game. Keep trying.")
        return oldValue
      
        
    print(f"\n {playerName} moved to {currentValue} from {oldValue}")
    #print(f"You need {need} to win this game. Keep trying.")
    if currentValue in snakes:
        FinalValue = snakes.get(currentValue)
        snakeBite(currentValue, FinalValue, playerName)
    
    elif currentValue in ladders:
      FinalValue = ladders.get(currentValue)
      ladderClimbed(currentValue, FinalValue, playerName)
     
    else:
        FinalValue = currentValue
        
    return FinalValue


# playerName = playerName()
#dice_value = diceRoll() # we have the right dice number here that was rolled


#currentValue = snakes_and_ladders(oldValue, currentValue, playerName, dice_value)
# print(currentValue)
# print(type(currentValue))
#currentValuentValue = int(currentValue)
# currentValue = snakes_and_ladders
# currentValuentValue = int(currentValue)

def checkWin(playerName, position):
    time.sleep(spaceBewtweenMesages)
    if finishGame == position:
        print("\n\n\nThats it.\n\n" + playerName + " won the game.")
        print("Congratulations " + playerName)
        
def playAgain(playerName, position):
    if finishGame == position:
        again = input("would you like to play again:")
    if again == "yes" or again == "Yes":
        start()
    elif again == "no" or again == "No":
        sys.exit(1)
        
def start():
    introMsg()
    #time.sleep(introMessage)
    player1name, player2name = playerName()
    #players = playerName()
    #print(type(players))
    
#     player1name = players[0] 
#     player2name = players[1]
    
    #print("P1", player1name)
    time.sleep(spaceBewtweenMesages)
        
    player1Position = 0
    player2Position = 0

    while True:
        time.sleep(spaceBewtweenMesages)
        print(player1name, end= "")
        input_1 = input("Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = diceRoll()
        time.sleep(spaceBewtweenMesages)
        print(player1name ," moving....")
       # here what happens
        player1Position = snakes_and_ladders(player1name, player1Position, dice_value)
       # do i ever get here
        checkWin(player1name, player1Position)

        print(player2name, end= "")
        input_2 = input("Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = diceRoll()
        time.sleep(spaceBewtweenMesages)
        print(player2name ," moving....")
        player2Position = snakes_and_ladders(player2name, player2Position, dice_value)
        checkWin(player2name, player2Position)
        playAgain(playerName, position)
# It Allows You to Execute Code When the File Runs as a Script
#if __name__ == "__main__":
start()

