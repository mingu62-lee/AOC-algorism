import queue

def openfile():
    with open("./2021/day2/input.txt") as f:
        return f.readlines()

def part1(f=None):
    horizontal = 0
    depth = 0
    lines = openfile()
    for line in lines:
        cmd = line.split(' ')[0]
        size = int(line.split(' ')[1])
        if cmd == "forward":
            horizontal += size
        elif cmd == "up":
            depth -= size
        elif cmd == "down":
            depth += size
        else:
            pass
    answer = horizontal * depth
    return answer

def checkdiff(depth=None, fwd=None):
    aim = depth
    if depth != 0:
        multi = aim * fwd
        return multi


def part2():
    horizontal = 0
    depth = 0
    mulsum = 0
    lines = openfile()
    for line in lines:
        cmd = line.split(' ')[0]
        size = int(line.split(' ')[1])
        if cmd == "forward":
            horizontal += size
            multi = checkdiff(depth, size)
            if multi is None:
                pass
            else:
                mulsum += multi
        elif cmd == "up":
            depth -= size
        elif cmd == "down":
            depth += size
        else:
            pass
    answer = horizontal * mulsum
    return answer


print(part2())