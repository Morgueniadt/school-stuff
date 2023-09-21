def PvAiName():
   PvAiname1 = None
   while not PvAiname1:
         PvAiname1 = input("please input player one name :")
         
         print("Ai is ready")

         PvAiName2 = "Ai"

         print("\nThis match will be played by Player 1", PvAiname1 , " and Player 2", PvAiName2)
         return PvAiname1, PvAiName2


def diceRoll(): # called third
    time.sleep(spaceBewtweenMesages)
    dice_value = random.randint(1, DICE)
    print("Its a " + str(dice_value))
    return dice_value
    

def snakeBite(oldValue, currentValue, PvAiName):
    (snakeBite)
    print("\n", PvAiName ," got bit by a snake and moved down from", str(oldValue)  ," to ", str(currentValue))
    
def ladderClimbed(oldValue, currentValue, PvAiName):
    (ladderClimbed)
    print("\n", PvAiName ," found a ladder and climbed from", str(oldValue)  ," to ", str(currentValue))
    
def snakes_and_ladders(PvAiName,currentValue, dice_value): #fix
    time.sleep(spaceBewtweenMesages)
    oldValue = currentValue
    currentValue = oldValue + dice_value #fix def

    if currentValue > finishGame:#
        need= finishGame - currentValue
        print(f"You need {need} to win this game. Keep trying.")
        return oldValue
      
        
    print(f"\n {PvAiName} moved to {currentValue} from {oldValue}")
    if currentValue in snakes:
        FinalValue = snakes.get(currentValue)
        snakeBite(currentValue, FinalValue, PvAiName)
    
    elif currentValue in ladders:
      FinalValue = ladders.get(currentValue)
      ladderClimbed(currentValue, FinalValue, PvAiName)
     
    else:
        FinalValue = currentValue
        
    return FinalValue



def checkWin(PvAiName, position):
    time.sleep(spaceBewtweenMesages)
    if finishGame == position:
        print("\n\n\nThats it.\n\n" + PvAiName + " won the game.")
        print("Congratulations " + PvAiName)
        sys.exit(1)

def startPvAi():
    introMsg()
    time.sleep(introMessage)
    
    PvAiname1, PvAiName2 = PvAiName()

    time.sleep(spaceBewtweenMesages)
        
    PvAi1Position = 0
    PvAi2Position = 0

    while True:
        time.sleep(spaceBewtweenMesages)
        print(PvAiname1, end= "")
        input_1 = input("Hit the enter to roll dice: ") 
        print("\nRolling dice...")
        dice_value = diceRoll()
        time.sleep(spaceBewtweenMesages)
        print(PvAiname1 ," moving....")
       # here what happens
        PvAi1Position = snakes_and_ladders(PvAiname1, PvAi1Position, dice_value)
       # do i ever get here
        checkWin(PvAiname1, PvAi1Position)

        print(PvAiName2, end= "")
        print("\nRolling dice...")
        dice_value = diceRoll()
        time.sleep(spaceBewtweenMesages)
        print(PvAiName2 ," moving....")
        PvAi2Position = snakes_and_ladders(PvAiName2, PvAi2Position, dice_value)
        checkWin(PvAiName2, PvAi2Position)
 
startPvAi()

