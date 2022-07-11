#This calculates how long it will take to get to a destination based on how fast traveling.
# time = distance / speed
# speed = distance / time
# distance = speed x time

destination = input("Where are you traveling to?\n")
distance = int(input("How many miles are you traveling?\n"))
speed = int(input("How fast will you be traveling?\n"))
time = round(distance / speed,2)

print(f"To get to {destination} it will take you {time} hours traveling at {speed} mph.")