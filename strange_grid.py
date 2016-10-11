# Your Python Path Here
# https://www.hackerrank.com/challenges/strange-grid
# simple math

grid_cell = input().split();

row = int(grid_cell[0]);
col = int(grid_cell[1]);
remainder = row % 2;

start = (row - 1) * 5;
if(remainder == 0): start = (row - 2) * 5;

if(start < 0): start = 0;
if(remainder == 0): start = start + 1;

print(start + ((col - 1) * 2));
