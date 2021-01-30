def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(4))

x = "goodbye"

# if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be goodbye"

file = open("books.txt")
cont = file.readlines()
for title in cont:
    print(title[0] + str(len(title) - 1))
file.close()

def fnone():
    print('hola')
    

print(fnone())
    
dt = {"uno":1, "dos":2 , "lista":{"uno": 1,"dos":2}, 1:1}
1 in dt
print(dt.get(8))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

tupla = 1,2,3,4,5,(1,2,3)
type(tupla)
print(tupla[5])


square = list(range(20))

print(square[3:6])
print(square[1:])
print(square)

print(square[::2])
print(square[2:8:3])
print



square = list(range(20))
print(square[7:5:-1])
print(square)

cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i ** 2 for i in range(10) if i % 2 == 0]
print(evens)