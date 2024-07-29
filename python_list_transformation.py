grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()
grades.reverse()
print(f"All the class grades are: {grades}")

average_grade = sum(grades) // len(grades)
print(f"The average grade in the class is: {average_grade}")