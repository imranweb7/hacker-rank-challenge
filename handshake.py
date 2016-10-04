# Your Python Path Here
# https://www.hackerrank.com/challenges/handshake
# Count handshakes - pigeonhole principle
import math;
T = int(input());
while(T > 0):
	directors = int(input());
	#TC --- Director = Count handshake
	#1 = 0
	#2 = 1
	#3 = 3
	#4 = 6
	#5 = 10
	#6 = 15
	# (n * n-1) / 2 
	print(math.floor((directors * (directors - 1)) / 2));	
	T -= 1;

