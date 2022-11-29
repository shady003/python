a = 5
b = 2
try:
    print("resorce open")
    print(a/b)
    num = int(input('Enter any number'))
    print(num)
except ZeroDivisionError as e:
    print('Error:', e)
    print('hey you cant divide num by 0')
except ValueError as e :
    print("Invalid Input")
except Exception as e :
    print('Something went wrong')
finally:
    print('resource closed')

print('Bye')