# Weapon file generator

import csv
import os
import shutil
import sys

# Deletes old files
#if os.path.exists("items"):
#    shutil.rmtree('items')
#if os.path.exists("cities"):
#    shutil.rmtree('cities')
#if os.path.exists("crafts"):
#    shutil.rmtree('crafts')

#Verifying exitance of folders
if not os.path.exists("items"):
    os.makedirs("items")

if not os.path.exists("cities"):
    os.makedirs("cities")

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
                filename = "Item " + row[0] + ".dat"

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
              
                    # Craft Requirements
                    craft_execution = row[11]
                    craft_city = row[12]

                    if craft_city != "":
                        for i in range(13, 23 + 1):
                            craft_requirements.append(row[i])

                    craft_price = row[25]

                else: 
                    armor = row[6]
                    item_description = row[7]

                    craft_execution = row[8]
                    craft_city = row[9]
                    if craft_city != "":
                        for i in range(10, 20 + 1):
                            craft_requirements.append(row[i])

                    craft_price = row[22]


                if not os.path.exists("cities/" + craft_city):
                    os.makedirs("cities/" + craft_city)

                if not os.path.exists("crafts/"):
                    os.makedirs("crafts/")

                if craft_execution != "":         

                    # Crafts.dat file
                    myCraftsDatFile = open("cities/" + craft_city + "/crafts.dat", 'a')

                    myItemFile = open("items/" + filename, 'w')

                    myCraftsFile = open("crafts/" + filename, 'w')            

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

                    ### Writing each crafts file ###

                    # Line 1: The itemname

                    myCraftsFile.write('"' + itemname + '"\r\n')

                    # Line 2: Class restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 3: Race restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 4: Divinity restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 5: Level restriction

                    myCraftsFile.write('"' + '"\r\n')                    

                    # Line 6: STR restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 7: INT restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 8: AGI restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 9: END restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 10: WIS restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 11: CHR restriction to craft. Ignored for now

                    myCraftsFile.write('"' + '"\r\n')

                    # Line 12: Craft Location. Empty for now.

                    myCraftsFile.write('"' + '"\r\n')                    

                    # Line 13: Execution text

                    myCraftsFile.write('"' + craft_execution + '"\r\n')

                    # Line 14: One time use

                    myCraftsFile.write('"' + 'no"\r\n')

                    # Line 15-19: Reserved

                    for i in range(15, 19 + 1):
                        myCraftsFile.write('"' + '"\r\n')

                    # Rest of the lines are the craft ingredients

                    for item in craft_requirements:
                        if item != "":

                            myCraftsFile.write('"' + item + '"\r\n')

                    myCraftsFile.close()

                    # Crafts.dat file

                    # Item
                    myCraftsDatFile.write('"Item ' + itemname + '"\r\n')

                    # Price
                    myCraftsDatFile.write('"' + craft_price + '"\r\n')

                    # Level
                    myCraftsDatFile.write('"1"\r\n')


                    myCraftsDatFile.close()
            line_num += 1

filename_csv = str(sys.argv[1])

file_csv_reader(filename_csv)


