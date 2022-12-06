
task = open("./5/example.txt","r")
# task = open("./5/task.txt","r")

# prepare table 5x5

# count, from, to
RawWarehouse = []
Warehouse = []
comands = []
comandsAdress = [1,3,5]


def DisplayArray(dispArr):
    for dispRow in dispArr:
        print(dispRow)

def prepareWarehouse(RawData):
    rows = len(RawData)
    cols = int(len(RawData[-1].split(' '))/3)

    Warehouse = [[0 for i in range(cols)] for j in range(rows)]

    RawDataInRow = RawData[-1].split(' ')

    for j in range(0, cols):
        Warehouse[-1][j] = RawDataInRow[j*3+1]

    for i in range(0, rows - 1):
        RawDataInRow = RawData[i].split(' ')
        jj = 0
        for j in range(0, cols):
            if RawDataInRow[jj] == '':
                Warehouse[i][j] = '0'
                jj += 4
            else:
                Warehouse[i][j] = RawDataInRow[jj][1]
                jj += 1
            


    return Warehouse
    

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
Warehouse = prepareWarehouse(RawWarehouse)
print("="*3 + "Warehouse" + "="*3)
DisplayArray(Warehouse)
print("="*10)
DisplayArray(comands)


task.close()