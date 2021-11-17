class matrix:

    def __init__(self, m):
        self.matrix = m

    def matrixToArray(self):
        lst = [self.matrix[0], self.matrix[1], self.matrix[2]]
        return lst

    def printMatrix(self):
        for i in range(0, len(self.matrix)):
            print(self.matrix[i])

    def addMatrix(self, lst):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + lst[i][j]

        self.printMatrix()

    def subtractMatrix(self, lst):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] - lst[i][j]

        self.printMatrix()

    def multiplyMatrix(self, lst):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] * lst[i][j]

        self.printMatrix()

    def divideMatrix(self, lst):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] / lst[i][j]

        self.printMatrix()

    def powMatrix(self, pow):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] ** pow

        self.printMatrix()

    def determinant(self):
        row1 = self.matrix[0]
        row2 = self.matrix[1]
        row3 = self.matrix[2]
        determinantR = (row1[0]*row2[1]*row3[2])+(row1[1]*row2[2]*row3[0])+(row1[2]*row2[0]*row3[1])
        determinantL = (row3[0]*row2[1]*row1[2])+(row3[1]*row2[2]*row1[0])+(row3[2]*row2[0]*row1[1])

        determinant = determinantR-determinantL
        return determinant

    def identity(self):
        lst = [[1,0,0],[0,1,0],[0,0,1]]
        return lst
