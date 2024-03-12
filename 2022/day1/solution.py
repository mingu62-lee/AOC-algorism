def openfile():
    with open("./2022/day1/input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        Elf = 0
        Elflist = []
        for i in lines:
            if i == "":
                Elflist.append(Elf)
                Elf = 0
            else:
                Elf = Elf + int(i)
        return Elflist

def solution():
    Calories = openfile()

    #part1ret = max(Calories)

    three_elves = 0

    for i in sorted(Calories)[-3:]:
        three_elves = i + three_elves

    part2ret = three_elves

    return part2ret

if __name__ == "__main__":
    ret = solution()
    print(ret)