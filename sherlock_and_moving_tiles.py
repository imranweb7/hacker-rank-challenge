# Your Python Path Here
# https://www.hackerrank.com/challenges/sherlock-and-moving-tiles
# two moving objects meeting time
# distance = time X speed

import math;

line = input().split();
length = float(line[0]);

# finding relative velocity of two moving object
relative_velocity =  float(line[2]) - float(line[1]);
if(relative_velocity < 0): relative_velocity =  float(line[1]) - float(line[2]);

# diagonal of first object
diagnoal_of_object = length * math.sqrt(2);

Q = int(input());
while(Q > 0):
    # overlapping area
    query = int(input());

    # diagonal of overlapping area
    diagnoal_of_query = math.sqrt(query) * math.sqrt(2);

    distance = diagnoal_of_object - diagnoal_of_query;

    print(distance / relative_velocity);
    Q -= 1;
