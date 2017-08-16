from itertools import permutations, product

file = open("output.txt", "w")

def reverse_polish(exp):
    stack = []

    for val in exp.split(' '):
        if val in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val == '-':
                result = op2 - op1
            if val == '+':
                result = op2 + op1
            if val == '*':
                result = op2 * op1
            if val == '/':
                try:
                    result = op2 / op1
                except:
                    pass
            stack.append(result)
        else:
            stack.append(float(val))

    return stack.pop()

nums4 = []
nums3 = []
nums2 = []
nums1 = []
expression = []

perm4 = permutations(['1', '4', '8', '9'], 4)
for p in perm4:
    nums4.append(p)
perm3 = permutations(['1', '4', '8', '9'], 3)
for p in perm3:
    nums3.append(p)
perm2 = permutations(['1', '4', '8', '9'], 2)
for p in perm2:
    nums2.append(p)
perm1 = permutations(['1', '4', '8', '9'], 1)
for p in perm1:
    nums1.append(p)

for item in nums4:
    OpsPerm4 = product(['+','-','/','*'], repeat=3)
    for p in OpsPerm4:
        expression.append(item+p)
for item in nums3:
    OpsPerm3 = product(['+','-','/','*'], repeat=2)
    for p in OpsPerm3:
        expression.append(item+p)
for item in nums2:
    OpsPerm2 = product(['+','-','/','*'], repeat=1)
    for p in OpsPerm2:
        expression.append(item+p)
for item in nums1:
    OpsPerm1 = product(['+','-','/','*'], repeat=0)
    for p in OpsPerm1:
        expression.append(item+p)

for i in expression:
    exp = " ".join(i)
    polish_result = reverse_polish(exp)
    if (1 <= polish_result <= 100) and (polish_result.is_integer()):
        print(i, '=', polish_result, file=file)

file.close()

