import operator
import sys
from itertools import permutations

OPS = {operator.mul: "*", operator.truediv: "/", operator.add: "+", operator.sub: "-"}
perms = []


def build_permutations(start, perm, total_numbers):
    newperm = perm.copy()

    if start >= (total_numbers * 2) - 1:
        perms.append(newperm)
        return

    for k in OPS.keys():
        build_permutations(
            start + 2, newperm[:start] + [k] + newperm[start:], total_numbers
        )


def main(target, numbers):

    for i in permutations(numbers):
        perm = list(i)
        build_permutations(1, perm, len(numbers))

    def solved(initial, perm, steps=0):
        steps += 1
        sols = perm.copy()
        if sols[0] == target:
            return (True, initial[:steps])
        elif len(sols) == 1:
            return (sols[0] == target, initial[:steps])

        left = sols.pop(0)
        op = sols.pop(0)
        right = sols.pop(0)

        result = op(left, right)

        return solved(initial, [result] + sols, steps + 1)

    for perm in perms:
        (solves, solution) = solved(perm.copy(), perm)
        if solves is True:
            print(" ".join([str(x) if type(x) == int else OPS[x] for x in solution]))


def usage():
    print("python numbers.py TARGET NUMBER1 NUMBER2 ...")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)
    target = int(sys.argv[1])
    numbers = [int(x) for x in sys.argv[2:]]
    main(target, numbers)
