def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('Vamsi', age=22, city="Bangalore", mob=987654)
