# Your Python Path Here
# https://www.hackerrank.com/challenges/diwali-lights
# permutation theory

T = int(input());
while (T > 0):
    N = int(input());
    total = ((2**N) - 1) % 100000;
    print(total);
    T -= 1;