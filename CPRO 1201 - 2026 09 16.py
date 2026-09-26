
assig1 = 0.25
assig2 = 4.82
assig3 = 10

# Math: 
#    1: * /
#    2: + -
average = (assig1 + assig2 + assig3) / 3

#print("Average:", average)
print(f"Average: {average}")

#%%

num1 = 2
num2 = 1.2

res = num1 - num2
res2 = num2 - num1

print(res)
print(res2)

#%%

num1 = 2.56
num2 = -3

print(num1 / num2)
print(num1 // num2)

#%%
num1 = 5
num2 = 3.2

print(num1 / num2)
print(num1 % num2)

print(num1 ** num2)

print(type(num1))
print(type(num2))

print(type(num1 ** num2))

#%%
num1 = 5 # assignment operator
num2 = 3.2

print(num1 == num2)
print(num1 != num2)

#%%
# > < <= >=
num1 = 2
num2 = 3
print(f"num1: {num1}; num2: {num2}")
print(num1 > num2)
print(num1 < num2)

# ...( (True) == (True) )
print((num1 <= num2) == (num1 != num2))
print(num1 <= num2 == num1 != num2)

print(f"num1: {num1}")

# instead of conv. to bool -> True == True
# -> conv. to int -> True (1) == num1 (2)
print("!", True == num1)
print("!", num1 >= True == (num1 == num2))

print("int(True):", int(True))

print(bool(num1))
print(True, type(True), bool(True))

num3 = -0.1
print(bool(num3))



























