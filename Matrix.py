from numpy import *
# arr = linspace(1, 10, 10, int)
# matrix = array([
#                 [arange(1, 6, 1, int)], [arange(8, 16, 1, int)]
#                 ])
matrix1 = array([[1, 2, 3, 4, 5, 6], [5, 6, 7, 8, 9, 10]])
matrix2 = matrix1.flatten()
matrix3 = matrix2.reshape(2, 2, 3)
# print(matrix3)
# print(matrix2)
# print(matrix1)
mat = matrix(matrix1)
m = matrix('1, 2, 4, 5 ; 6, 7, 8, 9 ;6, 7, 8, 9')
# mat = matrix('1 2 3 ; 4 5 6') //not working in only this project proof in malmatrix:project
# mat2 = matrix('1 2 4 ; 3 4 5 ')
# mat3 = mat * mat2  // Ending here
# print(mat3)
m2 = m.copy()
print(m)
# print(diagonal(m))
# print(m.min())
# print(m)
# print(asmatrix(matrix1))
# print(matrix1.ndim)
# print(matrix1.shape)
# print(matrix1.size)
