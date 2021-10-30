import sys


def main(word):
    wordlist = open("/usr/share/dict/words", "r")
    words = [{"".join(sorted(x.strip())): x.strip()} for x in wordlist.readlines()]
    sortedwords = "".join(sorted(word))
    for i in [x for x in words if sortedwords in x.keys()]:
        print("".join(i[sortedwords]))


def usage():
    print("python letters.py WORD")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        exit(1)
    main(sys.argv[1])
