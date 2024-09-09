# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# records = [["chi", 20.0], ["alpha", 50.0], ["beta", 50.0]]
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score:
# ["alpha", "beta"]. Ordered alphabetically, the names are printed as:

# alpha
# beta

# Input Format

# The first line contains an integer N the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.

# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    students.sort(key=lambda x: x[1], reverse=False)
    print("sort: ", students)
    
    minimum = min(students, key=lambda x: x[1])
    print("min01: ", minimum)
    
    students = [student for student in students if minimum[1]!= student[1]]
    print("remove max: ", students)
    
    print(students)

    minimum = students[0]
    students.sort(key=lambda x: x[0], reverse=False)
    for student in students:
        if minimum[1] == student[1]:
            print(student[0])