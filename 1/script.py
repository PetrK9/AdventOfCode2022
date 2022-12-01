
task = open("task.txt","r")

currElf = 0
currCaloriesSum = 0
topElf = 0
topElfSum = 0
topThreeElfs = 0

caloriesList = []

for row in task:    
    if(row == "\n"):
        currElf += 1
        caloriesList.append(currCaloriesSum)
        if(topElfSum<currCaloriesSum):
            topElf = currElf
            topElfSum = currCaloriesSum
        currCaloriesSum = 0
    else:
       currCaloriesSum += int(row)

caloriesList.sort(reverse=True)

topThreeElfs = sum(caloriesList[0:3])

print("Top Elf:" + str(topElf))
print("Count of calories:" + str(topElfSum))
print("-"*15)
print("Top 3 Elfs:" + str(topThreeElfs) )


task.close()