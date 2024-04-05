import os
import re

def openfile():
    file_list = []
    with open('./input.txt') as file_data:
        for line in file_data.readlines():
            file_list.append(line.split("\n")[0])
        return file_list


def part1_solution():
    game = openfile()
    answer = 0
    for inp in game:
        ID = inp.split(":")[0].split(" ")[1]
        cube_dict = {"red":(list(map(int,(re.findall(r'(\d+) red\b', inp))))), "green":(list(map(int,(re.findall(r'(\d+) green\b', inp))))), "blue": (list(map(int,(re.findall(r'(\d+) blue\b', inp)))))}
        if max(cube_dict["red"]) > 12 or max(cube_dict["green"]) > 13 or max(cube_dict["blue"]) > 14:
            pass
        else:
            answer += int(ID)
            
    return answer
        

def part2_solution():
    game = openfile()
    answer = 0
    for inp in game:
        ID = inp.split(":")[0].split(" ")[1]
        cube_dict = {"red":(list(map(int,(re.findall(r'(\d+) red\b', inp))))), "green":(list(map(int,(re.findall(r'(\d+) green\b', inp))))), "blue": (list(map(int,(re.findall(r'(\d+) blue\b', inp)))))}
        x = max(cube_dict["red"]) * max(cube_dict["green"]) * max(cube_dict["blue"])
        answer += x
    return answer

if __name__ == "__main__":
    ret1 = part1_solution()
    ret2 = part2_solution()
    print(ret2)
