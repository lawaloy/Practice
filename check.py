#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n)
    queries_length = len(queries)
    for idx in range(queries_length):
        arr[queries[idx][0]] += queries[idx][2]
        if queries[idx][1]+1 < n:
            arr[queries[idx][1]] -= queries[idx][2]
    curSum = 0
    totalMax = float("-inf")
    for num in arr:
        curSum += num
        totalMax = max(curSum, totalMax)
    return(totalMax)


queries = [[2, 3, 603],[1, 1, 286],[4, 4, 882]]
n = 5
print(arrayManipulation(n, queries))



