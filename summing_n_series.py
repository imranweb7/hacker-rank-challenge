# Your Python Path Here
# https://www.hackerrank.com/challenges/summing-the-n-series
# summation of n series

T = int(input());
mod = (10**9 + 7);
while (T > 0):
    n = int(input());
    sum = (n**2) % mod;
    print(sum);
    T -= 1;