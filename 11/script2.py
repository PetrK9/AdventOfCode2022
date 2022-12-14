from tqdm import tqdm
import time


class ItemCls:
    def __init__(self, Value):
        self.facors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.facValConta = []
        self.facValCount = []

        self.updateNumber(Value)

    def plusNumber(self, Number):
        self.updateNumber(self.returnNumber()+Number)

    def updateNumber(self, Value):
        self.updateFactor(Value)
        self.devideIntoFactor(Value)

    def timesTwo(self):
        for i in range(0, len(self.facValCount)):
            self.facValCount[i] *= 2

    def timesNumber(self, Number):
        if (Number in self.facValConta):
            self.facValCount[self.facValConta.index(Number)] += 1
        else:
            self.facValConta.append(Number)
            self.facValCount.append(1)

    def testDevisible(self, Value):
        if (Value in self.facValConta):
            return True
        else:
            return False

    def devideIntoFactor(self, Value):
        self.facValConta = []
        self.facValCount = []

        for facor in self.facors:
            if (Value % facor == 0):
                self.facValConta.append(facor)
                self.facValCount.append(1)
                Value //= facor
                while Value % facor == 0:
                    Value //= facor
                    self.facValCount[-1] += 1
            if Value == 1:
                break

    def returnNumber(self):
        returnedValue = 1
        for i in range(0, len(self.facValConta)):
            for j in range(0, self.facValCount[i]):
                returnedValue = returnedValue*self.facValConta[i]

        return returnedValue

    def updateFactor(self, Value):
        if (Value > max(self.facors)):
            for i in range(max(self.facors)+1, (Value)):
                NotDevided = True
                for j in self.facors:
                    if (i % j == 0):
                        NotDevided = False
                        break
                if NotDevided:
                    self.facors.append(i)


class Monkey:
    def __init__(self, ID):
        self.items = []
        self.itemObj = []
        self.id = ID
        self.optType = ''
        self.optVal = 0  # times/plus value
        self.test = 0  # test DevidedNumber
        self.testTrueMonkey = 0
        self.testFalseMonkey = 0
        self.inspecItem = 0

    def inspectItemsBIG(self):
        moveItemToMonkey = []
        moveItem = []
        for item in self.itemObj:
            self.inspecItem += 1
            optVal = self.optVal
            match self.optType:
                case "+":
                    item.plusNumber(optVal)
                case "*":
                    item.timesNumber(optVal)
                case "secExp":
                    item.timesTwo()

            moveItem.append(item)
            if (item.testDevisible(self.test)):
                moveItemToMonkey.append(self.testTrueMonkey)
            else:
                moveItemToMonkey.append(self.testFalseMonkey)

        self.itemObj = []

        return [moveItemToMonkey, moveItem]

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

    def printInspectiom(self):
        print(f"Monkey {self.id} inspected items {self.inspecItem} times.")

    def printMonkey(self):
        print(f"Monkey {self.id}:")
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
                NewMonkey.itemObj.append(ItemCls(int(Item)))

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
    dipsReportIn = [1, 20, 1000, 2000, 3000,
                    4000, 5000, 6000, 7000, 8000, 9000, 10000]
    dipsReportIn.sort(reverse=True)
    checkNumber = dipsReportIn.pop()

    monkeyList = monkeyParser()
    t = time.time()
    for j in tqdm(range(0, 21), desc="Monkey working!"):
        for monkey in monkeyList:
            trasferItemsBIG = monkey.inspectItemsBIG()
            for i in range(0, len(trasferItemsBIG[0])):
                # For monkey on addres form trasfered item add new item
                monkeyList[trasferItemsBIG[0][i]].itemObj.append(trasferItemsBIG[1][i])

        if (j+1 == checkNumber):
            print(f"== After round {j+1} ==")
            for monkey in monkeyList:
                monkey.printInspectiom()
            checkNumber = dipsReportIn.pop()
        pass
    print(f"Runtime: {time.time() - t}")

    MovementCount = []
    for monkey in monkeyList:
        MovementCount.append(monkey.inspecItem)

    MovementCount.sort()

    print("I am done")
