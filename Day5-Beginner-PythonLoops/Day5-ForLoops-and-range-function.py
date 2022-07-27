#For loop with Range - first 2 numbers are the range. If a 3rd number that specifies the step. e.g. 5 = print every
#5th number
# for num in range(1, 101):
#     print(num)

#Below loops through every number in range adding them all together
total = 0
for number in range(1,101, 2):
    total += number
print(total)