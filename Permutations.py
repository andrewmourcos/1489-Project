import itertools
import operator

# make a dictionary for the operators
ops_dict = {
    'P': operator.add,
    'M': operator.sub,
    'T': operator.mul,
    'D': operator.truediv
}

# Insert operations as strings in a list
opslist = ["P","M","T","D"]

# store the 4 numbers to use in variables
a = 1
b = 4
c = 8
d = 9

# Insert those numbers into a list
nums = [a, b, c, d]
perm_nums = []
perm_ops = []
n = 0

while len(perm_nums) < 24:
    # Determine all permutations for the numbers
    perm1 = itertools.permutations(nums, 4)
    for p in perm1:
        perm_nums.append(p)

    # Determine all permutations for the operations
    perm2 = itertools.permutations(opslist, 3)
    for p in perm2:
        perm_ops.append(p)

    print(perm_nums)
    print(perm_ops)

