# worldgen.py
# World generation for the Cepheus Engine and similar OGL 2d6 Sci-Fi games.
# v1.6, May 29, 2017.
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import os
import platform
import worldgenlib
import stellagama

#set functions

def world_gen (worldhex): #input hex number
	"""
	primary world-generating function
	"""
	worldname=worldgenlib.name_gen() #generates world name from list
	allegiance="Na" #currently a placeholder
	stellar=" "
	uwp_list=worldgenlib.uwp_gen() #generate UWP list
	uwp_string=worldgenlib.uwp_hex(uwp_list) #convert UWP list to string
	base=worldgenlib.base_gen(uwp_list[0]) #generate base code
	trade_list=worldgenlib.trade_gen(uwp_list) #generate trade codes
	trade_string=worldgenlib.trade_stringer(trade_list) #convert trade codes to string
	pbg=worldgenlib.pbg_gen(uwp_list) #generate PBG code
	zone=worldgenlib.zone_gen(uwp_list) #check for Amber Zone
	stellar=worldgenlib.star_gen(uwp_list)
	preliminary_world_string=worldname, str(worldhex), uwp_string, base, trade_string, zone, pbg, allegiance, stellar
	world_string=str.join(' ', preliminary_world_string)
	return world_string #output world row string compatible with a SEC file	
	
def sec_gen (maxcolumn, maxrow): #input maximum generated space row and column. as well as the file name for generation
	"""
	SEC file generating function
	"""
	sector_name=stellagama.savefile("txt")
	file_name=sector_name+".sec"
	outp = open(file_name,"w")
	outp.write(sector_name+'\r\n') #start of SEC file header output
	outp.write(""+'\r\n')
	outp.write("The data in the sector text files is laid out in column format:"+'\r\n')
	outp.write(""+'\r\n')
	outp.write(" 1-14: Name"+'\r\n')
	outp.write("15-18: HexNbr"+'\r\n')
	outp.write("20-28: UWP"+'\r\n')
	outp.write("   31: Bases"+'\r\n')
	outp.write("33-47: Codes & Comments"+'\r\n')
	outp.write("   49: Zone"+'\r\n')
	outp.write("52-54: PBG"+'\r\n')
	outp.write("56-57: Allegiance"+'\r\n')
	outp.write("59-74: Stellar Data"+'\r\n')
	outp.write(""+'\r\n')
	outp.write("....+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....8"+'\r\n')
	outp.write(""+'\r\n') #end of SEC file header output
	try: #added to make sure the file is always closed no matter what
		for column in range (1, maxcolumn+1): #generate subsector, quadrant, or sector
			for row in range (1, maxrow+1):
				throw=stellagama.dice(1,6)
				if throw>=4:
					if row<=9:
						row_loc="0%i" % (row)
					if row>=10:
						row_loc="%i" % (row)
					if column<=9:
						column_loc="0%i" % (column)
					if column>=10:
						column_loc="%i" % (column)
					worldhex=column_loc+row_loc
					world_line=world_gen(worldhex)
					outp.write(world_line+'\r\n')
	finally: #added to make sure the file is always closed no matter what
		outp.close() #close file	
				
def	main():
	"""
	Main program body
	"""
	menu=1
	while menu == 1: #Program will always return to the menu unless exited
		stellagama.clear_screen() #clears screen before any new appearance of the menu
		print ("")
		print ("Welcome to the Cepheus Engine World Generator v1.5")
		print ("========================================")
		print ("Please choose an option:")
		print ("1 - Generate a single world to screen")
		print ("2 - Generate a subsector to file")
		print ("3 - Generate a quadrant to file")
		print ("4 - Generate a sector to file")
		print ("5 - About")
		print ("6 - Exit Program")
		print ("========================================")
		choice=input("Please enter your choice: ")
		if choice in [1, "1"]:
			print("")
			print (world_gen("0101"))
			print("")
			print("Press any key to continue")
			input()
		elif choice in  [2, "2"]:
			print("")
			print ("Generating subsector to file")
			print ("")
			sec_gen(8, 10)
			print ("Subsector generated, press any key to continue")
			input()
		elif choice in [3, "3"]:
			print("")
			print ("Generating quadrant to file")
			print ("")
			sec_gen(16, 20)
			print ("Quadrant generated, press any key to continue")
			input()
		elif choice in [4, "4"]:
			print("")
			print ("Generating sector to file")
			print ("")
			sec_gen(32, 40)
			print ("Sector generated, press any key to continue")
			input()
		elif choice in [5, "5"]: #displays program information
			print ("")
			print("World generation for the Cepheus Engine and similar OGL 2d6 Sci-Fi games")
			print("v1.5, March 27, 2017")
			print("This is open source code, feel free to use it for any purpose")
			print("contact the author at golan2072@gmail.com")
			print("Press any key to continue")
			input()
		elif choice in [6, "6"]:
			print("Exiting program")
			menu=0
			break
		else:
			print ("Invalid Input, press any key to return to menu")
			input()

#Program execution starts here
main()