# Weapon file generator

import csv
import os
import sys

with open(str(sys.argv[1]), 'r') as f:
    reader = csv.reader(f)

    # Line number counter
    line_num = 0

    # Iteration of each row in csv
    for row in reader:

        # Ignores header
        if line_num != 0:

            # Atribues
            # Name  Reference Number    Location from Reference Room Number Room Title  Room Enter  Room Description    Gfx

            directory = "rooms"

            room_number = row[0]   
            room_name = row[1]
            room_type = row[2]      
            special = row[3]
            city_name = row[4]   
            room_enter = row[5]
            room_description = row[6]

            # Calculating 0s on room file
            gfx = row[7].zfill(6)

            room_exit_n = row[8]
            room_exit_w = row[9]
            room_exit_e = row[10]
            room_exit_s = row[11]            
            room_exit_u = row[12]
            room_exit_d = row[13]

            outside_area = row[14]
            light_needed = row[15]

            toRead = row[16]

            if not os.path.exists(directory):
                os.makedirs(directory)

            filename = room_number + ".rm"

            myFile = open(directory + "/" + filename, 'w')

            # Line 1: Room number

            myFile.write('"' + room_number + '"\r\n')

            # Line 2: Room name

            myFile.write('"' + room_name + '"\r\n')

            # Line 3: Area Type 

            myFile.write('"' + room_type + '"\r\n')

            # Line 4: Short description

            myFile.write('"' + room_enter + '"\r\n')    

            # Line 5: Image

            myFile.write('"' + gfx + '"\r\n') 

            # Line 6: Level   
            # TODO

            myFile.write('"' + '"\r\n') 

            # Line 7: Special  

            myFile.write('"' + special + '"\r\n') 

            # Line 8: City name

            myFile.write('"' + city_name + '"\r\n') 

            # Line 9: Hint
            myFile.write('"' + '"\r\n') 

            # Lines 10-17: Hints. Not used.  

            for line in range(10, 17 + 1):
                myFile.write('"' + '"\r\n') 

            # Lines 18-47: Exits. 

            # Lines 18-20

            if room_exit_n != "":
                myFile.write('"Normal"\r\n')       
                myFile.write('"' + room_exit_n + '"\r\n') 
                myFile.write('"' + '"\r\n') 
            else: 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 

            # Lines 21-23

            if room_exit_w != "":
                  myFile.write('"Normal"\r\n')       
                  myFile.write('"' + room_exit_w + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
            else: 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 

            # Lines 24-26

            if room_exit_e != "":
                  myFile.write('"Normal"\r\n')       
                  myFile.write('"' + room_exit_e + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
            else: 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n')                   

            # Lines 27-29

            if room_exit_s != "":
                  myFile.write('"Normal"\r\n')       
                  myFile.write('"' + room_exit_s + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
            else: 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 

            # Lines 30-41: Ignored for now

            for i in range(30, 41 + 1):
                  myFile.write('"' + '"\r\n')                   

            # Lines 42-44

            if room_exit_u != "":
                  myFile.write('"Normal"\r\n')       
                  myFile.write('"' + room_exit_u + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
            else: 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 

            # Lines 45-47

            if room_exit_d != "":
                  myFile.write('"Normal"\r\n')       
                  myFile.write('"' + room_exit_d + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
            else: 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 
                  myFile.write('"' + '"\r\n') 

            # Lines 48-101
            for i in range(48, 101 + 1):
                  myFile.write('"' + '"\r\n')   

            # Line 102: Always "no"
            myFile.write('"no"\r\n') 

            # Lines 103-109
            for i in range(103, 109 + 1):
                  myFile.write('"' + '"\r\n')   

            # Line 110: Outside area
            myFile.write('"' + outside_area + '"\r\n') 

            # Line 111: Light source 
            myFile.write('"' + light_needed + '"\r\n') 

            # Line 112: Long Description 
            myFile.write('"' + room_description + '"\r\n') 

            # Lines 113-199
            for i in range(113, 199 + 1):
                  myFile.write('"' + '"\r\n')     

            # Line 200: Always "0"
            myFile.write('"0"\r\n') 

            # Line 201: Always "0"
            myFile.write('"0"\r\n') 

            # Lines 202-250
            for i in range(202, 250 + 1):
                  myFile.write('"' + '"\r\n')                      

            myFile.close()
        line_num += 1
