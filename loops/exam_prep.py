allowed_poor_grades = int(input("Enter the number of allowed poor grades: "))

poor_grades_count = 0
total_score = 0
problem_count = 0
last_problem = ""

while True:
    problem_name = input("Enter problem name (or 'Enough' to stop): ")

    if problem_name == "Enough":
        break

    grade = int(input("Enter grade: "))
    total_score += grade
    problem_count += 1
    last_problem = problem_name

    if grade <= 4:
        poor_grades_count += 1
        if poor_grades_count == allowed_poor_grades:
            print(f"You need a break, {poor_grades_count} poor grades.")
            break

if problem_name == "Enough":
    average_score = total_score / problem_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem}")
