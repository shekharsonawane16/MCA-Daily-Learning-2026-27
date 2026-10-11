# Assignment 1 - Student Performance Management System
# FY MCA | Division B | Academic Year 2026-27

# List: Maintain a list of all students.
students = [
    {
        "student_id": 101,
        "name": "Shekhar",
        "scores": {"Python": 82, "DSA": 76, "DBMS": 88}
    },
    {
        "student_id": 102,
        "name": "Rahul",
        "scores": {"Python": 65, "DSA": 72, "DBMS": 68}
    },
    {
        "student_id": 103,
        "name": "Priya",
        "scores": {"Python": 45, "DSA": 52, "DBMS": 48}
    }
]

# Tuple: Store fixed subject codes.
subject_codes = ("PY", "DSA", "DBMS")

# Set: Store unique subjects.
unique_subjects = {"Python", "DSA", "DBMS"}

print("STUDENT PERFORMANCE MANAGEMENT SYSTEM")
print("-" * 45)

passed_students = []

for student in students:
    student_id = student["student_id"]
    name = student["name"]
    scores = student["scores"]

    # Integer / Float: Calculate average score.
    average = sum(scores.values()) / len(scores)

    # Boolean: Flag pass/fail.
    passed = average >= 50
    status = "Pass" if passed else "Fail"

    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Average Score: {average:.2f}")
    print(f"Result: {status}")
    print()

    if passed:
        passed_students.append(name)

# Print names of students who passed.
print("Students who passed:")
for name in passed_students:
    print(f"- {name}")

print()
print("Subject Codes:", subject_codes)
print("Unique Subjects:", unique_subjects)
