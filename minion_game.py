# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# ⁡⁣⁢⁢For Example:⁡
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:

# banana.png

# Your task is to determine the winner of the game and their score.

# ⁡⁣⁢⁢Function Description⁡

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze

#⁡⁣⁢⁢ Prints⁡

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner

# ⁡⁣⁢⁢Input Format⁡

# A single line of input containing the string ⁡⁢⁢⁡⁢⁣⁣S⁡⁡.
# Note: The string ⁣S⁡⁢⁣⁣⁡ will contain only uppercase letters: ⁡⁢⁣⁣[A-Z]⁡.

# Constraints



# Sample Input

# BANANA
# Sample Output

# Stuart 12
# Note :
# Vowels are only defined as ⁡⁢⁣⁣'AEIOU'⁡. In this problem,  is not considered a vowel.


def minion_game(string):
    # Initialize variables
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0

    # Iterate over each character in the string
    for i in range(len(string)):
        # Check if the character is a vowel
        if string[i] in vowels:
            # Add 1 point to Kevin's score for each vowel starting substring
            kevin_score += len(string) - i
        else:
            # Add 1 point to Stuart's score for each consonant starting substring
            stuart_score += len(string) - i

    # Determine the winner and print their score
    if stuart_score > kevin_score:
        print('Stuart', stuart_score)
    elif stuart_score < kevin_score:
        print('Kevin', kevin_score)
    else:
        print('Draw')
    
    
# Test the function with the provided example
if __name__ == '__main__':
    #s = input()
    s = 'AYOUB'  # Expected output: Kevin 7
    s = 'BANANA'  # Expected output: Stuart 12
    minion_game(s)
