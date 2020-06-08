"""
Given a string and number of rows to be used for zigzag pattern, return zigzagged string

Below code is 99.96% faster than all solutions availabe in leetcode. Runtime: 36ms

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows in [0, 1] or numRows > len(s):
            return s

        output = [""] * numRows
        pos = 0
        n_ = numRows - 1
        reverser = False
        for letter in s:
            output[pos] += letter
            if reverser:
                pos -= 1
            else:
                pos += 1

            if pos > n_:
                pos = n_ - (pos - n_)
                reverser = True

            if pos == 0 and reverser:
                reverser = False

        return "".join(output)

# sample input
"""
ABCDEF

zigZag:         A   D F
                B C E 

ACEBDF

"""