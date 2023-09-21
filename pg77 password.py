file = open("password.txt", "w")
file.write("621")


file = open("password.txt", "r")
dataIn = file.read()
file.close





# file = open("password.txt", "r")
#read back
savedPwd = dataIn
enterwhileLoop = 0

while enterwhileLoop == 0:
    password = input ('please enter password?')
    if password == savedPwd:
        print('you are in')
        enterwhileLoop = 1
        
    else:
        print('enter you password again')


file.close()
