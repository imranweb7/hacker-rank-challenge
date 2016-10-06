# Your Python Path Here
# https://www.hackerrank.com/contests/master/challenges/restaurant
# Bread cutting in restaurant - maximum large square shape

def getMaximumLargeSquareShape(length, breadth):
	#if it is already square dont need to slice
	if(length == breadth): return 1;
	
	#if length is greater then breadth then swap for calculation 
	if(length > breadth): return getMaximumLargeSquareShape(breadth, length);
	
	max_square = 0;
	for x in range(1, length+1):
		if((length % x == 0) and (breadth % x == 0)):
			max_square = ((length/x) * (breadth/x));
				
	return int(max_square);
		

T = int(input());
while(T > 0):
	line = input().split();
	length = int(line[0]);
	breadth = int(line[1]);
	
	print(getMaximumLargeSquareShape(length, breadth));
	T -= 1;