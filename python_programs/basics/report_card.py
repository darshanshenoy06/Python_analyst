student_name = input("Enter the student's name: ")
student_age = int(input("Enter the student's age: "))
student_marks = float(input("Enter the student's marks: "))
student_grade = student_marks
if student_marks >= 90:
    student_grade = "A"
elif student_marks >= 80:
    student_grade = "B"
elif student_marks >= 70:
    student_grade = "C"
elif student_marks >= 60:
    student_grade = "D"
else:
    student_grade = "F" 
dict_report_card = {
    "Name": student_name,
    "Age": student_age,
    "Marks": student_marks,
    "Grade": student_grade
}
print(dict_report_card)      