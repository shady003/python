# else for, for  loop
num = int(input("enter number to check prime"))
for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print('Prime')
    