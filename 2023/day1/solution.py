import os
def openfile():
    file_list = []
    with open('./2023/day1/input.txt') as file_data:
        for line in file_data.readlines():
            file_list.append(line.split("\n")[0])
        return file_list
    
def part1_solution():
    Trebuchet = openfile()
    answer = 0
    for inp in Trebuchet:

        num_list = []
        for num in inp:
            if num.isdigit():
                num_list.append(int(num))
            else:
                pass
        if len(num_list) == 1:
            ans = num_list[0] * 11
        else:
            ans = int(str(num_list[0]) + str(num_list[-1]))

        answer = answer + ans
    return answer

def part2_solution():
    Trebuchet = openfile()
    answer = 0
    answer_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for inp in Trebuchet:
        dict_list = []
        distring = ''

        for num in inp:
            if num.isdigit():
                dict_list.append(int(num))
                distring = ''
            else:
                distring += num
                for i in answer_dict:
                    if i in distring:
                        
                        dict_list.append(answer_dict[i])
                        distring = distring[-1]

        if len(dict_list) == 1:
            ans = dict_list[0] * 11
        else:
            ans = int(str(dict_list[0]) + str(dict_list[-1]))
        answer = answer + ans
    return answer

if __name__ == "__main__":
    ret1 = part1_solution()
    ret2 = part2_solution()
    print(ret1, ret2)
