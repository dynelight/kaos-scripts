# Weapon file generator

import csv



with open('weapons.csv', 'r') as f:
    reader = csv.reader(f)

    # Line number counter
    line_num = 0

    directory = "items"

    if not os.path.exists(directory):
        os.makedirs(directory)

    # Crafts.dat file
    myCraftsDatFile = open(directory + "/crafts.dat", 'w')

    # Iteration of each row in csv
    for row in reader:

    	# Ignores header
    	if line_num != 0:

            # Cleans initial and ending spaces
            for i in range(0, len(row)):
                row[0] = row[0].strip()

            # Atributes
            filename = row[0] + ".dat"
            itemname = row[0]            
            image = row[1]            
            decked = row[5]
            bane_type = row[8]
            bane_percentage = row[9]
            restrictions = row[4]
            min_damage = row[6]
            max_damage = row[7]
            item_description = "\"" + row[10] + "\""
            item_class = row[3]
            item_type = row[2]

            # Craft Requirements

            craft_execution = row[11]

            craft_requirements = []
            for i in range(13, 24 + 1):
                craft_requirements.append(row[i])



            myFile = open(filename, 'w')
            myCraftsFile = open(directory + "/" + row[0], 'w')            

            ### Writing each file ###

    		# Line 1: File and item name

            myFile.write(itemname + '\r\n')

            #Line 2: Image. "00" needs to be added before.

            # Needs to check if the image has 2 or 3 digits to add trailing zeros

            if len(image) == 2:
                myFile.write("00" + image + '\r\n')
            else: 
            	myFile.write("0" + image + '\r\n')
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

            # (1) Weight is 0 on weapons

            line3 += "`"

            # (2) and (3) are empty

            line3 += "`"
            line3 += "`"

            # (4) (5) (6) (7) (8) and (9) are related to values being decked or not

            if decked == "yes":
            	line3 += "yes`yes`yes`yes`yes`yes`"
            else: 
            	#line3 += "no`no`no`no`no`no`"
            	line3 += "``````"
            # (10) is the bane and (11) is the bane %

            line3 += bane_type
            line3 += "`"
            line3 += bane_percentage
            line3 += "`"

            # TODO: (12) Enchant levels, can be empty for now
            line3 += "`"
            # (13), (14) and (15) are empty

            line3 += "```"

            myFile.write(line3 + '\r\n')

            # Line 4: Item type. (Will be the same for weapons)

            myFile.write(item_type + '\r\n')

            # Line 5: TODO Drop/Spawn

            myFile.write('0\r\n')

            # Line 6: Min damage

            myFile.write(min_damage + '\r\n')

            # Line 7: Max damage

            myFile.write(max_damage + '\r\n')

            # Line 8: AC (Ignored on weapons)

            myFile.write("0\r\n")

            # Line 9: Item Class

            myFile.write(item_class + '\r\n')

            # Line 10: Item Restriction

            myFile.write(restrictions + '\r\n')

            # Line 11: Description

            myFile.write(item_description)

            myFile.write('\r\n')
            myFile.write('\r\n')
            myFile.write('\r\n')

            myFile.close()

            ### Writing each crafts file ###

            # Line 1: The itemname

            myCraftsFile.write('"' + itemname + '"\r\n')

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

            # Crafts.dat file

            # Item
            myCraftsDatFile.write('"' + itemname + '"\r\n')

            # Price
            myCraftsDatFile.write('"10000"\r\n')

            # Level
            myCraftsDatFile.write('"1"\r\n')

        line_num += 1
    myCraftsDatFile.close()