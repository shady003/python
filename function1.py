# def fun_name():
#     pass
#  contniue by lecture 32
def greet():
    print('Hello', 'Good Morning')
    # print('Good Morning')

# for i in range(0,10):
#     greet()
def add_sub(n=0, n2=0) :
    return int(n)+int(n2), int(n)-int(n2)
x,y = add_sub(3,5)
# print(type(x))
print(x, y)
# Lecture #33
# call by value
def update(x):

    x = 8
    print(x)
def lst_update(list):
    print('old', list)
    list[1] = 25
    print('From_function', list)
x = 5
update(x)
print(x)
list = [20, 20, 20]
lst_update(list)
print('base_one', list)
# lacture 34 ___ types of arguments
def sum(*b):   # formal argument
        c = 0
        for i in b:
            c += i
        print(c)
sum(5, 6, 7, 8)
# Actual argument
def person(name,age = 18):
    print(name)
    print(age - 3)
person(age=22,name='Saurabh')
def add(a, *b  ):           # /*b can hold list of nos.*/
    c = a
    for i in b:
        c += i
    print(c)
add(5, 6, 34, 78)