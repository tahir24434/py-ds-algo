"""
Michelle has created a word game for her students. The word game begins with
Michelle writing a string and a number, K, on the board. The students must find a
substring of size K such that there is exactly one character that is repeated once;
in other words, there should be K - 1 distinct characters in the substring.
Write an algorithm to help the students find the correct answer. If no such
substring can be found, return an empty list; if multiple such substrings exist,
return all of them, without repetitions. The order in which the substrings are
returned does not matter.

Input
The input to the function/method consists of two arguments - inputString,
representing the string written by the teacher; num, an integer representing the
number, K, written by the teacher on the board.
Output
Return a list of all substrings of inputString with K characters, that have K-1
distinct character i.e. exactly one character is repeated, or an empty list if no
such substring exists in inputString. The order in which the substrings are returned
does not matter.
Constraints
The input integer can only be greater than or equal to 0 and less than or equal to
26 (0 ≤ num ≤ 26) The input string consists of only lowercase alphabetic characters.
"""


def is_exactly_one_repeating(s):
    count = {}
    for item in s:
        count[item] = count.get(item, 0) + 1
    repeating = False
    for val in count.values():
        if (not repeating) and (val > 1):
            repeating = True
        elif repeating and val > 1:
            return False
    return repeating


def generate_substrings(s, k):
    res = set()
    len_s = len(s)
    if k > len_s:
        return " "
    for i in range(len_s):
        end_index = min(i+k, len_s)
        sub = s[i:end_index]
        print(sub)
        if is_exactly_one_repeating(sub):
            res.add(sub)
    return res

if __name__ == "__main__":
    s = "abccbcdc"
    k = 3
    print(generate_substrings(s, k))



