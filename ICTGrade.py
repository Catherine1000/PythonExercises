name = input("Enter your name: ")
Homework = int(input("Enter Homework marks: "))
Assessment = int(input("Enter Assessment marks: "))
Final = int(input("Enter final exam marks: "))

def ictGrade():
    score = (((Homework/25 + Assessment/50 + Final/100) / 3)*100)

    if score >= 70:
        grade = "Grade: A"
    elif score >= 60:
        grade = "Grade: B"
    elif score >= 50:
        grade = "Grade: C"
    elif score >= 40:
        grade = "Grade: D"
    else:
        grade = "Fail"
    
    return grade 

print(name, ictGrade())