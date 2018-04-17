import csv

class rushHour:
    def __init__(self, gridSize, puzzle):
        self.gridSize = gridSize

        with open(self.puzzle) as csvfile:
            readcsv = csv.reader(csvfile, delimiter = ",")

            for row in readcsv:
                self.x = row[0]
                self.y = row[1]
                self.richting = row[2]
                self.lengte = row[3]

        
