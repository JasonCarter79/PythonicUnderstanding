# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# The below can't be used for this challenge but would be a very easy way to do it
# total_height = sum(student_heights)
# num_of_students = len(student_heights)
# avg_height = round(total_height / num_of_students)
# print(avg_height)
print(student_heights)
# The below replicates how the sum function works
total_height = 0
for height in student_heights:
  # total_height = total_height + height
  total_height += height
print(total_height)

# Now we can replicate how the len function works
num_students = 0
for student in student_heights:
  num_students += 1
print(num_students)

avg_height = round(total_height / num_students)
print(avg_height)