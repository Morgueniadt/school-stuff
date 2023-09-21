# file = open ("myfirsttextfile2.txt","w")
# 
# file.write(" "+ name)
# 
# print("text file created")
# file.close()

# myData = open("myfirsttextfile2.txt","r")
# text = myData.read()
# myData.close()
# print(text)
# spaces = 0
# vowels = 0
# vowelsLi st = ["a", "e", "i", "o", "u" , "A", "E", "I", "O", "U",]
# 
# for character in text :
#     if character == " ":
#         spaces += 1
#     if vowelsList.__contains__(character):
#         vowels += 1
#         
# print(spaces)
# print(vowels)

file = open("myfilecsvdfile.csv", "w")
file.write("1,2,3,4,5")
file