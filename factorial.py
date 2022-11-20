def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


x = int(input('Enter the value for factorial\n>>>'))
result = fact(x)
print("factorial of {} is {}".format(x, result))


