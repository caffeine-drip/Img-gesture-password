def namech(ss):
    fobj = open("name.txt", 'r')
    f=fobj.readline()
    if f==ss:
        return 1
    else:
        return 0
    fobj.close()
