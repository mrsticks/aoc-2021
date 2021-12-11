#!/usr/bin/env python3

data_file = open("./input", 'r')
gamma = ""
epsilon = ""
zerobits = 0
onebits = 0

i = 0
j = 0
matrix = []
with open("./input") as input_text:
    for line in input_text:
        line = line.strip()
        matrix.append([])
        matrix[i].append(int(line[j]))
        j += 1
    i += 1

#for line in matrix:

print("this is the length of matrix %d" % len(matrix))
print("this is the length of matrix[1] %d " % len(matrix[1]))
print(matrix[1])