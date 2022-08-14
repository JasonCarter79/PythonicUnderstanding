print("Welcome to the roller coaster. Let's check your height to make sure you can ride ")
height = int(input("Enter your height in inches: "))
bill = 0

if height > 48:
  print("All aboard!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay $7.")
  else:
    bill = 12
    print("Please pay $12.")

  wants_photo = input("Do you want a photo? Y or N. ")
  if wants_photo == "Y":
    bill += 3
    print(f"Your final bill is {bill}")
else:
  print("Sorry, you're not quite tall enough yet.")