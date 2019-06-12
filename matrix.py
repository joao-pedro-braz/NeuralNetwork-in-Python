import random

class Matrix():
    rows = 0
    cols = 0
    matrix = []
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        for i in range(0, rows):
            self.matrix.append([])
            for j in range(0, cols):
                self.matrix[i].append(0) 

    def fromArray(arr):
        newArray = Matrix(len(arr), 1)    
        for i in range(0, len(arr)):
            newArray.matrix[i][0] = (arr[i])
        #Matrix.mapArray(newArray, lambda x: arr[])
        return newArray

    def randomize(a):    
        random.seed(None)
        Matrix.mapMatrix(a, lambda y: y + random.uniform(-1, 1))

    def mapMatrix(a, function):
        a.matrix = list(map(lambda x: list(map(function, x)), a.matrix))
        return a

    def mapArray(a, function):
        a.matrix = list(map(function, a.matrix))

    def add(self, a):
        if(isinstance(a, Matrix)):
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.matrix[i][j] += a.matrix[i][j]
        else:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.matrix[i][j] += a

        return self.matrix

    def multiply(self, n):
        if(isinstance(n, Matrix)):
            if((self.cols) == (n.cols)):
                for i in range(0, self.rows):
                    for j in range(0, self.cols):
                        self.matrix[i][j] *= n.matrix[i][j]
                return self
            else:
                for i in range(0, self.rows):
                    for j in range(0, self.cols):
                        self.matrix[i][j] *= n.matrix[i]
                return self
        else:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.matrix[i][j] *= n
            return self

    def MatrixMultiplication(a, b):
        if (len(a.matrix[0]) == len(b.matrix)):            
                lines = a.matrix
                columns = Matrix.transpose(b).matrix              
                result = Matrix(len(lines), len(columns))
                for i in range(0, len(lines)):
                    for j in range(0, len(columns)):
                        result.matrix[i][j] = Matrix.dotMultiplication(lines[i], columns[j])
                return result
        else:
            raise ArithmeticError("Trying to multiply incompatible Matrixs")

    def transpose(a):
        b = Matrix(a.cols, a.rows)
        for i in range(0, a.cols):
            for j in range(0, a.rows):
                b.matrix[i][j] = a.matrix[j][i]
        return b

    def dotMultiplication(lines, columns):
        result_sum = 0
        for i in range(0, len(lines)):
            result_sum += lines[i] * columns[i]
        return result_sum

    def toArray(self):
        b = []
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                b.append(self.matrix[i][j])
        return b
