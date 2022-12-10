class Knot:
    def __init__(self, type):
        self.type = type
        self.x = 0
        self.y = 0
        self.visitPlaces = ['0_0']

    def move(self, direction):
        match direction:
            case "R":
                self.x += 1
            case "L":
                self.x -= 1
            case "D":
                self.y -= 1
            case "U":
                self.y += 1
        
        self._visitPlacesUpdate()

    def follow(self,Follow):
        DiffX = Follow[0] - self.x  
        DiffY = Follow[1] - self.y  

        if(DiffY == 0 or DiffX == 0):
            if(abs(DiffX) > 1):
                if DiffX > 0:
                    self.x += 1
                else:
                    self.x -= 1

            if(abs(DiffY) > 1):
                if DiffY > 0:
                    self.y += 1
                else:
                    self.y -= 1
        else:
            if(abs(DiffY) > 1 or abs(DiffX) > 1):          
                if DiffX > 0:
                    self.x += 1
                else:
                    self.x -= 1

        
                if DiffY > 0:
                    self.y += 1
                else:
                    self.y -= 1
                pass

        self._visitPlacesUpdate()  
    
    def _visitPlacesUpdate(self):
        visitString = f"{self.x}_{self.y}"
        
        if not(visitString in self.visitPlaces):
            self.visitPlaces.append(visitString)

    def visitPlacesList(self):
        return self.visitPlaces
    
    def visitPlacesCount(self):
        countOfPlaces = len(self.visitPlaces)
        return countOfPlaces
    
    def showVisitPlaces(self):
        for row in self.visitPlaces:
            print(row)

    def possition(self):
        return [self.x, self.y]

    def showPossiton(self):
        print(f"The coordinates of {self.type} is x:{self.x} ,y:{self.y} .")


if __name__ == "__main__":
    # task = open("./9/example.txt", "r")
    task = open("./9/task.txt","r")

    head = Knot('Head')
    tail = Knot('Tail')

    for row in task:
        rowAdd = row.strip().split(' ')
        for i in range(0,int(rowAdd[1])):
            head.move(rowAdd[0])
            tail.follow(head.possition())
    
    print(f"The tail visit {tail.visitPlacesCount()} places")
    

    task.close()