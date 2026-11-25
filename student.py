# Grade Calculator Program

marks = float(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

if marks < 0 or marks > 100:
    print("Invalid marks!")
else:
    print("Your marks:", marks)
    print("Your grade:", grade)
