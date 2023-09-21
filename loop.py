# counter = 1
# 
# while counter <= 10:
#     print("hello world")
#     counter +=1
#     
#     print("goodbye")
#     
#     counter = 1
# counter = 0
# 
# while counter <10:
#     print(counter)
#     counter +=1
#     
#     print("loop finished..")
#     
# counter = 1
# 
# while counter <11:
#     print(counter)
#     counter +=1
#     
#

# grade = int(input("what grade did you get"))

grade = int(input("grade please 1 - 100"))

while grade < 0 or grade> 100:
    grade = int(input("grade please use a number between 1 - 100"))
    
print(grade)
if grade >=90 and grade <101:
    print("H1")
elif grade >80 and grade <=89:
    print("H2")
elif grade >70 and grade <=79:
    print("H3")
elif grade >60 and grade <=69:
    print("H4")
elif grade >50 and grade <=59:
    print("H5")
elif grade >40 and grade <=49:
    print("H6")
elif grade >30 and grade <=39:
    print("H7")
elif grade >0 and grade <=29:
    print("H8")


