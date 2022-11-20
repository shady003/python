def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


x = int(input('Enter the value for factorial\n>>>'))
result = fact(x)
print("factorial of {} is {}".format(x, result))

# by recursion


def facto(num):
    if num == 0:
        return 1
    return num * fact(num-1)


x = int(input('enter no for fact\n>>>'))
fac = facto(x)
print('factorial of {} by recursion method is {}'.format(x, fac) )

