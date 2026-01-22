student = {}

def add_student():
    name = input("Please enter the name of studnet you want to add: ")
    name = name.strip().title()
    grade = input("Please enter the grade: ").strip().upper()
    student[name] = grade
    print("Name added successfully")
    
def find_grade():
    search =  input("Please type the name of student whoose grade u want to know: ")
    search = search.strip().title()
    if search in student:
        print("Grade of the student are",student[search] )
    else:
        print(" Error")
        
import os
def show_all_student():
    print(student)
    
def calculate_average():
    grade_points = {"A": 4, "B": 3, "C": 2, "D": 1}
    total = 0
    count = 0
    for grade in student.values():
        if grade in grade_points:
            total = total + grade_points[grade]
            count = count + 1
    if count > 0:
        print("Average grade point:", total / count)
    else:
       print("No students available")

def save_to_file():
    file = open("student_list.txt", "w")
    for name, grade in student.items():
        file.write( name + ", " + grade + "\n" )
    file.close()

def load_to_file():
    try:
        file = open("student_list.txt", "r")
        for line in file:
            name, grade = line.strip().split(", ")
            student[name] = grade
        file.close()
    except FileNotFoundError:
        pass
load_to_file()
while True:
    
    try:
        print("Soo choose the operation you want to conduct")
        x = int(input("""
1 → Add student
2 → Find grade
3 → Show all students
4 → Calculate average
5 → Exit
: """))

        if x == 1:
            add_student()
            save_to_file()
        elif x == 2:
            find_grade()
        elif x == 3:
            show_all_student()
        elif x == 4:
            calculate_average()
        else :
            print("You have successfully exited")
            break


    except ValueError:
        print("Please enter a integer")


    
