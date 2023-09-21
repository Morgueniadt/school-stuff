# def countDownRec(n):
#         if n<=0:
#             print("end")
#         else:
#             print(n)
#             countDownRec(n-1)
#             
# countDownRec(5)

def factorial(numIn):
    if numIn > 1:
        solution = numIn * factorial (numIn - 1)
        return solution
    else:
        return 1

userInput = int(input("what number would you like to input:")) 
ans = factorial(3)

print(ans)