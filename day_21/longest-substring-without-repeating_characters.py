"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


"""

s = "abcabcbb"

ch_count = {}
count = 0
max_count = 0

for ch in s:
    if ch not in ch_count:
        ch_count[ch] = 1
        count += 1
    else:
        count = 1
        ch_count = {ch: 1}

    if count > max_count:
        max_count = count

print(max_count)