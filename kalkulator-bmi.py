Name = input("Input your name: ")
Age = input("Input your age: ")
BB = int(input("Input your weight: "))
TB = float(input("Input your height: "))
BMI = (BB) / (TB*TB)
print("")
print("")
print(Name)
print(Age)
print(BB)
print(TB)
print(BMI)
print("")
if BMI <= 18.5:
    print('Your BMI is', BMI,'which means your underweight')
elif BMI > 18.5 and BMI < 25:
    print('Your BMI is', BMI,'congrats, your normal.')
elif BMI > 25 and BMI < 30:
    print('Your BMI is', BMI,'which means your overweight.')
elif BMI > 30:
    print('Your BMI is', BMI,'which means your obese.')
else:
    print('there was an error when inputting')
input('\n\nPlease press enter to exit.')

