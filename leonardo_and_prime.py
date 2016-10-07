# Your Python Path Here
# https://www.hackerrank.com/challenges/leonardo-and-prime
# find Maximum number of unique Prime factors in range [1, n] - Sieve of Eratosthenes Prime Factorizations - Divide and Conquer

import math;
''''
MAX = 60;
list = [1 for x in range(0, MAX)];
list[0] = 0;

for i in range(1, MAX):
	if(list[i]):
		k = 0;
		while(MAX):
			j = ((i+1)*(i+1)) + (k*(i+1));
			if(j > MAX): break;
			list[j-1] = 0;
			k += 1;

primes_count = [];
current_value = 1;			
for x in range(0, MAX):
	if(list[x]):
		current_value = current_value * (x+1);
		primes_count.append(current_value);
'''
# using Sieve of Eratosthenes Prime Factorizations algorithm 
# following prime multiplication generated to avoid TLE 
primes_count = [2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230, 200560490130, 7420738134810, 304250263527210, 13082761331670030, 614889782588491410, 32589158477190044730, 1922760350154212639070];		
	
def getMaximumNumberofUniquePrimeFactors(n, start, end):

	if(primes_count[start] == n):
		return start+1;
		
	if(primes_count[end] == n):
		return end+1;
	
	if(n > primes_count[start] and n < primes_count[end]):
		if(end - start == 1):
			return start+1;
			
		left = getMaximumNumberofUniquePrimeFactors(n, start, math.ceil((start+end) / 2));
		
		if(left):
			return left;
		else:
			return getMaximumNumberofUniquePrimeFactors(n, math.ceil((start+end) / 2), end);
	else:
		return 0;
	
	
Q = int(input());
while(Q > 0):
	n = int(input());
	if(n == 1): print('0');
	else: print(getMaximumNumberofUniquePrimeFactors(n, 0, len(primes_count)-1));
	Q -= 1;