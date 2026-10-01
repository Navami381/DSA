"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
s = "A man, a plan, a canal: Panama"

s = s.lower() #Convert to lowercase

new_s = ""         #Keep only letters and numbers

for char in s:
    if char.isalnum():
        new_s += char


if new_s == new_s[::-1]:     #check if it is equal to its reverse
    print(True)
else:
    print(False)