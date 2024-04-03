import os
def openfile():
    file_list = []
    with open('./2023/day1/input.txt') as file_data:
        for line in file_data.readlines():
            file_list.append(line.split("\n")[0])
        return file_list
    
def part1_solution():
    pass

def part2_solution():
    pass

if __name__ == "__main__":
    ret1 = part1_solution()
    #ret2 = part2_solution()
    print(ret1)
    #print(ret2)
