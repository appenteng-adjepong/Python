grades = "a+ a a- b+ b b- c+ c c- d+ d f".upper().split(" ")
scores = "4.0 4.0 3.67 3.33 3.0 2.67 2.33 2.0 1.67 1.33 1.0 0.0".split(" ")
grading_system = {grade: float(scores[idx]) for idx, grade in enumerate(grades)}

def get_grade(grading_system):
    course_count = 0
    total_points = 0
    done = False
    while not done:
        grade = input().upper()
        if grade == "":
            done = True
        elif grade not in grading_system:
            print("Unknown grade '{}' being ignored...".format(grade))
        else:
            course_count += 1
            total_points += grading_system[grade]
    if course_count > 0:

        print("You took {} courses.\nYour GPA is {:.3}.".format(course_count, total_points/course_count))


get_grade(grading_system)

def get_final_grade(grading_system, n_courses):
    course_count = 0
    total_points = 0
    while True:
        grade = input("").upper()
        if grade not in grading_system:
            print(f"Unknown grade: {grade}")
        else:
            course_count += 1
            total_points += grading_system[grade]

        if course_count == n_courses:
            break
    print("You took {} courses.\nYour GPA is {:.3}.".format(course_count, total_points/course_count))

get_final_grade(grading_system, 15)

