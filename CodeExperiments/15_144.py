import glob
import csv
import shutil
import webbrowser

#glob
myfiles = glob.glob("../Init/Files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())
#csv
with open("Files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(row[1])
#shutil
shutil.make_archive("Files/output","zip","../CodingExercise/1-10/Files")

#webbrowser
user_term = input("Enter a search terms: ")

webbrowser.open("https://google.com/search?q=" + user_term)
