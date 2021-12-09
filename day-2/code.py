#!/usr/bin/env python3

data_file = open("./input", 'r')
data = []

with open("./input") as input_text:
    for line in input_text:
        data.append(line.strip())

# part 1
hpos = 0
depth = 0

for cmd in data:
    split = cmd.split(" ")
    if split[0] == "forward":
        hpos += int(split[1])
    if split[0] == "down":
        depth += int(split[1])
    if split[0] == "up":
        depth -= int(split[1])

print("Your final position math for part 1 is %d" % (hpos*depth))

# part 2
hpos = 0
depth = 0
aim = 0

for cmd in data:
    split = cmd.split(" ")
    if split[0] == "forward":
        hpos += int(split[1])
        depth += aim * int(split[1])
    if split[0] == "down":
        aim += int(split[1])
    if split[0] == "up":
        aim -= int(split[1])

print("Your final position math for part 2 is %d" % (hpos*depth))