

class Student:
    # Q: we need to store 4 grades
    # DUNDER init    
    # constructor
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.grades = []            
    def __str__(self):
        return f"INFO: {self.name}, {self.address}: {self.grades_avg():.2f}"
    def grades_avg(self):
        return sum(self.grades) / len(self.grades)
#    def m1(self, ...):
#        return "fdgdfg"# + self.__str__()

# s --> an Object
s1 = Student("Mary", "11 Street")
s1.grades.append(78.9)
s1.grades.append(98.9)
s1.grades.append(12.0)

print(s1)
print(s1.grades)
print(s1.grades_avg())

#%%
g = []        
for i in range(4):
    g.append(float(input("Grade: ")))

s = Student("Mark", "10 Street", g)
    
    
#print(f"{s1.name}, {s1.address}, {s1.grade}")
print(s1)
#print(type(s1))

#%%
s2 = Student("Elith", "12 Street", 32)
#print(s2.name, s2.address, s2.grade)
print(s2)




