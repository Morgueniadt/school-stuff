menu = 0

while menu != 3:
    print("*****Menu*****")
    print("1) Car Insurance")
    print("2) House Insurance")
    print("3) Exit")
    print("*"*15)
    
    menu = int(input("Option please:"))
    
    if menu == 1:
        print("Car")
    if menu == 2:
        print("Home")
    if menu == 3:
        print("bye, bye")