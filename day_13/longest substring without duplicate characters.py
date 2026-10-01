"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
"""
s = "abcabcbb"

current = ""
maximum = 0

for ch in s:
    if ch not in current:
        current += ch
        maximum = max(maximum, len(current))
    else:
        current = current[current.index(ch) + 1:]
        current += ch

print(maximum)