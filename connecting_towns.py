# Your Python Path Here
# https://www.hackerrank.com/challenges/connecting-towns
# Modular arithmetic

T = int(input());
while(T > 0):
	towns = int(input());
	routes = input().split();
	total_routes = 1;
	
	for i in range(0, towns-1):
		total_routes = total_routes * int(routes[i]);

	print(total_routes % 1234567);
	T -= 1;