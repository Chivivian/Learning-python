# BMI calculator
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / height ** 2
bmi1 = int(bmi)

if bmi < 18.5:
    print ("Your BMI is " + str(bmi1) + ", you are underweight")
if bmi < 25:
    print ("Your BMI is " + str(bmi1) + ", your weight is normal")
elif bmi < 30:
    print ("Your BMI is " + str(bmi1) + ", you are slightly overweight")
elif bmi < 35:
    print ("Your BMI is " + str(bmi1) + ", you are obese")
else:
    print ("Your BMI is " + str(bmi1) + ", you are clinically obese")