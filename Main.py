from itertools import permutations


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

nums = []
expression = []

perm1 = permutations(['1', '4', '8', '9'], 4)
for p in perm1:
    nums.append(p)

for item in nums:
    perm2 = permutations(['+','-','/','*'], 3)
    for p in perm2:
        expression.append(item+p)

for i in expression:
    exp = " ".join(i)
    polish_result = reverse_polish(exp)
    if (0 <= polish_result <= 100) and (polish_result.is_integer()):

        print(i,'=', polish_result)
