def div(a, b):
    return (a/b)

def smart_div(div):
    def change(a, b):
        if a < b:
            a, b = b, a
        return div(a, b)
    return change


div = smart_div(div)
print(div(2, 4))
