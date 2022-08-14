# 🚨 Don't change the code below 👇
height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in pounds: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#BMI formula U.S. is weight (lb) / [height (in)]2 x 703
BMI = round(weight / height**2*703)

if BMI < 18.5:
  print(f"Your bmi is {BMI}, you are underweight.")
elif BMI < 25:
 print(f"Your bmi is {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your bmi is {BMI}, you are overweight.")
elif BMI < 35:
  print(f"Your bmi is {BMI}, you are obese.")
else:
  print(f"Your bmi is {BMI}, you are clinically obese.")