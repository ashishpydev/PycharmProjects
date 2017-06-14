import math
"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""
s = raw_input()
s = s.upper()
vowels = "AEIOU"
k_score = 0
s_score = 0

for i in range(len(s)):
    if s[i] in vowels:
        k_score += (len(s) - i)
    else:
        s_score += (len(s) - i)
if k_score > s_score:
    print("Kevin {}".format(k_score))
elif s_score > k_score:
    print("Stuart {}".format(s_score))
else:
    print("Draw")