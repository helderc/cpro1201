
s1 = "CPRO 1201"
s2  = " is GREAT"

s12 = s1 + s2

print(s12)

#%%

print("-" * 20)

s3 = "RDP"

print(s3 * 6)

#%%

n = 2
print(n * (s2 + s3))

#%%

s4 = s1 + s2
#s5 = f"s4: '{s4}'"

print(f"s4: '{s4}'")

s6 = "is" * 10 # 2 chr
print(f"s6: {s6}")

print(s6 in s4)

#%%

s4 = s1 + s2
print(f"s4: '{s4}'")

s6 = "is"
print(f"s6: {s6}")

print(s6 not in s4)

#%%

print(chr(97))


print(ord('a'))

print(f"s1: |{s1}|; length: {len(s1)}")

sl = s4.split()
print(sl[0])

#%%

# str()

n1 = 32
print(type(n1))

n2 = 123

print(n1 + n2)

fs = f"{n1}"
print(type(fs), fs)

fs2 = str(n1)
print(type(fs2), fs2)

print(str(n1) + str(n2))

#%%

#s = s1 + s2
s = "Python is GREAT"
print(s, len(s))

print(s[1])
print(s[len(s)-1], len(s))

print(s[3:8])

print(s[:5]) # 0:5-1 -> 0:4
print(s[0:5])

s2 = s[2:]
s3 = s[2:8]
print(s2, type(s2))
print(s3)

s4 = s2 + s3
print(s4)

s5 = s
print(id(s))
print(id(s5))

print(s5 is s)

#%%

s1 = "s1"

print(s[8:2])

print(s)
print(s[-5:-2])

# string[N1 : N2 : N3]
# N1: first character
# N2: 
print('str:', s[:10:2])

print(s1, 10, s2, 91239)






























