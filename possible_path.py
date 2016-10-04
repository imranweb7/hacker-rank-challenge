# Your Python Path Here
# https://www.hackerrank.com/challenges/possible-path
# 2D grid Possible path - greatest common divisor

def gcd(a, b):
	if(a == 0): return b;
	if(b == 0): return a;
	return gcd(b, a%b);

T = int(input());
while(T > 0):
	line = input().split();
	ax = int(line[0]);
	ay = int(line[1]);
	x = int(line[2]);
	y = int(line[3]);
	
	if(ax < 0): ax = ax * (-1);
	if(ay < 0): ay = ay * (-1);
	if(x < 0): x = x * (-1);
	if(y < 0): y = y * (-1);
	
	if(gcd(ax, ay) == gcd(x, y)):
		print("YES");
	else:
		print("NO");
		
	T -= 1;

