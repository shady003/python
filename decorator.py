def div(a, b):
    return (a/b)


def add(a, b):
    return a+b


def smart_div(div):
    def change(a, b):
        if a < b:
            a, b = b, a
        return div(a, b)
    return change


def add2(add):
    def chng(a, b):
        b = b + 2
        return add(a, b)
    return chng

add = add2(add)
div = smart_div(div)
print(div(2, 4))
print(add(2, 4))
