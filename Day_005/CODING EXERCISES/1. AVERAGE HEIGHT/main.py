# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
#for total height 
for height in student_heights:
  total_height += height
#print(total_height)

#for no of students
no_of_students = 0
for student in student_heights:
  no_of_students += 1
#print(no_of_students)

average_height = total_height/no_of_students

print(f"The average height is {average_height}")
  
