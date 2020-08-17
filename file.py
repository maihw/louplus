name = input("enter the file name: ")
fobj = open(name)
print(fobj.read())
fobj.close()
