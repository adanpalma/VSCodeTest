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
cont = enumerate(cont)
for title in cont:
    print(title[0] + str(len(title) - 1))
file.close()


def fnone():
    print("hola")


print(fnone())

dt = {"uno": 1, "dos": 2, "lista": {"uno": 1, "dos": 2}, 1: 1}
1 in dt
print(dt.get(8))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

tupla = 1, 2, 3, 4, 5, (1, 2, 3)
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

cubes = [i ** 3 for i in range(5)]
print(cubes)

evens = [i ** 2 for i in range(10) if i % 2 == 0]
print(evens)

print("{a},{b},{c}".format(a=1, b=2, c=3))

print("Hello me".replace("me", "jajajajaja"))

print("estas es una cadena y hago esto".split(" "))
print(sum(range(1000)))

if all(range(1, 1000)):
    print("si")

nums = [55, 44, 33, 22, 11]
nums = enumerate(nums)
for v in nums:
    print(type(v))

file = open("books.txt")
cont = file.readlines()
cont = enumerate(cont)
for title in cont:
    print(title[1])
file.close()

nums = [-1, 2, -3, 4, -5]
print(nums[0:0])
print([abs(i) < 3 for i in nums])
if all([abs(i) < 3 for i in nums]):
    print(1)
else:
    print(2)

text = ""
with open("books.txt") as f:
    text = f.read()
print(text)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
txt = txt.split(" ")
maxlong = max([len(i) for i in txt])
for w in txt:
    if len(w) == maxlong:
        print(w)
