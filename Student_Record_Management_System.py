student1 = ("James Sebastian", 18 , "12th grade" )
student2 = ("Jhon Verbos", 15 , "9th grade" )
student3 = ("Javier Santiago", 16 , "10th grade" )

students = (student1,student2,student3)

print(f"Number of students: {len(students)}")
print(f"Index of Javier Santiago: {students.index(student3)}")

student_ids = {1001,1002,1003,1004,1005}
courses = {"English", "History", "Sports", "Science", "Math"}

print(f"Student IDs: {student_ids}")
print(f"Courses: {courses}")

new_students = {1006, 1007}
student_ids.update(new_students)
print(f"Updated Student IDs: {student_ids}")

completed_courses = {"Math", "English"}
remaining_courses = courses - completed_courses
print(f"Remaining Courses: {remaining_courses}")

frozen_courses = frozenset(["Math", "Science", "English", "History"])
print(f"Frozen Courses: {frozen_courses}")

frozen_student_data = frozenset(students)
print(f"Frozen Student Data: {frozen_student_data}")