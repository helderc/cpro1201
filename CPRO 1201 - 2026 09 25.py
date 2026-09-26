
print(12, 25, 2026, sep="/")

#%%
print("string 1", end="\n------\n")
print("string 2", end=" ")
print("string 3 \n- string 4")

print("string A\tstring B")

print("string\ string2")

#%%
#            0         1          2
fruits = ["apple", "banana", "strawberry"]
print(fruits)
print(type(fruits))

print(fruits[0:2])

for e in fruits:
    print(f"--> {e}")

    print("end")

#%%

fruits = ["apple", "banana", "strawberry"]

#      k :   v    ,  k :  v  , ....
d = { "p":"pencil", "d":"dog", "c": fruits}

print(d)
print(type(d))

for k,v in d.items():
    print(f"key: {k} - value: {v}")

#%%

first_name = "Mary"
last_name = "Mason"

print(f"{first_name} {last_name}")

print("{1} {0}".format(first_name, last_name))














