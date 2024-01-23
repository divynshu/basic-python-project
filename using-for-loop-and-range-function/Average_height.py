#Just to find out average height of student
student_height=input().split() # just to take multiple input
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
total_height=0
for height in student_height:
    total_height+=height
print(f"total height ={total_height}")
number_of_student=0
for student in student_height:
    number_of_student+=1
print(f"number of student={number_of_student}")
average_height=round(total_height/number_of_student)
print(f"average height = { average_height}")

#input= 4o 60 5o
#total height=150
#number of student=3
#average height =50
