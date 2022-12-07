
# task = open("./5/example.txt","r")
task = open("./5/task.txt","r")

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
                currComand.append(int(currComRowSplit[index].strip()))

            comands.append(currComand)
            
        if not prepareComandTable:
            if row.strip():
                RawWarehouse.append(row.replace('\n', ''))
            else:
                prepareComandTable = True

def DoAllMovements(comandList, warehouse, typeCrane):
    for currComand in comandList:
        if(typeCrane == '9000'):
            warehouse = MoveItems(currComand,warehouse)
        if(typeCrane == '9001'):
            warehouse = MoveGroupItems(currComand,warehouse)
        # print('_'*10)
        # DisplayArray(warehouse)¨
    
    return warehouse

def MoveGroupItems(comad,warehouse):
    if(comad[0] == 1):
        return MoveItem(warehouse,comad[1]-1,comad[2]-1)
    else:
        warehouse, items = GetItems(warehouse, comad[1]-1, comad[0])
        return InserItems(warehouse,comad[2]-1,items)


def MoveItems(comad,warehouse):
    for i in range(0,comad[0]):
        warehouse = MoveItem(warehouse,comad[1]-1,comad[2]-1)
    
    return warehouse

def MoveItem(warehouse,inCol,OutColl):
    warehouse, item = GetItem(warehouse, inCol)
    return InserItem(warehouse, OutColl, item)

def GetItem(warehouse,col):
    for j in range(0, len(warehouse)):
        if warehouse[j][col] != '0':
            item = warehouse[j][col]
            warehouse[j][col] = '0'
            return warehouse, item

def InserItem(warehouse,col, item):
    if warehouse[0][col] != '0':

        warehouse.insert(0,['0' for i in range(len(warehouse[0]))] ) 
        warehouse[0][col] = item
        return warehouse

    for j in range(0, len(warehouse)):
        if warehouse[j][col] != '0':
            warehouse[j-1][col] = item
            return warehouse

def GetItems(warehouse,col, count):
    items = []
    for j in range(0, len(warehouse)):
        if warehouse[j][col] != '0':
            for k in range(0, count):
                items.append(warehouse[j+k][col])
                warehouse[j+k][col] = '0'
            
            return warehouse, items

def InserItems(warehouse,col,items):
    for j in range(0, len(warehouse)):
        if warehouse[j][col] != '0':
            for i in range(0,len(items)):
                if(j-1-i) <0:
                    warehouse.insert(0,['0' for i in range(len(warehouse[0]))] )             
                    warehouse[0][col] = items.pop()
                else:
                    warehouse[j-1-i][col] = items.pop()
            return warehouse

def PrintTopLetters(warehouse):
    message = ''
    for i in range(0,len(warehouse[0])):
        
        for j in range(0,len(warehouse)):
            if(warehouse[j][i]) != '0':
                message += warehouse[j][i]
                break

    print(message)      



prepareData()
DisplayArray(RawWarehouse)
Warehouse = prepareWarehouse(RawWarehouse)

print("="*3 + "Warehouse" + "="*3)
DisplayArray(Warehouse)
print("="*10)
WarehouseMoved = DoAllMovements(comands, Warehouse, '9000')
print("="*3 + "CrateMover 9000" + "="*3)
PrintTopLetters(WarehouseMoved)

print("="*3 + "CrateMover 9001" + "="*3)
Warehouse = prepareWarehouse(RawWarehouse)
WarehouseMoved = DoAllMovements(comands, Warehouse, '9001')
PrintTopLetters(WarehouseMoved)

# DisplayArray(comands)


task.close()