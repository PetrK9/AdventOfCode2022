from tqdm import tqdm
import time

class Monkey:
    def __init__(self, ID):
        self.items = []
        self.id = ID
        self.optType = ''
        self.optVal = 0
        self.test = 0
        self.testTrueMonkey = 0
        self.testFalseMonkey = 0
        self.inspecItem = 0

    def inspectItems(self):
        moveItemToMonkey = []
        moveItem = []
        for item in self.items:
            self.inspecItem += 1
            ItemWorrLev = self._calcItemWorr(item)
            moveItem.append(ItemWorrLev)
            if (ItemWorrLev % self.test == 0):
                moveItemToMonkey.append(self.testTrueMonkey)
            else:
                moveItemToMonkey.append(self.testFalseMonkey)

        self.items = []

        return [moveItemToMonkey, moveItem]

    def _calcItemWorr(self, item):
        optVal = self.optVal
        match self.optType:
            case "+":
                return ((item + optVal) // 3)
            case "*":
                return ((item * optVal) // 3)
            case "secExp":
                return ((item * item) // 3)
        
        

    def printMonkey(self):
        print(f"Monkey {self.id}:")
        itemStr = ''
        for item in self.items:
            itemStr += str(item) + ', '
        print(f"\tStarting items: {itemStr[:-2]}")
        if (self.optType == "secExp"):
            print(f"\tOperation: new = old * old")
        else:
            print(f"\tOperation: new = old {self.optType} {self.optVal}")
        print(f"\tTest: divisible by {self.test}")
        print(f"\t\tIf true: throw to monkey {self.testTrueMonkey}")
        print(f"\t\tIf false: : throw to monkey {self.testFalseMonkey}")
        print(f"\tMoved item: {self.inspecItem}")


def monkeyParser():
    task = open("./11/example.txt", "r")
    # task = open("./11/task.txt","r")

    monekyList = []

    for row in task:
        CleanRow = row.strip()
        RwSlBySpc = CleanRow.split(" ")
        if ("Monkey " in CleanRow):
            NewMonkey = Monkey(RwSlBySpc[1][:-1])

        if ("Starting items:" in CleanRow):
            for Item in CleanRow[16:].split(', '):
                NewMonkey.items.append(int(Item))

        if ("Operation:" in CleanRow):
            if (RwSlBySpc[-1] == "old"):
                NewMonkey.optType = "secExp"
            else:
                NewMonkey.optVal = int(RwSlBySpc[-1])
                NewMonkey.optType = RwSlBySpc[-2]

        if ("Test:" in CleanRow):
            NewMonkey.test = int(RwSlBySpc[-1])

        if ("If true:" in CleanRow):
            NewMonkey.testTrueMonkey = int(RwSlBySpc[-1])

        if ("If false:" in CleanRow):
            NewMonkey.testFalseMonkey = int(RwSlBySpc[-1])

        if (not CleanRow):
            monekyList.append(NewMonkey)

    monekyList.append(NewMonkey)

    task.close()
    return monekyList


if __name__ == "__main__":
    monkeyList = monkeyParser()
    t = time.time()
    for j in tqdm(range(0, 20), desc="Monkey working!" ):
         
        for monkey in monkeyList:
            trasferItems = monkey.inspectItems()
            for i in range(0, len(trasferItems[0])):
                # For monkey on addres form trasfered item add new item
                monkeyList[trasferItems[0][i]].items.append(trasferItems[1][i])
    print(f"Runtime: {time.time() - t}")

    for monkey in monkeyList:
        monkey.printMonkey()

    MovementCount = []

    for monkey in monkeyList:
        MovementCount.append(monkey.inspecItem)
    
    MovementCount.sort()

    print(f"Bonkey business id {MovementCount[-1]*MovementCount[-2]}")

    print("I am done")
