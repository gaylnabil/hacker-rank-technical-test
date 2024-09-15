# start() & end()
# These expressions return the indices of the start and end of the substring matched by the group.

# Code

# >>> import re
# >>> m = re.search(r'\d+','1234')
# >>> m.end()
# 4
# >>> m.start()
# 0

# Task

# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.

# Input Format

# The first line contains the string .
# The second line contains the string .

# Output Format

# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).

# Sample Input

# aaadaa
# aa
# Sample Output

# (0, 1)  
# (1, 2)
# (4, 5)


# Explanation

# In the first test case, the substring "aa" starts at index 0 and ends at index 1.
# In the second test case, the substring "aa" starts at index 1 and ends at index 2.
# In the third test case, the substring "aa" starts at index 4 and ends at index 5.
# Note: If there are multiple occurrences of the substring, print the first occurrence.

# Constraints
# 1 �� |S|, |k| �� 10^5
# |S|, |k| are the lengths of string S and string k respectively.
# S and k consist only of lowercase English alphabets.
# Substring k will always be present in string S.
# Language
# Python 3

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def find_index_start_end(s: str, k: str):
    m = re.search(k, s)
    print(m)
    if m is None:
        print((-1, -1))
    else:
        for i in range(0, len(s)):
            # print(s[i:])
            m = re.search(k, s[i: i + len(k)])
            if m is not None:
                print((m.start() + i, m.end()+ i - 1))

if __name__ == '__main__':
    
    s = input()
    k = input()
    find_index_start_end(s, k)


