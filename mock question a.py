#Question 16(a)
#Write your name here:

Gross_wages = int(input("Please enter your annual wages: ")) 

Tax_Credits = 1700
cutoff = 36800  

total_tax = (cutoff * 0.2) + ((Gross_wages - cutoff)* 0.4) - Tax_Credits
percentage_tax = total_tax/Gross_wages * 100
def income_tax(Gross_wages):
    print("Welcome to my income tax calculator")
    if Gross_wages <= 36800:
       print("you to pay no income tax") 
    elif Gross_wages >= 36800:
       print("you will have to pay income tax")
    print("your income tax bill is :", total_tax)
    print("the the percentage you lost to tax was:", round(percentage_tax,2),"%")

#Net_income = Gross_wages - Total_tax

income_tax(Gross_wages)       
