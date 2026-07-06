f = open('abc.txt')
data = f.readlines()
print(data)
for x in data:
    print(x, end='')
print(type(data))
f.close()