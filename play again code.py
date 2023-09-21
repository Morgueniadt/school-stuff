playerName = "boxbot"
position = 100
finishGame = 100
def checkWin(playerName, position):
    #time.sleep(spaceBewtweenMesages)
    if finishGame == position:
        print("\n\n\nThats it.\n\n" + playerName + " won the game.")
        print("Congratulations " + playerName)
        again = input("would you like to play again:")
    if again == "yes" or "Yes":
        break


    checkWin(playerName, position)