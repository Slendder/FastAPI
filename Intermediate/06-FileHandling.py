### File Handling ###

# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=15524

import xml
import csv
import json
import os

# .txt files
f = open('./Intermediate/MyFile.txt', 'w+')

f.write('Bautista\nPrieto\n15\nJavaScript, Python, C++')

print(f.read())
print(f.read(10))  # char length
print(f.readline())
for i in f.readlines():
    print(i)

f.write('\nAunque tambien me gusta Rust')

f.close()

with open("Intermediate/MyFile.txt", "a") as my_other_file:
    my_other_file.write('\nSwift')

# os.remove("./Intermediate/MyFile.txt")

# .json file

json_file = open('Intermediate/my_file.json', 'w+')

json_test = {
    "Name": "Bautista",
    "Surname": "Prieto",
    "Age": 15,
    "Skills": {
        "Frontend": [
            "JavaScript",
            "CSS",
            "HTML",
            "React",
        ],
        "Backend": [
            "Python",
            "Rust"
        ],
    }
}

json.dump(json_test, json_file, indent=4)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))

# .csv file

csv_file = open("Intermediate/myCSV.csv", "w+")

json_test = {
    "Name": "Bautista",
    "Surname": "Prieto",
    "Age": 15,
    "Skills": {
        "Frontend": [
            "JavaScript",
            "CSS",
            "HTML",
            "React",
        ],
        "Backend": [
            "Python",
            "Rust"
        ],
    }
}

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Name', 'Surname', 'Age'])
csv_writer.writerow(['Bautista', 'Prieto', '15'])
csv_writer.writerows(zip(json_test['Skills'].keys(), zip(*[json_test['Skills'][skill] for skill in json_test['Skills']])))  
data = json_test['Skills']
for skill in data:
    skills = data[skill]

csv_file.close()



with open("Intermediate/myCSV.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file Install module!

# .xml file
