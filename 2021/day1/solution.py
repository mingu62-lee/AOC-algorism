import queue

def openfile():
    with open("./2021/day1/input.txt") as f:
        return f.readlines()

def part1(f=None):
    answer = 0
    index = 0    
    if f:
        answer = 0
        index = 0
        for row in f:
            if index == row:
                pass
            elif index < row:
                if index == 0:
                    pass
                else:
                    answer += 1
            else:
                pass
            index = row
    else:
        lines = openfile()
        for line in lines:
            if index == int(line.rstrip('\n')):
                pass
            elif index < int(line.rstrip('\n')):
                if index == 0:
                    pass
                else:
                    answer += 1
            else :
                pass
            index = int(line.rstrip('\n'))
    
    return answer

        
def part2():
    qlist = []
    three = []
    three_count=0
    lines = openfile()
    answer = 0
    for line in lines:
        sum =0
        qlist.append(int(line.rstrip('\n')))
        if len(qlist)==3:
            for row in qlist[:]:
                sum += row
            three.append(sum)
            del qlist[0]
    return part1(three)

print(part2())