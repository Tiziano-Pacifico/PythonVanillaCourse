filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for f in filenames:
    path = "Files/" + f
    file = open(path, 'w')
    file.writelines("Hello")
    file.close()