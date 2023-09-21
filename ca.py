# fName = input("what is your first name:")
# sName = input("what is your surname:")

# loanTerm = input("how many years are in your loan term:")
# loanAmount = input("what is your loan amount:")
# appReason = input("what is the reason for your application:")
#  
# cfName = fName.capitalize()
# csName = sName.capitalize()
# print( cfName, csName )
#

ans = False
 
while ans == False:
    pNumber = input("what is your PPS number:")
    if "M" in pNumber or "F" in pNumber:
        print("Kepp Going")
        ans = True
    else:
        print("Error, incorrect input")
 