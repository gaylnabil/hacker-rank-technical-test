# Task
# Given an integer, , perform the following conditional actions:
# •	If n is odd, print Weird
# •	If n  is even and in the inclusive range of 2 to 5, print Not Weird
# •	If n is even and in the inclusive range of 6 to 20, print Weird
# •	If n is even and greater than 20 , print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints
# •	
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input 0
#  n = 3
# Sample Output 0
# Weird
# Explanation 0
#  n = 3
#  n is odd and odd numbers are weird, so print Weird.
# Sample Input 1
# 24
# Sample Output 1
# Not Weird
# Explanation 1
#  n = 24
#  n > 24 and  is even, so it is not weird.

if __name__ == '__main__':
    print("enter a number: ")
    n = int(input().strip())
    
    if n % 2 != 0:
        value = "Weird"
    else:
        if n in range(2, 6):
            value = "Not Weird"
        elif n in range (6, 21):
            value = "Weird"
        else:
            value = "Not Weird"
    
    print(f"The number {n} is: {value}")
