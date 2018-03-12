"""
Given an input string and a dictionary of words,
find out if the input string can be segmented into a space-separated sequence of
dictionary words. See following

examples for more details.
This is a famous Google interview question, also being asked by many other companies
now a days.
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung"
or "i like sam sung".

https://www.youtube.com/watch?v=RPeTFTKwjps
"""
from nose.tools import assert_true


def word_break(word, dict, i):
    if word[:i] in dict:
        return True
    if word[i-1:] in dict and word_break(word, dict, i-1):
        return True
    else:
        word_break(word, dict, i-1)


if __name__ == "__main__":
    word_dict = {'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream',
                 'icecream', 'man', 'go', 'mango'}
    word = "ilike"
    assert_true(word_break(word, word_dict, len(word)))
