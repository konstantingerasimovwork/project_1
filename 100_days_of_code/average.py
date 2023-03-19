student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


summ_height = 0
students = 0
for height in student_heights:
  summ_height += height
  students += 1
average = round(summ_height / students)
print(average)