#my Stats and Hypotheses
import csv

with open("information.csv", "r") as file:
    students = list(csv.reader(file))
    print(students)
             
    for student in students:

     print("Name:", student[0],"\tSurname:", student[1], "\tAge:", student[2], "\Win:", student[3], "\time:", student[4])
    