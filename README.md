# Lab11.py
import matplotlib.pyplot as plt
import os
import math

def main():
    print_menu()
    print()
    choice_user = input("Enter your selection: ")
    if choice_user == "1":
        get_student_grade()
    elif choice_user == "2":
        get_assignment_statistics()
    elif choice_user == "3":
        make_assignment_graph()
    exit()

def print_menu():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")

def get_student_grade():
    student_input = input("What is the student's name: ")
    students = sort_students()
    assignments_sort = sort_assignments_by_code()
    student_grade = 0

    if student_input not in students:
        print("Student not found")
        return

    for file in os.listdir("data/submissions"):
        file_path = os.path.join("data/submissions", file)
        with open(file_path, "r") as submission_file:
            line = submission_file.readline().strip()
            if line[0:3] == students[student_input]:
                assignment_code = line[4:-3].strip()
                score = int(line[-2:])
                weight = 0
                for assignment in assignments_sort:
                    if assignment == assignment_code:
                        weight = int(assignments_sort[assignment]) / 100
                        student_grade += score * weight

    print(f"{custom_round(student_grade / 1000 * 100)}%")

def get_assignment_statistics():
    assignment = input("What is the assignment name: ")
    assignments = sort_assignments_by_name()
    grades = []
    assignment_code = ''

    for item in assignments:
        if assignment == item:
            assignment_code = assignments[item]

    if assignment_code == '':
        print("Assignment not found")
        return

    for file in os.listdir("data/submissions"):
        file_path = os.path.join("data/submissions", file)
        with open(file_path, "r") as submission_file:
            line = submission_file.readline().strip()
            if assignment_code != line[4:-3].strip():
                continue
            grades.append(int(line[-2:]))

    maximum = find_max(grades)
    minimum = find_min(grades)
    average = find_average(grades)

    print(f"Min: {minimum}%")
    print(f"Avg: {average}%")
    print(f"Max: {maximum}%")

def make_assignment_graph():
    assignment = input("What is the assignment name: ")
    assignments = sort_assignments_by_name()
    grades = []
    assignment_code = ''

    for item in assignments:
        if assignment == item:
            assignment_code = assignments[item]

    if assignment_code == '':
        print("Assignment not found")
        return

    for file in os.listdir("data/submissions"):
        file_path = os.path.join("data/submissions", file)
        with open(file_path, "r") as submission_file:
            line = submission_file.readline().strip()
            if assignment_code != line[4:-3].strip():
                continue
            grades.append(int(line[-2:]))

    plt.hist(grades, bins=[0, 25, 50, 75, 100])
    plt.title(f"Distribution of Grades for {assignment}")
    plt.xlabel("Grade Range")
    plt.ylabel("Number of Students")
    plt.show()

def sort_students():
    with open("students.txt", "r") as students_file:
        lines = students_file.readlines()
    students = {}
    for line in lines:
        students[line[3:].strip()] = line[0:3]  # map student name to 3-digit ID
    return students

def sort_assignments_by_code():
    with open("assignments.txt", "r") as assignments_file:
        lines = assignments_file.readlines()
    assignments = {}
    for i in range(1, len(lines), 3):
        assignments[lines[i + 1].strip()] = lines[i + 2].strip()  # map assignment code to point value
    return assignments

def sort_assignments_by_name():
    with open("assignments.txt", "r") as assignments_file:
        lines = assignments_file.readlines()
    assignments = {}
    for i in range(1, len(lines), 3):
        assignments[lines[i].strip()] = lines[i + 1].strip()  # map assignment name to code
    return assignments

def custom_round(number):
    decimal = number - int(number)
    if decimal < 0.5:
        return math.floor(number)
    else:
        return math.ceil(number)

def find_max(grades):
    i = 0
    maximum_grade = grades[0]
    while i < len(grades):
        if grades[i] > maximum_grade:
            maximum_grade = grades[i]
        i += 1
    return maximum_grade

def find_min(grades):
    i = 0
    minimum_grade = grades[0]
    while i < len(grades):
        if grades[i] < minimum_grade:
            minimum_grade = grades[i]
        i += 1
    return minimum_grade

def find_average(grades):
    return int(sum(grades) / len(grades))

if __name__ == '__main__':
    main()
