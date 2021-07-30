import sys


def Collatz(num):
    if (num % 2 == 0):
        num = num / 2
        print(int(num))

        if(num != 1):
            Collatz(num)
    elif (num % 2 == 1):
        num = num * 3 + 1
        print(int(num))
        Collatz(num)


if __name__ == '__main__':
    num = int(sys.argv[1])
    print(num)
    Collatz(num)