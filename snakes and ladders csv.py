import csv

firstName = input("Please Enter your First Name:")
lastName = input("Please Enter your Last Name:")
age = int(input("Please enter age:"))

studentInfo = [firstName,lastName, age]

with open("information.csv", "a", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(studentInfo)
    
    

with open("information.csv", "r") as file:
    students = list(csv.reader(file))
     
    print(students)
     
    for student in students:

        print("Name:", student[0],"\nSurname:", student[1], "\nAge:", student[2])