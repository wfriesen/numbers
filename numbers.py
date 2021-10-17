import sys
from itertools import permutations

perms = []


def build_permutations(start, perm, total_numbers):
    newperm = perm.copy()

    if start >= (total_numbers * 2) - 1:
        perms.append(newperm)
        return

    for k in ["*", "/", "+", "-"]:
        build_permutations(
            start + 2, newperm[:start] + [k] + newperm[start:], total_numbers
        )


def main(target, numbers):

    for i in permutations(numbers):
        perm = list(i)
        build_permutations(1, perm, len(numbers))

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


def usage():
    print("python numbers.py TARGET NUMBER1 NUMBER2 ...")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)
    target = int(sys.argv[1])
    numbers = [int(x) for x in sys.argv[2:]]
    main(target, numbers)
