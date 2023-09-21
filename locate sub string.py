name = input("please enter your full name")
name = name.capitalize()


spaceLoc = name.index(" ")
print(spaceLoc)

spacePlus = spaceLoc + 1

print(name[0:spaceLoc])
print(name[spaceLoc+1:])