# 변수명
# 함수나누기
# map(), reduce()함수이용

answer = 0

def passvalid(password, password_text, valid, invalid):

	first = password[valid] == password_text 
	second = password[invalid] == password_text 
	
	if (first and second) or (not first and not second):
		return False
	else:
		return True

with open('day2/puzzle.txt') as f:
	for line in f:
		lineSplit = line.split(":")

		password = lineSplit[1].strip()
		
		number = lineSplit[0].split()
		password_text = number[1]
		
		numbers = number[0].split("-")
		valid = int(numbers[0]) - 1
		invalid = int(numbers[1]) - 1

		if passvalid(password, password_text, valid, invalid):
			answer += 1

	print(answer)
