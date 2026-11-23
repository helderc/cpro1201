

try: 
    inp = input("Enter a number (int): ")
    amount = int(inp)
    res = 100/amount
except ValueError:
    print("Wrong value!")
    res, amount = 0, 0    
except ZeroDivisionError:
    print("The value must be > 0!")
    res, amount = 0, 0
finally:
    print("Calculation attempt finished.")

print(f"{amount}: {res}")

print("finished!")







