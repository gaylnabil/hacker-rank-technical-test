# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example
x = 1
y = 1
z = 2
n = 3



# All permutations of [i, j, k] are:
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2]]
# Print an array of the elements that do not sum to .

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 2, 2], [1, 0, 0], [1, 1, 2]]

# Input Format

# Four integers  and , each on a separate line.

# Constraints

# Print the list in lexicographic increasing order.

# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0

# Each variable  and  will have values of  or . All permutations of lists in the form .
# Remove all arrays that sum to  to leave only the valid permutations.

# Sample Input 1

# 2
# 2
# 2
# 2
# Sample Output 1

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # data = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2]]
    
    result = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                v = [i, j, k]
                s = sum(v)
                if s != n:
                    result.append(v)
    print(result)