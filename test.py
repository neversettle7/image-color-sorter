nomefile = "testo"


def openfile(nomefile):
    f = open(nomefile, 'r')
    return f


def writeinfo(f):
    f = f.read()
    print (f)
    return


f = openfile(nomefile)
writeinfo(f)
