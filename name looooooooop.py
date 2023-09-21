# def playerName():
#     while True:
#         player1name = input("please input player one name :")
#         player2name = input("please input player two name :")
#         if player1name and player2name == "" :
#             print("\nThis match will be played by Player 1", player1name , " and Player 2", player2name)   
#         else:
#             break;
# playerName()

def playerName():
    player1name = None
    while not player1name:
         player1name = input("please input player one name :")

    player2name = None
    while not player2name:
         player2name = input("please input player two name :")

    print("\nThis match will be played by Player 1", player1name , " and Player 2", player2name)
    return player1name, player2name

playerName()