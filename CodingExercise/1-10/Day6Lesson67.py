filenames = ['a','b','c']

for f in filenames:
    path = "Files/" + f + ".txt"
    files = open(path, 'r')
    print(files.read())
    files.close()