import numpy as np
import csv

dimension = set()

with open('unesco_langlang_20120722_iso639-3.txt') as txt:
    for line in txt:
        line = line.split()
        #print ("row")
        if int(line[2]) > 1000:
            dimension.add(line[1])
            dimension.add(line[0])

        #print (aline)
    #print (dimension)

name = list(dimension)
print(len(name))

lang_matrix = np.zeros(shape=(len(name),len(name)))

with open('unesco_langlang_20120722_iso639-3.txt') as txt:
    for line in txt:
        row = line.split()
        #print(lang_matrix[(name.index(row[0]), name.index(row[1]))])
        #print(row)
        if int(row[2]) > 1000:
            lang_matrix[(name.index(row[0]), name.index(row[1]))] = float(row[2])


np.savetxt("matrix.txt", lang_matrix,  delimiter=',', newline='],\n[', header='[', footer=']', comments='')


# csv = np.genfromtxt('lang.csv',delimiter=',')

# dimension = csv.shape
# row = dimension[0]

# lang_matrix = np.zeros(shape=(row,row))

# length = set()
# with open('relation.txt', encoding='utf-8', mode='w+') as f:



