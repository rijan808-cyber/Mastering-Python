from zipfile import ZipFile
f = ZipFile("test.zip",'r')
name = f.namelist()
print(name)
for x in name:
    print(f'File Name: {x}')
    f1 = open(x,'r')
    data = f1.read()
    print(data)
    print("__"*30)
    print()
    f1.close()
f.close()
print("Zip file read succesfully")