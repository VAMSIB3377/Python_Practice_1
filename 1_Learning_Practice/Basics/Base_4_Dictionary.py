# Dictionary is a set of Key Value Pairs

Dict = {1:"abc", 2:"bcd", 3:"cde"}

keys = {10, 20 ,30}

values = ['xyz', 'wxy', 'vwx']

data = dict(zip(keys, values))

print(Dict)
print(Dict.keys())
print(Dict.values())
print(Dict.items())
print(Dict[2])
print(Dict[1])
print(Dict.get(3,'Not Found'))
print(Dict.get(5,'Not Found'))
print(data)

print(data[20])

data['40'] = 'uvw'

print(data)

del data[30]
print(data)




print("\n\n\n")
prog = {'JS':'Atom', 'C#':'VS', 'Python':['Pycharm','Sublime'], 'Java':{'JSE':'Netbeans','JEE':'Eclipse'} }

print(prog)

print(prog['JS'])
print(prog['C#'])
print(prog['Python'])
print(prog['Python'][0])
print(prog['Java'])
print(prog['Java']['JSE'])
print(prog['Java']['JEE'])



