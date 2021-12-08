#!/usr/bin/env python3

data_file = open("./input", 'r')
data = []

# larger measurement counter
lm = 0
with open("./input") as input_text:
    for line in input_text:
        data.append(int(line.strip()))

num_entries = len(data)

i = 0

while i < num_entries:
    if i > 0:
        if data[i] > data[i-1]:
            lm += 1
    i += 1

print(lm)

