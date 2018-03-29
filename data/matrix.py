import numpy as np
import csv

dimension = set()

with open('lang2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print ("row")
        dimension.add(row[1])
        dimension.add(row[0])
        #print (aline)
    print (dimension)

name = list(dimension)

lang_matrix = np.zeros(shape=(len(name),len(name)))

with open('lang2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if lang_matrix[(name.index(row[0]), name.index(row[1]))] != 0:
            lang_matrix[(name.index(row[0]), name.index(row[1]))] += int(row[2])
            lang_matrix[(name.index(row[1]), name.index(row[0]))] += int(row[2])
        else:
            lang_matrix[(name.index(row[0]), name.index(row[1]))] = int(row[2])
            lang_matrix[(name.index(row[1]), name.index(row[0]))] = int(row[2])     


np.savetxt("matrix2.txt", lang_matrix,  delimiter=',', newline='],\n[', header='[', footer=']', comments='')


# csv = np.genfromtxt('lang.csv',delimiter=',')

# dimension = csv.shape
# row = dimension[0]

# lang_matrix = np.zeros(shape=(row,row))

# length = set()
# with open('relation.txt', encoding='utf-8', mode='w+') as f:



