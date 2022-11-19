x = input('Enter symbol for patten')
i = int(input('Input no. for matrix '))
j = 1
for j in range(1, i*i+1):
    if j % i == 0:
        print(x, " ")
        j += 1
    else:
        print(x, ' ', end="")
        j += 1
