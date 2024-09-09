# Consider the following:

# A string S, of length N where S =C0 + C1 + C2 ... CN-1.
# An integer K, where K is a factor of N.
# We can split S into N/K substrings where each substring Ti, consists of a contiguous block of K characters in S. Then.
# Use each Ti to create string Ui such that:

# The characters in Ui are a subsequence of the characters in Ti.
# Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly once. In other words, if the character at some index J in Ui occurs at a previous index < J in Ti, then do not include the character in string .
# Given S and K, print N/K lines where each line i denotes string Ui.

# Example

# S = 'AAABCADDE'

# There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so U1 = 'A'. The second substring has all distinct characters, so U2 = 'BCA'. The third substring has 2 different characters, so U3 = 'DE'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

# Function Description

# Complete the merge_the_tools function in the editor below.

# merge_the_tools has the following parameters:

# string S: the string to analyze
# int K: the size of substrings to analyze
# Prints

# Print each subsequence on a new line. There will be N/K of them. No return value is expected.

# Input Format

# The first line contains a single string S .
# The second line contains an integer K the length of each substring.


# Sample Input

# STDIN       Function
# -----       --------
# AABCAAADA   S = 'AABCAAADA'
# 3           K = 3
# Sample Output

# AB
# CA
# AD
# Explanation

# Split  into N/K = 9/3 = 3 equal parts of length K = 3. Convert each Ti to Ui by removing any subsequent occurrences of non-distinct characters in Ti:

# Print each  on a new line.

# T0 = "AAB" => U0 = "AB"
# T1 = "CAA" => U0 = "CA"
# T2 = "ADA" => U0 = "AD"

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        t = string[i:i+k]
        u = set(t)
        print(''.join(sorted(u, key=t.index)))

if __name__ == '__main__':
    
    string = 'AABCAAADA'
    string = 'RTYUUNOPOOAZQE'
    k = 4
    merge_the_tools(string, k)