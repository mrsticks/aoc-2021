#!/usr/bin/env python3
import math

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
        if data[i] > data[i - 1]:
            lm += 1
    i += 1

print(lm)

i = 0
a = 0
b = 1
c = 2
this_sum = 0
prev_sum = 0
num_increases = 0

while i < num_entries:
    if i == 0:
        prev_sum = data[a] + data[b] + data[c]
    i += 1
    a += 1
    b += 1
    c += 1
    if i <= num_entries - 3:
        this_sum = data[a] + data[b] + data[c]
    # do the logic
        if this_sum > prev_sum:
            num_increases += 1
        # move the sum fwd
        this_sum = prev_sum
        prev_sum = data[a] + data[b] + data[c]

print(num_increases)


