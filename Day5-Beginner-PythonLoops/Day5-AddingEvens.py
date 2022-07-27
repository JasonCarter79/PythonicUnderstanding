# Using a step of 2, to count every other number, and start at 2 knowing they will then only be the evens.
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# Using modulo for a remainder of 0 = cleanly divisible
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)
