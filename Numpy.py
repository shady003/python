from numpy import *
# # No need to describe datatype
# arr = array([1, 2, 3, 4, 5.0], float) # Every value is conveted into float64
# print(arr.dtype)
# print(arr)
# # linspace
# brr = linspace(10, 150, 15, int)
# print(brr)
# rrr = arange(10, 150, 2, int)
# print(rrr)
# lrr = logspace(1, 40, 5, int)
# print('%.2f' % lrr[0])
# # zeros
# zrr = zeros(5, int);
# print(zrr)
# orr = ones(5, int)
# print(orr)
# Adding 5 to array
ar1 = arange(1, 6, 1, int)
ar2 = arange(6, 11, 1, int)
ar3 = ar1 + ar2
# print(ar3)
# print(sum(ar3))
# print(min(ar3))
# print(max(ar3))
# print(sin(ar3))
# print(cos(ar3))
# print(log(ar3))
# print(sort(ar3))
# print(unique(ar3))
# print(concatenate([ar3, ar1]))
# serious stuff
# arcpy = ar1.
arcpy = ar1.view()  # adrress will be changed
arcpy = ar1.copy()  # adrress will be changed and deep copy not sellow copy arcpy will not change in it
ar1[1] = 2
print(ar1)
print(arcpy)
print(id(ar1))
print(id(arcpy))
