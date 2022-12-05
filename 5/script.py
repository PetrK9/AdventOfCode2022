
task = open("./5/example.txt","r")
# task = open("./5/task.txt","r")

# prepare table 5x5

# count, from, to
RawWarehouse = []
Warehouse = []
comands = []
comandsAdress = [1,3,5]


arr = [[0]*cols]*rows

arr.append([1]*cols)
arr.insert(0,[2]*cols)

def DisplayArray(dispArr):
    for dispRow in dispArr:
        print(dispRow)

def prepareWarehouse():
    rows = len(RawWarehouse)
    cols = len(RawWarehouse)

def prepareData():
    
    prepareComandTable = False

    for row in task:

        if prepareComandTable:
            currComRowSplit = row.split(' ')
            currComand = []
            
            for index in comandsAdress:
                currComand.append(currComRowSplit[index].strip())

            comands.append(currComand)
            
        if not prepareComandTable:
            if row.strip():
                RawWarehouse.append(row.replace('\n', ''))
            else:
                prepareComandTable = True

            
        
            



prepareData()
DisplayArray(RawWarehouse)
print("="*10)
DisplayArray(comands)


task.close()