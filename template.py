import sys
import math
import string

def bround(num):
    decimals = 100.0
    multiplied = num * decimals
    floored = math.floor(multiplied)
    remainder = multiplied - floored
    if remainder >= .5:
        floored += 1
    rounded = str(floored / decimals)
    while len(rounded) - rounded.index('.') <= 2:
        rounded += '0'
    return rounded

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    var1, var2 = (float(val) for val in line.split(","))