
def name1(ds):
    print(ds)
    
# f(x) = 2*x
def f(x):
    x = 2*x
    return x

grades = [23, 52, 87]
name1(grades)

print("finished")

this_is_a_text = "asdlkjjaslk d"
name1(this_is_a_text)

num1 = 13
res = f(num1)
print(f"{num1}: {res}")

res2 = f(grades)
print(res2)

#%%

def f2(x):
    res = x * x
    ...
    return res ** x

lst2 = [11, 22]
num1 = 56
res3 = f2(num1)
#print(res3)
name1(res3)

ii = str(res3)
iii = 0
for i in ii:
    iii += 1
print()
print(iii)

#%%

def grades_adj(g):
    # add +5 to each grade
    # and return it
    #for i in range(len(g)):
    #    g[i] += 15
    g_adj = [ grade+5 for grade in g ]
    return g_adj
    
grades1201 = [40, 56, 71, 2]
res_g1201 = grades_adj(grades1201)
print(res_g1201)

#%%

def g(x, y):
    return 2*x + 2*y

print(g(2,3))

#%%

def grades_adj(g, x, bonus=5):
    # add +5 to each grade
    # and return it
    #for i in range(len(g)):
    #    g[i] += 15
    g_adj = [ grade+bonus for grade in g ]
    return g_adj

grades1201 = [40, 56, 71, 2, 19.2]
#print(grades_adj(grades1201))

print(grades_adj(grades1201, 10))

print(grades_adj(x=2, g=[1,2,3], bonus=3))

#%%

def bubble_sort(lst):
    holder = 0
    result []
    for i in range(1, len(lst)):
        #if i > i+1:
        if lst[i-1] < 
            
    
lst1 = [13, 1, 9.0, 21, 81, 0, 67, -1]
res = bubble_sort(lst1)

print(lst1)
print(res)



















