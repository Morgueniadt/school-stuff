#question 16 A
#Aaron caffrey

password = "secret"
overwrite = "overwrite"

#the input variable takes an input from the user, in this scenario it is taking in a password 
myPassword = input("Enter your password:")

name = input("please enter your full name")
name = name.capitalize()
 
 
spaceLoc = name.index(" ")
 
print(spaceLoc)
 
spacePlus = spaceLoc + 1

print(name[0:spaceLoc])
print(name[spaceLoc+1:])

if myPassword == password:
    print("correct passowrd")
elif myPassword == overwrite:
    print("passowrd overwrite")
elif myPassword != password:
    for i in range(5):
        print("this is attempt""the password you entered:", myPassword ,",is incorrect, please try again")
        myPassword = input("Enter your password:")