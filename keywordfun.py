

def person(name, **data): # keyworded variable length
    print(name)
    for i, j in data.items():
        print(i, j)


person('Saurabh', age=22, city='Gorakhpur', mob=91400.)