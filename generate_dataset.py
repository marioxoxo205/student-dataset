"""
Assignment Two: Fictional Student Dataset Generator
---------------------------------------------------
Generates a fictional dataset of students with:
  1. Student ID
  2. Department
  3. Level
  4. Attendance Percentage
  5. Average Examination Score

Run:  python generate_dataset.py
Output: students.csv
"""

import csv
import random

# Seed makes the dataset reproducible (same data every run)
random.seed(42)

NUM_STUDENTS = 200

DEPARTMENTS = {
    "CSC": "Computer Science",
    "ENG": "Engineering",
    "BUS": "Business Administration",
    "ACC": "Accounting",
    "MCB": "Microbiology",
    "ECO": "Economics",
    "LAW": "Law",
    "MAS": "Mass Communication",
}

LEVELS = [100, 200, 300, 400, 500]


def generate_student(index: int) -> dict:
    dept_code = random.choice(list(DEPARTMENTS))
    level = random.choice(LEVELS)

    # Attendance between 40% and 100%
    attendance = round(random.uniform(40, 100), 1)

    # Exam score loosely correlated with attendance, plus some noise
    base = 20 + attendance * 0.6
    noise = random.gauss(0, 8)
    exam_score = round(max(0, min(100, base + noise)), 1)

    return {
        "Student ID": f"STU{2025}{dept_code}{index:04d}",
        "Department": DEPARTMENTS[dept_code],
        "Level": level,
        "Attendance Percentage": attendance,
        "Average Examination Score": exam_score,
    }


def main():
    students = [generate_student(i) for i in range(1, NUM_STUDENTS + 1)]
    fields = list(students[0].keys())

    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(students)

    print(f"Created students.csv with {len(students)} records.")


if __name__ == "__main__":
    main()
