from zipfile import ZipFile
f = ZipFile("test.zip",'w')
f.write("f1.txt")
f.write("f2.txt")
f.write("f3.txt")
f.close()
print("Zip file created succesfully")