import queue

def openfile():
    with open("./2021/day3/input.txt") as f:
        return f.readlines()

def calcultate(lst):
    z = 0
    asl = 0
    gam = 0
    for row in lst:
        if row==1:
            col = 2 ** z
            asl = asl + col
        else:
            col2 = 2 ** z
            gam = gam + col2
        z += 1
    return asl, gam

def part1():
    data_list = generator()
    asl, gam = calcultate(data_list)
    answer = asl * gam
    return answer

def generator(lines=None):
    zero_count = 0
    one_count = 0
    data_list = []
    if lines is None:
        lines = openfile()
    else:
        lines = lines
    countlen = len(lines[0].strip("\n"))
    for row in range(0,countlen): 
        for line in lines:
            if line[row] == "0":
                zero_count += 1
            else :
                one_count += 1
        if zero_count > one_count:
            data_list.append(0)
        else:
            data_list.append(1)
        zero_count = 0
        one_count = 0
    data_list.reverse()
    return data_list

def part2():
    '''
    oxygen
    co2
    generator에서 나타내는 값이 bit number가 큰것, 같다면 남겨둬야함

    '''
    gener_dict = {}
    lst = []
    num = 0
    lines = openfile()
    data_list = generator()

    for line in lines:
        if line[num] == str(data_list[num]):
            lst.append(line.strip("\n"))



def selfgen(lst, num):
    nlst = []
    ndata_list = generator(lst)
    for i in lst:
        if i[num] == str(ndata_list[num]):
            nlst.append(i)
    print(nlst)
    return nlst




print(part1())
