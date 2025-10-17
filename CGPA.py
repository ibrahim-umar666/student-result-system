def get_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    elif avg >= 30:
        return "E"
    else:
        return "F"

def get_remark(grade):
    if grade == "A":
        return "Excellent!"
    elif grade == "B":
        return "Very Good"
    elif grade == "C":
        return "Good"
    elif grade == "D":
        return "Fair"
    elif grade == "E":
        return "Poor"
    else:
        return "Fail – Needs improvement"

while True:
    matric_no = input("Enter student matric_no:")
    cos102 == int(input("Enter Math score: "))
    fuk-edu102 == int(input("Enter English score: "))
    sci = int(input("Enter Science score: "))

    total = math + eng + sci
    avg = total / 3
    grade = get_grade(avg)
    remark = get_remark(grade)

    print("\nResult for", matric_no)
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)
    print("Remark:", remark)

    choice = input("\nDo you want to enter another student? (yes/no): ")
    if choice.lower() != "yes":
        break