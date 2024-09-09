# Task

# Perform append, pop, popleft and appendleft methods on an empty deque .

# Input Format

# The first line contains an integer N the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Constraints


# Output Format

# Print the space separated elements of deque .

# Sample Input

# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
# Sample Output

# 1 2


# Explanation

# Initially, the deque is empty.

# append(1) adds 1 to the right end of deque. deque becomes [1].
# append(2) adds 2 to the right end of deque. deque becomes [1, 2].
# append(3) adds 3 to the right end of deque. deque becomes [1, 2, 3].
# appendleft(4) adds 4 to the left end of deque. deque becomes [4, 1, 2, 3].
# pop() removes the rightmost element from deque and returns it. deque becomes [4, 1, 2]. The popped element is 3.
# popleft() removes the leftmost element from deque and returns it. deque becomes [4, 1]. The popped element is 1.
# Thus, the final output is 1 2.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
           
d = deque()
n = int(input())
for _ in range(n):
    keyboard = input()
    
    operation = keyboard.split()[0]
    value = ''
    if len(keyboard.split()) > 1:
        value = keyboard.split()[1]
    
    if operation == 'append':
        d.append(int(value))
    
    elif operation == 'appendleft':
        d.appendleft(int(value))
    
    elif operation == 'pop':
        d.pop()
    
    elif operation == 'popleft':
        d.popleft()
        
    elif operation == 'remove':
        d.remove(int(value))
    
    elif operation == 'count':
        d.count(int(value))
    
    elif operation == 'reverse':
        d.reverse()

    elif operation == 'rotate':
        d.rotate()

print(' '.join(map(str, d)))