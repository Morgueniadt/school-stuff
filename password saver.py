correctPassword= 'Secret'
enterwhileLoop = 0

while enterwhileLoop == 0:
    password = input ('please enter password?')
    if password == correctPassword:
        print('you are in')
        enterwhileLoop = 1
        
    else:
        print('enter you password again')