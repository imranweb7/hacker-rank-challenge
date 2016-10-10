# Your Python Path Here
# https://www.hackerrank.com/challenges/little-chammys-huge-donation
# Divide and Conquer
import math;

list_square_summation = [0];

def findNumberOfChildrenServed(n, start, end):
	if(list_square_summation[start] == n): return start;
	if (list_square_summation[end] == n): return end;
	
	if (list_square_summation[start] < n and list_square_summation[end] > n):
		if(end - start == 1): return start;			
		mid = math.ceil((start + end) / 2);
		right = findNumberOfChildrenServed(n, mid, end);
		if(right): return right;
		else: return findNumberOfChildrenServed(n, start, mid);
	else: return 0;

def getNumberOfChildrenServed(n):
	result = findNumberOfChildrenServed(n, 0, (len(list_square_summation) - 1));
	if(result): return result;
	
	for i in range(len(list_square_summation), n + 1):
		sum = int(((i * (i+1) * ((2 * i) + 1)) / 6));
		list_square_summation.append(sum);
		if(sum == n): return i;
		if(sum > n): return i - 1;
	return 0;

T = int(input());
while(T > 0):
	X = int(input());
	print(getNumberOfChildrenServed(X));
	T -= 1;