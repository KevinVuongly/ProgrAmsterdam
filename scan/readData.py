import csv

class cars:
    def __init__(self, gridSize, puzzle):
        self.gridSize = gridSize

        self.changeable = []
        self.fixed = []
        self.richting = []
        self.lengte = []
        
        with open(puzzle) as csvfile:
            readcsv = csv.reader(csvfile, delimiter = ",")

            for row in readcsv:
                if row[2] == 0:
                    self.changeable.append(row[0])
                    self.fixed.append(row[1])
                else:
                    self.changeable.append(row[1])
                    self.fixed.append(row[0])

                self.richting.append(row[2])
                self.lengte.append(row[3])

class move:
    
