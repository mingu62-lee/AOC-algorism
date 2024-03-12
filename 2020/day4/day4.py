import re

def cleanPassport(p):
    #k,v선언 후 :기준으로 잘라서 \necl:hzl\nbyr:1991\niyr:1930 eyr:2024 이 부분 \n 컷
    pairs = [(k, v) for (k, v) in [row.split(':') for row in [row for row in re.split('[\n \n]', p)]]]
    #
    #print(pairs)
    return pairs

def checkPassports(cleanedPassports):
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    cur = [pair[0] for pair in cleanedPassports]
    #print(cur)
    for key in keys:
        if key not in cur:
            return False
    return True




if __name__ == "__main__":
    file = open('day4/puzzle.txt', 'r')
    allPassports = file.read().split('\n\n')
    #print(allPassports)
    cleanedPassports = [cleanPassport(p) for p in allPassports]
    #print("\n")
    #print(cleanedPassports)
    validPassports = [p for p in cleanedPassports if checkPassports(p)]
    print("part1 =", len(list(validPassports)))
    print(validPassports[0])

    