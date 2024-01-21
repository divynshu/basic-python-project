#we can use max or min function but we not use it.
#we just solve it by loop to get better understang of for loop.

#input alist of student score
student_score=input().split()
for n in range(0,len(student_score)):
    student_score[n]=int(student_score[n])
highest_score=0
for score in student_score:
    if score>highest_score:
        highest_score=score
print(f"The higest score in the clas is:{highest_score}")
