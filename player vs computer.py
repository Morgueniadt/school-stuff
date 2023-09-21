# def introMsgPvAi():
#     msg = """
#      Welcome to Snake and Ladder Game.
#      
#          Rules:
#        1. Both player and Ai are at the starting position i.e 0
#           Take it in turns to roll the dice. 
#           Move forward the number of spaces shown on the dice.
#        2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
#        3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
#        4. The first player to get to the FINAL position is the winner.
#        5. Hit enter to roll the dice.
#      
# 
#      
#      """
#     print(msg)
# def PvAiName():
#    PvAiname1 = None
#    while not PvAiname1:
#          PvAiname1 = input("please input player one name :")
#          
#          print("Ai is ready")
# 
#          PvAiName2 = "Ai"
# 
#          print("\nThis match will be played by Player 1", PvAiname1 , " and Player 2", PvAiName2)
#          return PvAiname1, PvAiName2


def diceRoll(): 
    time.sleep(timeOut)
    diceValue = random.randint(1, 6)
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