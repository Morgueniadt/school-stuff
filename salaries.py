import csv

with open("usasalaries.csv","r", newline="") as file:
    workerData = list(csv.reader(file))

numFemale = 0
numMale = 0

femaleGT50 = 0
maleGT50 = 0

for instance in workerData:

    if instance[9] == "Female":
        numFemale += 1
        if instance[14] == ">50K":
            femaleGT50 += 1
    else:
        numMale += 1
        if instance[14] == ">50K":
            maleGT50 += 1

print("Female :", numFemale, "\n\t>50K :", femaleGT50, "\t->", round(femaleGT50/numFemale*100,2),"%")
print("Male :", numMale, "\n\t>50K :", maleGT50, "\t->", round(maleGT50/numMale*100,2), "%")