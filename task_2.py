class Matrix:
    def __init__(self,n,*args):
        self.n = n
        self.matrix = []
        for i in range(0,n**2,n):
            self.matrix.append(list(args[i:i+n]))


    def get_matrix_(self):  return self.matrix

    def find_det(self, n, mat):
        if n == 1:
            return mat[0][0]
        det = 0
        for i in range(n):
            det += (-1)**(i+2) * mat[0][i] * self.find_det(n-1,list(map(lambda x: x[:i]+x[i+1:], mat))[1:])
        return det

    def compare(self, Matrix):
        T1 = self.find_det(self.n,self.matrix)
        T2 = self.find_det(Matrix.n, Matrix.matrix)
        if T1>T2:
            print("Matrix 1 bigger")
        elif T1<T2:
            print("Matrix 2 bigger")
        else:
            print("Matrix 1 is equal to the 2")
    def summarize(self, Matrix):
        if self.n != Matrix.n:  
            print("Matrices cannot be summarized")
            return False
        else:
            C = [0 for i in range(self.n)] 
            for i in range(self.n):
                C[i] = list(map(sum, zip(Matrix.matrix[i],self.matrix[i])))
            return C
    def multiply(self,Matrix):
        if self.n != Matrix.n:  
            print("Matrices cannot be multiplyed")
            return False
        else:
            C = [[0 for i in range(self.n)] for i in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    sum = 0
                    for k in range(self.n):
                        sum +=  self.matrix[i][k]*Matrix.matrix[k][j]
                    C[i][j] = sum
            return C
        pass

a = Matrix(2,1,1,2,2)
b = Matrix(2,1,2,2,2)

a.compare(b)
print("a+b:", a.summarize(b))
print("a*b:", a.multiply(b))
