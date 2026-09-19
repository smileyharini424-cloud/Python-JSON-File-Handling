import json

filename = "student.json"

student = {
    "name": "Harini",
    "age": 20,
    "course": "CSE",
    "city": "Hyderabad"
}

with open(filename, "w") as file:
    json.dump(student, file, indent=4)

with open(filename, "r") as file:
    data = json.load(file)

print("Student Details:")
print("Name:", data["name"])
print("Age:", data["age"])
print("Course:", data["course"])
print("City:", data["city"])
