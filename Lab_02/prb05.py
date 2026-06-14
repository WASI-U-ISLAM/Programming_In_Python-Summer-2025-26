marks = float(input("Enter the student's marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >= 85 and marks < 90:
    print("Grade: A")
elif marks >= 80 and marks < 85:
    print("Grade: B+")
elif marks >= 75 and marks < 80:
    print("Grade: B")
elif marks >= 70 and marks < 75:
    print("Grade: C+")
elif marks >= 65 and marks < 70:
    print("Grade: C")
elif marks >= 60 and marks < 65:
    print("Grade: D+")
elif marks >= 50 and marks < 60:
    print("Grade: D")
elif marks >= 0 and marks < 50:
    print("Grade: F (Fail)")
else:
    print("Invalid marks entered! Marks must be between 0 and 100.")