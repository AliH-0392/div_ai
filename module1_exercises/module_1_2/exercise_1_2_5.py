student_grade = int(input("Please enter your grade: "))
print(f"Your grade: {student_grade} \n")

if(((student_grade >= 0) and (student_grade <= 100))):
    if ((student_grade >= 90) and (student_grade <= 100)):
        print("The grade is A")
    elif ((student_grade >= 80) and (student_grade <= 89)):
        print("The grade is B")
    elif (((student_grade >= 70) and (student_grade <= 79))):
        print("The grade is C")
    elif((student_grade >= 60) and (student_grade <= 69)):
        print("The grade is D")
    else:
        print("The grade is F")
else:
    print("grade is incorrect")

