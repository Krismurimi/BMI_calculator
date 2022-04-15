def BMI_calc():
    weight = input("What is your weight? \n")
    height = input("What is your height? \n")
    try:
        bmi = float(weight) /(float(height)**2)
    except:
        print("Please input only digits")

    if bmi < 18.5:
        print("You are underweight")
    elif bmi < 25:
        print("Your weight is normal")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You are obese!")

    print(f'Your height is {height} and you weigh {weight}. Your BMI is {bmi}')

    return
BMI_calc()

