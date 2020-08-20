import sys

def fact(n):
    """
    jiecheng def
    :arg n: num
    :returns: n's *
    """
    if n == 0:
        return 1
    return n * fact(n - 1)

def div(n):
    """
    just chufa
    """
    res = 10 / n
    return res

def main(n):
    res = fact(n)
    print(res)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))

