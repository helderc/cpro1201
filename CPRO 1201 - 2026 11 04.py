
#           0       1       2
names = ["Alice", "Bob", "Alice"]

print(names[1])

for name in names:
    print(name)

#%%
print(type(names), type(names[1]))

print(names[0:2], len(names))

#%%

names.append("Charlie")
print(names)

#%%

names[0] = "Mary"
print(names)

#%%

names.remove("Charlie")
print(names)

#%%

grades = [10, 85, 23, 90, 100]

for grade in grades:
    print(grade)

print(sum(grades) / len(grades))

#%%

# Tuple

enrollment = (123, "CPRO1201")
print(enrollment[0])

student_id, course = enrollment
print(student_id, course)

#enrollment[0] = 666

#%%
var1 = "address"
tuple2 = (123, "CPRO1201", var1)
print(tuple2)

var1 = "asdasd"
print(tuple2)

#%%

# Sets

courses = ["CPRO1201", "CPRO2201", "CPRO1201"]
print(courses)

unique_courses = set(courses)
print(unique_courses)

tup2 = (1,3,4)
set2 = {1,3,4}
print(set(tup2))

#%%

items = []
while(...):
    
    item_name = ...
    value = ...
    items.append((item_name, value))

[   
 ( , ),
 ( , ),
 ( , )
]

#%%

courses = {"CPRO1201", "CPRO2201", "CPRO1201"}
print(courses)

print("CPRO2201" in courses)

print("Before")
for c in courses:
    if c == "CPRO2201":
        print(True)

#%%

#gA = {"Alice", "Bob", "Charlie"}
#gB = {"Bob", "David"}

gA = {1, 2, 3, 4}
gB = {6, 7, 2, 1}

print(gA)
print(gB)

print("union")
uAB = gA | gB
print(uAB)

print("intersection")
intAB = gA & gB
print(intAB)

print("Group A - B")
subAB = gA - gB
print(subAB)

#%%

print("Dictionary")

# key: value
student = {
      "id": 1234,
      "name": "Mary",
      "grade": 95
}
print(student)
print(type(student))

print(student["name"])

student["address"] = {
    "street": "This is my address",
    "number": 123,
    "code": 1123213908
}

print(student)

print(student.get("name", "It's not there"))

dict1 = {
    "key1": [1, 2, 4, 5]
}

print("\n\nStudent.Items")
for k, v in student.items():
    print(k, v)




































