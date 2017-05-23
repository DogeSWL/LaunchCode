import math
"""
A program to take grade input and calculate a student's gpa
"""

grades = []

# gather grade information
while True:
    grade = input("Your grade (0.0-4.0): ")
    credits = input("# credits: ")

    # store grades
    grades.append({'grade': float(grade), 'credits': int(credits)})

    continue_entry = input("Enter another grade? [y/n]: ")
    if continue_entry == 'n':
        break

    # compute GPA
    total_quality_score = 0
    total_credits = 0

# calculate quality scores and total
for gradeinfo in grades:
    total_quality_score += (gradeinfo['grade'] * gradeinfo['credits'])
    total_credits += gradeinfo['credits']

gpa = math.ceil((total_quality_score / total_credits)*100)/100
print("Your GPA is:", gpa)
