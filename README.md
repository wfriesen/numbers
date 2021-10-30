# numbers

A solver for the letters and numbers games on Countdown/Letters and Numbers.
Number solver uses a naive, brute force algorithm. Brute forces all permutations of the given numbers, along with the operators `*/+-`. The televised game only includes 6 numbers, which can be done in seconds on an old laptop.

Why spend time coming up with a smart solution when the dumb one is quick enough?

# Requirements

Python 3+
Standard UNIX words file at /usr/share/dict/words

# Usage

`python numbers.py TARGET NUMBER1 NUMBER2 ...`

```bash
$ python numbers.py 242 75 7 3 1 5 7
7 / 7 + 75 + 5 * 3 - 1
7 / 7 + 5 + 75 * 3 - 1
7 / 7 + 75 + 5 * 3 - 1
7 / 7 + 5 + 75 * 3 - 1
```

`python letters.py moretiny`

```bash
$ python letters.py moretiny
enormity
```
