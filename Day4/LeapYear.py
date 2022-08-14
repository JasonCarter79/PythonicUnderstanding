# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Cleanly divisible = (no remainder. modulo == 0.)
# Leap Year When below is true:
# (Cleanly divisible by 4 AND NOT cleanly divisible by 100)
# OR
# (Cleanly divisible by 4 AND 100 AND 400)

if year % 4 == 0:
  #print("Might be a leap year")
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")