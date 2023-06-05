import sys


def factorial(n):
    fact = 1
    if n <= 0:
        print(1)
        return
    else:
        for x in range(1, n + 1):
            fact *= x
        print(fact)
        factorial(n - 1)


if __name__ == '__main__':
    factorial(16)
    sys.exit(0)
