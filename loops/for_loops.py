# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0
total_count = 0
for i in student_heights:
  total_height += i
  total_count += 1

average_height = round(total_height / total_count)