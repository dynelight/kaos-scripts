# Room-Monster linker

import csv
import os
import sys
import fileinput

csv_file = str(sys.argv[1])
rooms_folder = str(sys.argv[2])

with open(csv_file, 'r') as f:
    reader = csv.reader(f)

    # Iteration of each row in csv
    line_num = 0


    for row in reader:

        # Ignores header
        if line_num != 0:

            row_inside = 0 

            room_number = row[row_inside]
            row_inside += 1


            filename = rooms_folder + "/" + room_number + ".rm"

            room_new_file = ""

            for count, line in enumerate(fileinput.input(filename, inplace=True)):
                if count >= 83 and count <= 100:  # Python counts from 0
                    line = '"' + row[row_inside] + '"' + "\r\n"
                    row_inside += 1        
                sys.stdout.write(line)

        line_num += 1