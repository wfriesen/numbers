from itertools import permutations

numbers = [75, 7, 3, 1, 5, 7]
target = 242
perms = []


def go(start, perm):
    newperm = perm.copy()
    if start > 9:
        perms.append(newperm)
        return

    for k in ["*", "/", "+", "-"]:
        go(start + 2, newperm[:start] + [k] + newperm[start:])


for i in permutations(numbers):
    perm = list(i)
    go(1, perm)


def solved(perm):
    sols = perm.copy()
    if len(sols) == 1:
        return sols[0] == target

    left = sols.pop(0)
    operator = sols.pop(0)
    right = sols.pop(0)

    if operator == "*":
        result = left * right
    elif operator == "/":
        result = left / right
    elif operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right

    return solved([result] + sols)


for perm in perms:
    s = solved(perm)
    if solved(perm) is True:
        print(perm)
