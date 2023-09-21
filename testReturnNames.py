def playerName():
    player1name = input("please input player one name :")

    player2name = input("please input player two name :")
   # time.sleep(spaceBewtweenMesages)
    print("\nThis match will be played by Player 1", player1name , " and Player 2", player2name)
    return (player1name, player2name)

name = playerName()

print(type(name))
print(name)
print(name[0])
print(name[1])