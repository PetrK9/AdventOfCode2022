
task = open("./5/example.txt","r")
# task = open("./5/task.txt","r")

# prepare table 5x5
rows, cols = (5, 5)
arr = [[0]*cols]*rows

arr.append([1]*cols)
arr.insert(0,[2]*cols)

def DisplayArray(dispArr):
    for dispRow in dispArr:
        print(dispRow)

DisplayArray(arr)


task.close()