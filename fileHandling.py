file = open('data', 'w') # write
# file = open('data', 'a') # append
file.write('Hello World')
file.close() #close file
file = open('data', 'r') # read
# print(file.read())
for i in file:
    print(i)
