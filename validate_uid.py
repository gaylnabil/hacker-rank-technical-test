# ABCXYZ company has up to  employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.

# A valid UID must follow the rules below:

# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits (0 - 9).
# It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.
# Input Format

# The first line contains an integer N the number of test cases.
# The next N lines contains an employee's UID.

# Output Format

# For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

# Sample Input

# 2
# B1CD102354
# B1CDEF2354
# Sample Output

# Invalid
# Valid
# Explanation

# B1CD102354:  is repeating → Invalid
# B1CDEF2354: Valid


if __name__ == '__main__':
    
    import re

    # Regular expression pattern
    pattern = r'^(?!.*(.).*\1)(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[A-Za-z0-9]{10}$'

    for _ in range(int(input())):
        if re.match(pattern, input()):
            print('Valid')
        else:
            print('Invalid')
    
    # Explanation:
    # ^                      : Start of string
    # (?!.*(.).*\1)           : Negative lookahead to check for repeated characters
    # (?=.*[A-Z].*[A-Z])      : Ensure at least 2 uppercase letters
    # (?=.*\d.*\d.*\d)        : Ensure at least 3 digits
    # [A-Za-z0-9]{10}         : Exactly 10 alphanumeric characters
    # $                      : End of string

