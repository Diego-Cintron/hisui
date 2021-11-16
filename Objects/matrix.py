class matrix:

    def __init__(self, m):
        self.matrix = []
        arr = []
        for i in range(0, len(m)):
            arr.append(m[i])
        self.matrix.append(arr)

    def addRow(self, row):
        while len(row) != len(self.matrix[0]):
            row.append(0)

        self.matrix.append(row)

    def addCol(self, row):
        while len(row) != len(self.matrix):
            row.append(0)

        for i in range(0,len(self.matrix)):
            self.matrix[i].append(row[i])

    def printMatrix(self):
        for i in range(0, len(self.matrix)):
            print(self.matrix[i])

    def addMatrix(self,matrix2):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + matrix2[i][j]

        self.printMatrix()

    def subtractMatrix(self,matrix2):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] - matrix2[i][j]

        self.printMatrix()

    def multiplyMatrix(self,matrix2):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] * matrix2[i][j]

        self.printMatrix()

    def divideMatrix(self,matrix2):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] / matrix2[i][j]

        self.printMatrix()

    def powMatrix(self,pow):
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] ** pow

        self.printMatrix()

