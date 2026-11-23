

print(1)
print(2)
print(3)
print(4)
print(5)

#%%

for number in range(6):
    print(number)
    if number == 2:
        break
    
    
#%%

#if EXPRESION -> True

count = 1
c = True

while (count <= 5) and c:
    print(f"{count}: test")
    count = count + 1
    if count == 3:
        c = False

print("finished!")


#%%

count = 1

while (count <= 5):
    print(f"{count}: test")
    count = count + 1
    if count == 3:
        break
    print(f"\t{count}!")
else:
    print("finished!")
    
#%%

print("Using 'for'-loop: 6, 5, 4, ..., 1")
for n in range(6, 0, -1):
    print(n)

#%%    
print("Using 'while'-loop: 6, 5, 4, ..., 1")
count = 6
while (count > 0):
    print(count)
    count -= 1
    #if count == 0:
    #    break'
    
#%%

for r in range(1,4):
    for c in range(3):
        print(f"{r} {c}")
    print(f"end: {r}")
    
#%%

s = "this is a string"
for letter in s:
    print(letter)

#%% 

# Groceries Receipt

# Ask the use "what" they bought and how much it "cost"
# When the user types "end" your software will:
#    - Stop asking
#    - Show the total: "Your total is: $...."





















































