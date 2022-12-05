
#task = open("./2/example.txt","r")
task = open("./2/task.txt","r")
# A - Rock Score: 1
# B - Paper Score: 2
# C - Scissors Score: 3

# WON - 6
# Draw - 3
# lose - 0


# First round
# Response
# X - Rock
# Y - Paper
# Z - Scissors

# Second round
# X - Lose
# Y - Draw
# Z - WIN


def ScoreRockParrScissorsPart1(player1, player2):
    scoreShape = 0
    match player1:
        case "X":
            match player2:
                case "A":
                    return (1 + 3)
                case "B":
                    return (1 + 0)
                case "C":
                    return (1 + 6)
        case "Y":
            match player2:
                case "A":
                    return (2 + 6)
                case "B":
                    return (2 + 3)
                case "C":
                    return (2 + 0)
        case "Z":
            match player2:
                case "A":
                    return (3 + 0)
                case "B":
                    return (3 + 6)
                case "C":
                    return (3 + 3)

def ScoreRockParrScissorsPart2(player1, player2):
    status = 0
    match player1:        
        case "X":
            # Lose
            status = 0
            match player2:
                case "A":
                    return (status + 3)
                case "B":
                    return (status + 1)
                case "C":
                    return (status + 2)
        case "Y":
            # Draw
            status = 3
            match player2:
                case "A":
                    return (status + 1)
                case "B":
                    return (status + 2)
                case "C":
                    return (status + 3)
        case "Z":
            # Win
            status = 6
            match player2:
                case "A":
                    return (status + 2)
                case "B":
                    return (status + 3)
                case "C":
                    return (status + 1)

scoreA = 0
scoreB = 0
rowCOunt = 0

for row in task: 
    splitRow = row.split(" ")
    scoreA += ScoreRockParrScissorsPart1(splitRow[1].strip(), splitRow[0].strip())
    scoreB += ScoreRockParrScissorsPart2(splitRow[1].strip(), splitRow[0].strip())
    

print("Your score for part 1: " + str(scoreA))    
print("Your score for part 1: " + str(scoreB))    
    

task.close()