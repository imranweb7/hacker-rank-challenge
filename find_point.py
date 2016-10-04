# Your Python Path Here
# https://www.hackerrank.com/challenges/find-point
# find symmetric point of point P about Q.
x = int(input());
while(x > 0):
	line = input().split();
	px = int(line[0]);
	py = int(line[1]);
	qx = int(line[2]);
	qy = int(line[3]);
	print((qx  - px + qx),  (qy  - py + qy));	
	x -= 1;

