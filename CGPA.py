import csv
import os


def get_grade(score):
    if score >= 70:
        return "A", 5
    elif score >= 60:
        return "B", 4
    elif score >= 50:
        return "C", 3
    elif score >= 45:
        return "D", 2
    elif score >= 40:
        return "E", 1
    else:
        return "F", 0


def get_remark(grade):
    remarks = {
        "A": "Excellent",
        "B": "Very Good",
        "C": "Good",
        "D": "Fair",
        "E": "Poor",
        "F": "Fail – Needs Improvement"
    }
    return remarks.get(grade, "Invalid")


def save_to_csv(student_name, matric, semester, courses, total_units, total_weighted_points, gpa, remark):
    """Save results to CSV file."""
    file_exists = os.path.isfile("results.csv")

    with open("results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Name", "Matric", "Semester", "Course", "Score", "Unit",
                "Grade", "Grade Point", "Weighted Point", "GPA", "Remark"
            ])

        for c in courses:
            writer.writerow([
                student_name, matric, semester, c["Course"], c["Score"], c["Unit"],
                c["Grade"], c["GP"], c["WP"], gpa, remark
            ])

    print("\n✅ Result saved successfully to results.csv.")


def calculate_cgpa(matric):
    """Calculate CGPA from existing records."""
    if not os.path.exists("results.csv"):
        return None

    total_points = 0
    total_units = 0

    with open("results.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Matric"] == matric:
                total_points += float(row["Weighted Point"])
                total_units += float(row["Unit"])

    if total_units == 0:
        return None
    return round(total_points / total_units, 2)


def view_all_results():
    """Display all saved results."""
    if not os.path.exists("results.csv"):
        print("\n❌ No results found.")
        return

    with open("results.csv", mode="r") as file:
        reader = csv.DictReader(file)
        print("\n=== ALL SAVED RESULTS ===\n")
        for row in reader:
            print(
                f"{row['Name']} ({row['Matric']}) | {row['Semester']} | "
                f"{row['Course']} | Score: {row['Score']} | Grade: {row['Grade']} | GPA: {row['GPA']}"
            )


def add_new_result():
    """Add new student result."""
    print("\n🎓=== ADD NEW STUDENT RESULT ===")
    name = input("Enter Student Name: ")
    matric = input("Enter Matric No: ").upper()
    semester = input("Enter Semester (e.g. First, Second): ").capitalize()

    total_units = 0
    total_weighted_points = 0
    courses = []

    while True:
        course_code = input("\nEnter Course Code (e.g. CSC101): ").upper()
        score = int(input(f"Enter {course_code} Score (0–100): "))
        unit = int(input(f"Enter {course_code} Credit Unit: "))

        grade, grade_point = get_grade(score)
        weighted_point = grade_point * unit

        courses.append({
            "Course": course_code,
            "Score": score,
            "Unit": unit,
            "Grade": grade,
            "GP": grade_point,
            "WP": weighted_point
        })

        total_units += unit
        total_weighted_points += weighted_point

        more = input("Add another course? (yes/no): ").lower()
        if more != "yes":
            break

    gpa = round(total_weighted_points / total_units, 2)
    final_grade = "A" if gpa >= 4.5 else "B" if gpa >= 3.5 else "C" if gpa >= 2.5 else "D" if gpa >= 1.5 else "F"
    remark = get_remark(final_grade)

    # Display summary
    print("\n=== SEMESTER RESULT SUMMARY ===")
    print(f"Student: {name} ({matric}) | Semester: {semester}")
    print("Course\tScore\tUnit\tGrade\tGP\tWP")
    print("-" * 45)
    for c in courses:
        print(f"{c['Course']}\t{c['Score']}\t{c['Unit']}\t{c['Grade']}\t{c['GP']}\t{c['WP']}")
    print("-" * 45)
    print(f"Total Units: {total_units}")
    print(f"Total Weighted Points: {total_weighted_points}")
    print(f"GPA: {gpa}")
    print(f"Remark: {remark}")

    save_to_csv(name, matric, semester, courses, total_units, total_weighted_points, gpa, remark)

    cgpa = calculate_cgpa(matric)
    if cgpa:
        print(f"\n📊 Cumulative GPA (CGPA) so far: {cgpa}")
    else:
        print("\nNo previous records found for CGPA.")


def check_cgpa():
    """Check CGPA for a specific student."""
    matric = input("\nEnter student matric number: ").upper()
    cgpa = calculate_cgpa(matric)
    if cgpa:
        print(f"📊 Student {matric} has a CGPA of {cgpa}")
    else:
        print("❌ No record found for that matric number.")


# ================================
# MAIN MENU
# ================================
while True:
    print("\n==============================")
    print("🎓 CGPA MANAGEMENT SYSTEM")
    print("==============================")
    print("1️⃣  Add New Student Result")
    print("2️⃣  View All Results")
    print("3️⃣  Check Student CGPA")
    print("4️⃣  Exit")
    print("==============================")

    choice = input("Choose an option (1–4): ")

    if choice == "1":
        add_new_result()
    elif choice == "2":
        view_all_results()
    elif choice == "3":
        check_cgpa()
    elif choice == "4":
        print("\n👋 Thank you for using the CGPA Management System!")
        break
    else:
        print("❌ Invalid choice. Please enter 1–4.")
