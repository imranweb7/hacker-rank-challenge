# Your Python Path Here
# https://www.hackerrank.com/challenges/reverse-game
# Simple math

T = int(input());
while (T > 0):
	line = input().split();
	number_of_balls = int(line[0]);
	find_ball_number = int(line[1]);
	
	if((find_ball_number * 2) >= (number_of_balls - 1)):
		print(((number_of_balls - 1) * 2) - (find_ball_number * 2));
	else:
		print((find_ball_number * 2) + 1);
	
	T -= 1;