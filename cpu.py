fobj = open("/proc/cpuinfo")
for i in fobj:
    print(fobj.readline)
fobj.close()
