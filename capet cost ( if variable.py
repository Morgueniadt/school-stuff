roomL = int(input("room length:"))
roomW = int(input("room width:"))
carpetType = input("select your prefered carpet type")

basic = 5.50
standard = 10.00
luxury = 25.00

area = roomL * roomW

if carpetType == "basic":
    basicCost = (area * basic)
    print("basic cost", basicCost)
elif carpetType == "standard":
    standardCost = (area * standard)
    print("standard",standardCost)
else:
    luxuryCost = (area * luxury)
    print("luxury", luxuryCost)
