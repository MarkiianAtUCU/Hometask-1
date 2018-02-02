# This function takes two positive integers n and m and returns the largest
# common divisor for these numbers based on the dependence
# F (n, m) = F (n-m, m)
import sys


def gcd(a, b):
    """
    :param a: int, 126
    :param b: int, 4
    :return: int, 2
    :param a: str, a
    :return: str, Enter only positive integers numbers, please!
    """
    return gcd(b, a % b) if b else a


try:
    sys.setrecursionlimit(1000000)
    a = int(input("Enter a positive integer: ",))
    b = int(input("Enter another positive integer: ",))
    if a < 0 or b < 0:
        print("Enter only positive numbers, please!")
    else:
        print("The greatest common divisor is:", gcd(a, b))
except:
    print("Enter only positive integers numbers, please!")
