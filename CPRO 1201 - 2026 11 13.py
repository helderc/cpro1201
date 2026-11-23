
# iteractive
def countdown(n):
    while n > 0:
        print(n)
        n -= 1

countdown(5)

#%%
# recursive

def countdown_rec(n):
    if n <= 0:
        return
    print(n)
    countdown_rec(n)

countdown_rec(5)

print("finished!")

#%%
# factorial: n! -> 5! = 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(4.2))













