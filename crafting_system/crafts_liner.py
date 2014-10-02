import csv
import os
import shutil
import sys

for root, dirs, files in os.walk("cities"):
    for name in files:
        if name.endswith((".dat")):

            directory = root.split(os.path.sep)[-1]
            #print directory

            if directory != "cities":

                filename = "cities/" + str(directory) + "/" + name
                print filename

                with open(filename, 'r') as f:
                    flength = len(f.readlines())

                print flength

                myCraftsDatFile = open(filename, 'a')

                for i in range(flength, 30):
                    myCraftsDatFile.write('""' + '\r\n')

                myCraftsDatFile.close()