# Weapon file generator

import csv
import os

with open('craftareas.csv', 'r') as f:
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

            room_name = row[0]
            room_number = row[1]            
            room_title = row[2]
            room_enter = row[3]
            room_description = row[4]

            # Calculating 0s on room file
            gfx = row[5].zfill(6)

            room_exit_n = row[6]
            room_exit_w = row[7]
            room_exit_e = row[8]
            room_exit_s = row[9]            
            room_exit_u = row[10]
            room_exit_d = row[11]

            toRead = row[12]

            print room_title

            if toRead:

                if not os.path.exists(directory):
                    os.makedirs(directory)

                    filename = room_number + ".rm"

                    myFile = open(directory + "/" + filename, 'w')

                		# Line 1: Room number

                    myFile.write('"' + room_number + '"\r\n')

                    # Line 2: Room name

                    myFile.write('"' + room_title + '"\r\n')

                    # Line 3: Area Type 
                    # TODO

                    myFile.write('"' + '"\r\n')

                    # Line 4: Short description

                    myFile.write('"' + room_enter + '"\r\n')    

                    # Line 5: Image

                    myFile.write('"' + gfx + '"\r\n') 

                    # Line 6: Level   
                    # TODO

                    myFile.write('"' + '"\r\n') 

                    # Line 7: Special  
                    # TODO 

                    myFile.write('"Craft' + '"\r\n') 

                    # Line 8: City name
                    # TODO: Don't understand difference. Can it be the same as the craft city? 

                    myFile.write('"' + room_name + '"\r\n') 

                    # Line 9: Hint
                    myFile.write('"' + '"\r\n') 

                    # Lines 10-17: Hints. Not used.  

                    for line in range(10, 17 + 1):
                        myFile.write('"' + '"\r\n') 

                    # Lines 18-47: Exits. 

                    # Lines 18-20

                    if room_exit_n != "":
                        myFile.write('"normal"\r\n')       
                        myFile.write('"' + room_exit_n + '"\r\n') 
                        myFile.write('"' + '"\r\n') 
                    else: 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 

                    # Lines 21-23

                    if room_exit_w != "":
                          myFile.write('"normal"\r\n')       
                          myFile.write('"' + room_exit_w + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                    else: 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 

                    # Lines 24-26

                    if room_exit_e != "":
                          myFile.write('"normal"\r\n')       
                          myFile.write('"' + room_exit_e + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                    else: 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n')                   

                    # Lines 27-29

                    if room_exit_s != "":
                          myFile.write('"normal"\r\n')       
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
                          myFile.write('"normal"\r\n')       
                          myFile.write('"' + room_exit_u + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                    else: 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 

                    # Lines 45-47

                    if room_exit_d != "":
                          myFile.write('"normal"\r\n')       
                          myFile.write('"' + room_exit_d + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                    else: 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 
                          myFile.write('"' + '"\r\n') 

                    # Lines 48-111
                    for i in range(48, 111 + 1):
                          myFile.write('"' + '"\r\n')    

                    # Line 112: Long Description 
                    myFile.write('"' + room_description + '"\r\n') 

                    # Lines 48-250
                    for i in range(113, 250 + 1):
                          myFile.write('"' + '"\r\n')                      

                    myFile.close()
        line_num += 1