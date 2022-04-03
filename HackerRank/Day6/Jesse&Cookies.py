"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value k. 
To do this, two cookies with the least sweetness are repeatedly mixed. 
This creates a special combined cookie with:
sweetness = (1 * Least sweet cookie + 2 * 2nd least sweet cookie).

This occurs until all the cookies have a sweetness >= k.

Given the sweetness of a number of cookies, determine the minimum number of operations required. 
If it is not possible, return -1.
"""

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq


def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    operations = 0
    while True:
        min1 = heapq.heappop(A)

        if min1 >= k:
            return operations

        if A:
            min2 = heapq.heappop(A)
            heapq.heappush(A, min1 + 2 * min2)
            operations += 1
        else:
            return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
