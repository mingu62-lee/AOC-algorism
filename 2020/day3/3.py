
from functools import reduce

def toboggan(treeCount,row,col,line:list) -> int:
    r =0
    c =0
    while r+1 < len(lines):
        r +=row
        c +=col
        way = lines[r][c % len(lines[r])]
        if way == "#":
            treeCount +=1
    return treeCount

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

if __name__ == "__main__":
    f = open("day3/puzzle.txt", 'r')
    lines = f.readlines()
    lines = [line.strip() for line in lines]


    treeCount =0
    row =1
    col =3
    print("part1= ",toboggan(treeCount, row, col, lines))

    slope_answer = []
    row =[1,1,1,1,2]
    col =[1,3,5,7,1]

    for (i,j) in zip(row,col):
        slope_answer.append(toboggan(treeCount, i, j, lines))
    print("part2= ",multiply(slope_answer))

#문제가 바뀔때 대응훈련 함수를 나누자
