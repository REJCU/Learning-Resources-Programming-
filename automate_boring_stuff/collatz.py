"""
import sys

def collatz(number):
    if (number % 2) == 0:
        return number // 2
    else:
        return 3 * number + 1

def recall(collatz):
    x = int(input("Enter Number: "))
    try:
        while x != 1:
            return collatz(x)
    except KeyboardInterrupt:
        sys.exit()

print(recall(collatz))
"""


def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))

