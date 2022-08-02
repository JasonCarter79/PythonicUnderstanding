# Don't do this as if elif statements stop after they find a true condition
# for number in range(1, 101):
#     if number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif nuumber % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz"
# Don't do this as if elif statements stop after they find a true condition

for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
