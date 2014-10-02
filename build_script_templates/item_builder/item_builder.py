# Weapon file generator

import csv
import os
import shutil
import sys

# Deletes old files
if os.path.exists("items"):
    shutil.rmtree('items')

#Verifying exitance of folders
if not os.path.exists("items"):
    os.makedirs("items")

def file_csv_reader(filename):

    with open(filename, 'r') as f:
        reader = csv.reader(f)

        # Line number counter
        line_num = 0

        # Iteration of each row in csv
        for row in reader:

            # Ignores header
            if line_num != 0 and len(row) > 0:
                # Cleans initial and ending spaces
                for i in range(0, len(row)):
                    row[0] = row[0].strip()

                print "Creating: " + row[0]

                # Atributes
                filename = row[0] + ".dat"

                itemname = row[0]     
                image = row[1]
                item_type = row[2]
                item_class = row[3]
                restrictions = row[4] 
                decked = row[5]

                bane_type = "0"
                bane_percentage = "0"
                armor = "0"                

                craft_requirements = []

                ### Weapons ###

                if item_type == "A":

                    min_damage = row[6]
                    max_damage = row[7]
                    bane_type = row[8]
                    bane_percentage = row[9]
                    item_description = row[10]

                else: 
                    armor = row[6]
                    item_description = row[7]

                    craft_execution = row[8]
                    craft_city = row[9]

                    myItemFile = open("items/" + filename, 'w')

                    ### Writing each file ###

            		# Line 1: File and item name

                    myItemFile.write(itemname + '\r\n')

                    #Line 2: Image. "00" needs to be added before.

                    # Needs to check if the image has 2 or 3 digits to add trailing zeros

                    if len(image) == 2:
                        myItemFile.write("00" + image + '\r\n')
                    else: 
                    	myItemFile.write("0" + image + '\r\n')
                    # Line 3: Several attributes
                    #
                    # (1)`(2)`(3)`(4)`(5)`(6)`(7)`(8)`(9)`(10)`(11)`(12)`(13)`(14)`(15)`

                    # (1) Charges, weight, duration - total/bonus points`
                    # (2) `
                    # (3) `
                    # (4) soulbound (yes/no)`
                    # (5) fire bless (yes/no)`
                    # (6) ice bless (yes/no)`
                    # (7) earth bless (yes/no)`
                    # (8) storm bless (yes/no)`
                    # (9) night bless (yes/no)`
                    # (10) Slay (what race the weapon has a bonus on)`
                    # (11) Amount of Racial Bonus Damage`
                    # (12) Enchant levels (dull, soft, bright, brilliant): weapons - 1 2 3 4, helms/shields - 2 4 6 8, body armor - 4 8 12 16`
                    # (13) `
                    # (14) `
                    # (15) `

                    line3 = ""

                    # Check to see if its a weapon or body armor
                    # A = Weapon, C = Armor, J = Shield, K = Helmet

                    if decked == "Yes":
                        if item_type == "A":
                            line3 += "17```yes`yes`yes`yes`yes`yes`" + bane_type + "`" + bane_percentage + "`12```"
                        elif item_type == "C":
                            line3 += "17```yes`yes`yes`yes`yes`yes```12```"
                        elif item_type == "J" or item_type == "K":
                            line3 += "6```yes`yes`yes`yes`yes`yes```6```"
                        else: 
                            line3 += "``````````````"
                    else:
                        if item_type == "A":
                            line3 += "`````````" + bane_type + "`" + bane_percentage + "````"
                        else: 
                            line3 += "``````````````"                        

                    # (10) is the bane and (11) is the bane %

                    myItemFile.write(line3 + '\r\n')

                    # Line 4: Item type. (Will be the same for weapons)

                    myItemFile.write(item_type + '\r\n')

                    # Line 5: TODO Drop/Spawn

                    myItemFile.write('0\r\n')

                    # Lines 6 and 7: Min/Max Damage. Must verify its a weapon. 

                    if item_type == "A":
                        myItemFile.write(min_damage + '\r\n')
                        myItemFile.write(max_damage + '\r\n')
                    else: 
                        myItemFile.write("0" + '\r\n')                    
                        myItemFile.write("0" + '\r\n')


                    # Line 8: AC. Must verify its armor
                    if item_type == "C" or item_type == "J" or item_type == "K":
                        myItemFile.write(armor + "\r\n")
                    else: 
                        myItemFile.write("0\r\n")

                    # Line 9: Item Class

                    myItemFile.write(item_class + '\r\n')

                    # Line 10: Item Restriction

                    myItemFile.write(restrictions + '\r\n')

                    # Line 11: Description

                    #myItemFile.write(item_description.replace("'", "\\'"))
                    myItemFile.write(item_description)

                    myItemFile.write('\r\n')
                    myItemFile.write('\r\n')
                    myItemFile.write('\r\n')

                    myItemFile.close()

            line_num += 1

filename_csv = str(sys.argv[1])

file_csv_reader(filename_csv)


