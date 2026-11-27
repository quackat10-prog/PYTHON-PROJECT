Height=float(input("Enter your height"))
Weight= float(input("Enter your weight"))
BMI=Weight/(Height/100)**2
print("BMI =",BMI)
if BMI<18.5 :
    print("You are underweight")
elif BMI>18.5 and BMI<24.9 :
    print("Your weight is normal")
elif BMI>25 and BMI<29.9 :
    print("You are overweight")
else: print("you are obese")
