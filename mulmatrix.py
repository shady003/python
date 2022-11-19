from numpy import *
mat = matrix('1 2 3 ; 4 5 6')
mat2 = matrix('1 2 4 ; 3 4 5 ')
mat3 = mat * mat2
print(mat3)