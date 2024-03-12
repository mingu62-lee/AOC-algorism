'''
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
'''

TRANS_KEYWORD = {
    "A" : "Rock",
    "B" : "Paper",
    "C" : "Scissors",
    "X" : "Rock",
    "Y" : "Paper",
    "Z" : "Scissors"
}

def openfile():
    with open("./2022/day2/input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def part1solution():
    answer = 0
    strategy = openfile()
    for i in strategy:
        if TRANS_KEYWORD[i.split(" ")[1]] == "Rock":
            answer += 1
        elif TRANS_KEYWORD[i.split(" ")[1]] == "Paper":
            answer += 2
        else:
            answer += 3

        if TRANS_KEYWORD[i.split(" ")[0]] == TRANS_KEYWORD[i.split(" ")[1]]:
            answer += 3
        elif TRANS_KEYWORD[i.split(" ")[0]] == "Rock" and TRANS_KEYWORD[i.split(" ")[1]] == "Paper" or TRANS_KEYWORD[i.split(" ")[0]] == "Scissors" and TRANS_KEYWORD[i.split(" ")[1]] == "Rock" or TRANS_KEYWORD[i.split(" ")[0]] == "Paper" and TRANS_KEYWORD[i.split(" ")[1]] == "Scissors":
            answer += 6
        elif TRANS_KEYWORD[i.split(" ")[0]] == "Rock" and TRANS_KEYWORD[i.split(" ")[1]] == "Scissors" or TRANS_KEYWORD[i.split(" ")[0]] == "Scissors" and TRANS_KEYWORD[i.split(" ")[1]] == "Paper" or TRANS_KEYWORD[i.split(" ")[0]] == "Paper" and TRANS_KEYWORD[i.split(" ")[1]] == "Rock":
            answer += 0

    return answer

def part2solution():
    answer = 0
    strategy = openfile()

    for i in strategy:
        if i.split(" ")[1] == "X":
            if TRANS_KEYWORD[i.split(" ")[0]] == "Rock":
                answer += 3
            elif TRANS_KEYWORD[i.split(" ")[0]] == "Paper":
                answer += 1
            else:
                answer += 2
            answer += 0
        elif i.split(" ")[1] == "Y":
            if TRANS_KEYWORD[i.split(" ")[0]] == "Rock":
                answer += 1
            elif TRANS_KEYWORD[i.split(" ")[0]] == "Paper":
                answer += 2
            else:
                answer += 3
            answer += 3
        if i.split(" ")[1] == "Z":
            if TRANS_KEYWORD[i.split(" ")[0]] == "Rock":
                answer += 2
            elif TRANS_KEYWORD[i.split(" ")[0]] == "Paper":
                answer += 3
            else:
                answer += 1
            answer += 6
    return answer 
if __name__ == "__main__":
    #ret = part1solution()
    ret = part2solution()
    print(ret)