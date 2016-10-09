# Your Python Path Here
# https://www.hackerrank.com/challenges/little-chammys-huge-donation
# Divide and Conquer

import math;

list_square_summation = [0];

def findNumberOfChildrenServed(n, start, end):
    if(list_square_summation[start] == n):
        return start;

    if (list_square_summation[end] == n):
        return end;

    if((end - start) == 1 and list_square_summation[start] < n and list_square_summation[end] > n):
        return start;

    if (list_square_summation[start] < n and list_square_summation[end] > n):
        mid = math.ceil((start + end) / 2);

        left = findNumberOfChildrenServed(n, start, mid);

        if(not left):
            return findNumberOfChildrenServed(n, mid+1, end);
        else:
            return left;
    else:
        return 0;


def getNumberOfChildrenServed(n):
    result = findNumberOfChildrenServed(n, 0, (len(list_square_summation) - 1));

    if(not result):
        for i in range(len(list_square_summation), n + 1):
            list_square_summation.append((i * (i+1) * ((2 * i) + 1)) / 6);

            result = findNumberOfChildrenServed(n, (i-1), (len(list_square_summation) - 1));
            if(result):
                break;

    return result;


T = int(input());
while(T > 0):
    X = int(input());
    print(getNumberOfChildrenServed(X));
    T -= 1;