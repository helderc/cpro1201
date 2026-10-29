
# AND
# 0 AND 0 = False
# 1 AND 0 = False (0)
# 0 AND 1 = False
# 1 AND 1 = True
# 1 -> True; 0 -> False


temperature = -15
raining = False

if ((temperature < 0) and (raining == True)):    
    print("1 You shouldn't go outside!!!!! DONT GO!")
else:
    if temperature < 0:
        print("2 It is not that good")
    else:
        print("3 Go to touch grass!?!")
        if raining == False:    
            print("4 You are good to go!")
    

#%%

#grade = 20
grade = 32

if grade < 100:
    print("A")
elif grade < 58:
    print("D")
elif (grade >= 54) and (grade <= 57):
    print("D+")
else:
    print("I have no idea!!")















    
    













