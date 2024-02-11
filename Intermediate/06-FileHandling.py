### File Handling ###

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

json.dump(json_test, json_file)
