
x = 1.1
y = 2.2

z = x + y # 3.3

print(f"{z}: {z == 3.3}")
#print(z, ":", z == 3.3)

tolerance = 0.01
print(abs(z - 3.3) < tolerance)

#%%

# not, or, and
is_admin = False
has_account = True

print(is_admin)
print(not is_admin)
print(f"Has account? -> {has_account}")

res = has_account and is_admin
print(f"Has account AND is admin? {res}")

res2 = has_account or is_admin
print(f"Has account OR is admin? {res2}")

#%%

is_admin = False
has_account = True

if has_account == True:
    print("User has an account")
if is_admin == True:
    print("User is admin")

#%%

print(bool(0), bool(0.0), bool(0.0+0j))
print(bool(""), bool(" "))
print(bool(""" """))

#int(...)
#float(...)
num1 = 5
num1_str = str(num1)

print(f"num1: {num1} - {type(num1)}")
print(f"num1_str: {num1_str} - {type(num1_str)}")

print(id(num1))
print(id(num1_str))

#%%

a = 5
#...
a = a + 17
a += 17
#
a -= 10 # a = a - 10
a *= 8 # a = a * 8
a /= 2 # a = a / 2





