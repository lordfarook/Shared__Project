from math import gamma

teacher = input("Hello teacher! What are the subjects you would like to include in the avrage of any student? ")
subject = [q.strip() for q in teacher.split(", ")]
len_subject = len(subject)

grades = []

students_num = int(input("How many students there are in your class? "))
y = 0
list_students = []
subjects = []
avg_student = []
avg_class = []
bag = {}
while y < students_num:
    grades = []
    hibur = 0
    name = input("Hello, what is your name? ")
    for x in subject:
        grade = int(input(f"Hello {name}, What is your grade at {x}? "))
        if grade < 0 or grade > 100:
            print("invalid grade, please insert a grade between 0 to 100! ")
            grade = int(input(f"Hello {name}, What is your grade at {x}? "))

        grades.append(grade)  # adds to a list the tatal grades of a student
        hibur = sum(map(int, grades))  # summing up all the grades and convert them to integers
        avg_student = hibur / len(subject)  # avrage

    avg_class.append(avg_student)  # a list of the avrage of every student

    bag[name] = grades
    g = ", ".join(str(values) for values in bag.values())

    print("")
    y += 1

print(bag)
print(avg_class)
