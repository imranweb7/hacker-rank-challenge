# Your Python Path Here
# https://www.hackerrank.com/challenges/sherlock-and-divisors
# Sherlock and divisors

T = int(input());
while(T > 0):
	N = int(input());
	total_divisor_by_two = 0;
	if(N%2 == 0):
		total_divisor_by_two += 1;
		i = 4;
		while(i <= N):
			if(N%i == 0):
				total_divisor_by_two += 1;					
			if((N/2) == i):
				total_divisor_by_two += 1;	
				i = N;
			i = i + 2;	
	print(total_divisor_by_two);
	T -= 1;

