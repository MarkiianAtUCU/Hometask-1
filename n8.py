# This function takes two positive numbers n and m and returns the sum
# of the range 1 ^ m + 2 ^ m + ... + n ^ m.
import sys


def rec(n, m):
    """

    :param n: int, 5
    :param m: int, 6
    :return: int, 20515

    """
    if n == 0:
        return 0
    return n**m + rec(n - 1, m)

# check the input
try:
    sys.setrecursionlimit(1000000)
    n = int(input('Enter a positive integer n: '))
    m = float(input('Enter another positive integer m: '))
    if n < 0 or m < 0:
        print("Error! Enter valid value")
    else:
        print('The sum of the range is: ', rec(n, m))
except:
    print("Error! Enter valid value")
