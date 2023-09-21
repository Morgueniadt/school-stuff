import random
import time
finish = 100
spaceBewtweenMesages = 1
introMessage = 5
player1Place = 0
player2Place = 0

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
 
time.sleep(introMessage)

player1name = input("please input player one name :")
time.sleep(spaceBewtweenMesages)



player2name = input("please input player two name :")
time.sleep(spaceBewtweenMesages)
     
print("\nThis match will be played by Player 1", player1name , " and Player 2", player2name)

time.sleep(spaceBewtweenMesages)
dice_value = random.randint(1, 6)
print("Its a " + str(dice_value))
