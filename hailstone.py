# Author: Makaliah Dickinson
# Date: 7/11/2020
# Description: A hailstone sequence starts with some positive integer. If that integer is even, then you divide it by
#              two to get the next integer in the sequence, but if it is odd,then you multiply it by three and add one
#              to get the next integer in the sequence. Then you use the value you just generated to find the next value,
#              according to the same rules. For example, if our initial number is 3, the subsequent numbers will be:
#              10, 5, 16, 8, 4, 2, 1. Write a function named hailstone that takes a positive integer parameter as the
#              initial number of a hailstone sequence and returns how many steps it takes to reach 1 (technically you
#              could keep going 1, 4, 2, 1, 4, 2, etc. but you will stop when you first reach 1). If the starting integer
#              is 1, the return value should be 0, since it takes no steps to reach 1 (we're already there). For example,
#              if the starting integer is 3, then the sequence would go: 3, 10, 5, 16, 8, 4, 2, 1, and the return value
#              should be 7, since it took 7 steps to reach 1. Your function does not need to print anything out - just
#              return a value.

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> hailstone
    if n <=1:
        print(1)
        return 1
    else:
        return hailstone_helper(n,1)
        """


input(print("Enter a positive integer:\n "))

"""
def hailstone_helper(n, num_steps):
    if n <= 1:
        return num_steps
    else:
        if n % 2 == 0:
            print(int(n / 2))
            hailstone_helper(int(n / 2), num_steps + 1)
        else:
            print(int(3 * n + 1))
            hailstone_helper(int(3 * n + 1), num_steps + 1)
"""
