f = open('abc.txt')
data = f.readline()
print(data, end='')
data1 = f.readline()
print(data1, end='')
print(type(data1))
f.close