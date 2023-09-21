binaryNum = input("enter 8bit binary number here")
print(binaryNum[7])

if binaryNum[7] == "0" :
    print("even")
else:
    print("odd")

num1 = int(binaryNum[0]) * 128
num2 = int(binaryNum[1]) * 64
num3 = int(binaryNum[2]) * 32
num4 = int(binaryNum[3]) * 16
num5 = int(binaryNum[4]) * 8
num6 = int(binaryNum[5]) * 4
num7 = int(binaryNum[6]) * 2
num8 = int(binaryNum[7]) * 1

print(num1+num2+num3+num4+num5+num6+num7+num8)