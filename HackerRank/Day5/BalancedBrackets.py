#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    open_brackets = ["{", "(", "["]
    bracket_pair = {"{": "}", "(": ")", "[": "]"}

    if len(s) % 2 != 0:
        return "NO"

    stack = []
    for c in s:
        if c in open_brackets:
            stack.append(c)
            continue

        if stack and bracket_pair[stack[-1]] == c:
            stack.pop(-1)
        else:
            return "NO"
    return "NO" if stack else "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
