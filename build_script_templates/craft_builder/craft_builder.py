# Weapon file generator

import csv
import os
import shutil
import sys

# Deletes old files
if os.path.exists("cities"):
    shutil.rmtree('cities')
if os.path.exists("crafts"):
    shutil.rmtree('crafts')

#Verifying exitance of folders

if not os.path.exists("cities"):
    os.makedirs("cities")

if not os.path.exists("crafts"):
    os.makedirs("crafts")    

def file_csv_reader(csv_filename):

    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)

        # Line number counter
        line_num = 0

        # Iteration of each row in csv
        for row in reader:

            # Ignores header
            if line_num != 0 and row[1] != "":
                craft_filename = row[0]
                craft_filename_dat = row[0] + ".dat"
                craft_name = row[1]
                craft_execution = row[2]
                craft_city = row[3]    
                craft_requirements = []
                
                for i in range(4, 15 + 1):
                    craft_requirements.append(row[i])
                cost = row[16]
                level = row[17]

                if not craft_city == "":

                    if not os.path.exists("cities/" + craft_city):
                        os.makedirs("cities/" + craft_city)

                    if not os.path.exists("crafts/"):
                        os.makedirs("crafts/")

                    # Crafts.dat file
                    myCraftsDatFile = open("cities/" + craft_city + "/crafts.dat", 'a')

                myCraftsFile = open("crafts/" + craft_filename_dat, 'w')            

                ### Writing each crafts file ###

                # Line 1: The itemname

                myCraftsFile.write('"' + craft_name + '"\r\n')

                # Line 2: Class restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 3: Race restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 4: Divinity restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 5: STR restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 6: INT restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 7: AGI restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 8: END restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 9: WIS restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 10: CHR restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 11: Area restriction to craft. Ignored for now

                myCraftsFile.write('"' + '"\r\n')

                # Line 12: Execution text

                myCraftsFile.write('"' + craft_execution + '\r\n')

                # Line 13: One time use

                myCraftsFile.write('"' + '"\r\n')

                # Line 14-18: Reserved

                for i in range(14, 18 + 1):
                    myCraftsFile.write('"' + '"\r\n')

                # Rest of the lines are the craft ingredients

                for item in craft_requirements:
                    if item != "":
                        myCraftsFile.write('"' + item + '"\r\n')

                myCraftsFile.close()

                ### Crafts.dat file ###

                # Item
                if not craft_city == "":
                    myCraftsDatFile.write('"' + craft_filename + '"\r\n')

                    # Price
                    myCraftsDatFile.write('"' + cost + '"\r\n')

                    # Level
                    myCraftsDatFile.write('"' + level + '"\r\n')


                    myCraftsDatFile.close()
            line_num += 1

filename_csv = str(sys.argv[1])

file_csv_reader(filename_csv)


