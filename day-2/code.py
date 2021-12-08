#!/usr/bin/env python3

data_file = open("./input", 'r')
data = []
hpos = 0
depth = 0

with open("./input") as input_text:
    for line in input_text:
        data.append(line.strip())

for cmd in data:
    split = cmd.split(" ")
    if split[0] == "forward":
        hpos += int(split[1])
    if split[0] == "down":
        depth += int(split[1])
    if split[0] == "up":
        depth -= int(split[1])

print("Your final position math is %d" % (hpos*depth))
