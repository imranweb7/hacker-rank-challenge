# Your Python Path Here
# https://www.hackerrank.com/challenges/diwali-lights
# combination theory

factorial_dict = {};

def getFactorial(n):
    try:
        return factorial_dict[n];
    except KeyError:
        if ((n - 1) <= 0):
            factorial_dict.update({1: 1});
            return 1;

        factorial_dict.update({n: (n * getFactorial(n - 1))});
        return factorial_dict[n];


def getTotalNumberofPatterns(total, n, r):
    if (r > n):
        return total;

    if (n >= r):
        total = total + (getFactorial(n) / (getFactorial(r) * getFactorial(n - r)));

    return getTotalNumberofPatterns(total, n, (r + 1));


T = int(input());
while (T > 0):
    N = int(input());
    print(int(getTotalNumberofPatterns(0, N, 1)));
    T -= 1;