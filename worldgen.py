# worldgen.py
# World generation for the Cepheus Engine and similar OGL 2d6 Sci-Fi games.
# v1.5, March 27, 2017.
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import os
import platform

#set functions

def dice(n,sides): #inputs number of dice, sides per die
	"""
	die-rolling function
	"""
	die=0
	roll=0
	while die<n:
		roll=roll+random.randint(1,sides)
		die+=1
	return roll #outputs die roll result

def yn():
	"""
	simple yes or no prompt filtering invalid results
	"""
	query = 1
	while query == 1:
		answer = str(input("Y/N: "))
		answer=answer.lower()
		if answer == "y":
			return "y"
			query = 0
		if answer == "n":
			return "n" #outputs "y" or "n"
			query = 0
		else:
			print ("Invalid Answer")

def current_dir():
	"""
	lists the current directory's contents on Windows or Linux
	"""
	if platform.system() == "Windows":
		directory=os.listdir(".\\")
	else:
		directory = os.getcwd()
	return directory
			
def check_file_exists(check_file):
	if check_file in os.listdir():
		file_exists = True
	else:
		file_exists = False
	return file_exists
 
def savefile():
	"""
	file-saving function
	"""
	filename=str(input("Please enter file name to generate: "))
	filecheck=filename+".sec"
	save = 1
	#directory=current_dir() #check if file already exists
	#filenumber=len(directory)
	#for i in range (0, filenumber):
	#  print(directory[i])
	#  #directory[i]=str(directory[i].lower())
	#  directory = "fred"
	#filecheck=filecheck.lower()
	if check_file_exists(filecheck):
		print(" ")
		print("File already exists. Overwrite?")
		overwrite=yn()
		if overwrite == "y":
			save=0
		if overwrite == "n":
			filename=input("Please enter new file name to generate: ")
	return filename #outpus File name

def clear_screen():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')

def random_choice(list): #input list
	"""
	randomly chooses an element from a list.
	"""
	element=list[random.randint(0,len(list)-1)]
	return element #output randomly-selected element
	
def pseudo_hex(num): #inputs number
	"""
	converts numbers to Cepheus Engine "Pseudo-Hex"
	now converted to a list.
	"""
	num=int(num)
	code=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "E", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	num=code[num]
	return num #outputs "pseudo-hex" number

def size_gen():
	"""
	generates the size number
	"""
	worldsize=0
	worldsize=dice(2,6) - 2
	return worldsize #outputs world size number

def atmo_gen(worldsize): #inputs world size number
	"""
	generates the atmosphere number
	"""
	worldatmo=0
	worldatmo=dice(2,6)-7 + worldsize
	if worldsize == 0:
		worldatmo = 0
	if worldatmo < 0:
		worldatmo = 0
	if worldatmo > 15:
		worldatmo = 15
	return worldatmo #outputs atmosphere number

def hyd_gen(worldsize): #inputs world size number
	"""
	generates the hydrographics number
	"""
	worldhyd=0
	worldhyd=dice(2,6) - 7 + worldsize
	if worldsize == 0:
		hyd=worldhyd - 4
	if worldsize == 1:
		hyd=worldhyd - 4
	if worldsize >= 10:
		hyd=worldhyd - 4
	if worldsize == 0:
		worldhyd = 0
	if worldhyd < 0:
		worldhyd = 0
	if worldhyd > 10:
		worldhyd = 10
	return worldhyd #outputs hydrographics number

def pop_gen (worldsize, worldatmo, worldhyd): #inputs world size, atmospehere, and hydrographics numbers
	"""
	generates the population number
	"""
	worldpop=0
	worldpop=dice(2,6)-2
	if worldsize<=2:
		worldpop-=1
	if worldatmo>=10:
		worldpop-=2
	if worldatmo==6:
		worldpop+=3
	if worldatmo in [5,8]:
		worldpop+=1
	if worldhyd==0 and worldatmo<3:
		worldpop-=2
	if worldpop<0:
		worldpop=0
	return worldpop #outputs population number
	
def starport_gen (worldpop): #inputs the world population number
	"""
	generate starport letter
	"""
	starport="X"
	starport_roll=dice(2,6) - 7 + worldpop
	if worldpop==0:
		starport="X"
	if starport_roll <= 2:
		starport="X"
	if starport_roll in [3,4]:
		starport="E"
	if starport_roll in [5, 6]:
		starport="D"
	if starport_roll in [7, 8]:
		starport="C"
	if starport_roll in [9,10]:
		starport="B"
	if starport_roll>=11:
		starport="A"
	return starport #outputs the starport letter

def gov_gen (worldpop): #inputs the world population number
	"""
	generate government number
	"""
	worldgov=0
	worldgov=dice(2,6) - 7 + worldpop
	if worldgov < 0:
		worldgov=0
	if worldgov>15:
		worldgov=15
	if worldpop==0:
		worldgov=0
	return worldgov #outputs the world government number

def law_gen (worldgov): #inputs the world government number
	"""
	generate law level number
	"""
	worldlaw=0
	worldlaw=dice(2,6) - 7 + worldgov
	if worldgov == 0:
		worldlaw=0
	if worldlaw<0:
		worldlaw=0
	return worldlaw #outputs the world law level number

def tech_gen (starport, worldsize, worldatmo, worldhyd, worldpop, worldgov): #input the world's starport, size, atmosphere, hydrographics, population, and government ratings - 6 parameters
		"""
		generate tech-level number
		"""
		worldtech=0
		worldtech=dice(1,6)
		if starport == "A":
			worldtech+=6
		if starport== "B":
			worldtech+=4
		if starport== "C":
			worldtech+=2
		if starport== "X":
			worldtech-=4
		if worldsize in [0, 1]:
			worldtech+=2
		if worldsize in [2, 3, 4]:
			worldtech+=1
		if worldatmo in [0, 1, 2, 3, 10, 11, 12, 13, 14, 15]:
			worldtech+=1
		if worldhyd in [0, 9]:
			worldtech+=1
		if worldhyd == 10:
			worldtech+=2
		if worldpop == 0:
			worldtech=0
		if worldpop in [1, 2, 3, 4, 5, 9]:
			worldtech+=1
		if worldpop==10:
			worldtech+=2
		if worldpop==11:
			worldtech+=3
		if worldpop==12:
			worldtech+=4
		if worldgov in [0, 5]:
			worldtech+=1
		if worldgov==7:
			worldtech+=2
		if worldgov in [13, 14]:
			worldtech-=2
		if worldhyd in [0, 10] and worldpop >= 6 and worldtech < 4:
			worldtech=4
		if worldatmo in [4, 7, 9] and worldtech <5:
			worldtech=5
		if worldatmo < 3 or worldatmo in [10, 11, 12]:
			if worldtech < 7:
				worldtech=7
		if worldatmo in [13, 14] and worldhyd==10 and worldtech<7:
			worldtech=7
		if worldtech<0:
			worldtech=0
		return worldtech #outputs the world tech level number

def uwp_list_gen(starport, worldsize, worldatmo, worldhyd, worldpop, worldgov, worldlaw, worldtech): #input the world's starport, size, atmosphere, hydrographics, population, government, law, and tech-level ratings - 8 parameters
	"""
	convert world variables into a UWP list
	"""
	uwp_list=[starport, worldsize, worldhyd, worldatmo, worldpop, worldgov, worldlaw, worldtech]
	return uwp_list #outputs the UWP list

def trade_gen (uwp_list): #input UWP list
	"""
	determine trade codes from a UWP list
	"""
	trade_list=[]
	if uwp_list[2] in [4, 5, 6, 7, 8, 9] and uwp_list[3] in [4, 5, 6, 7, 8] and uwp_list[4] in [5, 6, 7]:
		trade_list.append("Ag")
	if uwp_list[1] == 0 and uwp_list[2] == 0 and uwp_list[3] == 0:
		trade_list.append("As")
	if uwp_list[4] == 0 and uwp_list[5] == 0 and uwp_list[6] == 0:
		trade_list.append("Ba")
	if uwp_list[2] >= 2 and uwp_list[3] == 0:
		trade_list.append("De")
	if uwp_list[2] >= 10 and uwp_list[3] >= 1:
		trade_list.append ("Fl")
	if uwp_list[2] in [5, 6, 8] and uwp_list[3] in [4, 5, 6, 7, 8, 9] and uwp_list[4] in [4, 5, 6, 7, 8]:
		trade_list.append("Ga")
	if uwp_list[4] >= 9:
		trade_list.append("Hi")
	if uwp_list[7] >= 12:
		trade_list.append("Ht")
	if uwp_list[2] in [0, 1] and uwp_list[3] >= 1:
		trade_list.append("Ic")
	if uwp_list[2] in [0, 1, 2, 4, 7, 9] and uwp_list[4] >= 9:
		trade_list.append("In")
	if uwp_list[4] in [1, 2, 3]:
		trade_list.append("Lo")
	if uwp_list[7] <= 5:
		trade_list.append("Lt")
	if uwp_list[2] in [0, 1, 2, 3] and uwp_list[3] in [0, 1, 2, 3] and uwp_list[4] >= 6:
		trade_list.append("Na")
	if uwp_list[4] in [4, 5, 6]:
		trade_list.append("Ni")
	if uwp_list[2] in [2, 3, 4, 5] and uwp_list[3] in [0, 1, 2, 3]:
		trade_list.append("Po")
	if uwp_list[2] in [6, 8] and uwp_list[4] in [6, 7, 8]:
		trade_list.append("Ri")
	if uwp_list[3] == 10:
		trade_list.append("Wa")
	if uwp_list[2] == 0:
		trade_list.append("Va")
	return trade_list #output trade code list

def trade_stringer (trade_list): #input trade code list
	"""
	build a Trade Code string suitable for a SEC file
	Note that this is a plain text file formatted by spaces so the trade code string's length must be fixed.
	"""
	trade_string=""
	trade_count=6-len(trade_list)
	if trade_count<=0:
		trade_count=0
	for i in range (1, trade_count):
		trade_list.append("  ")
	trade_string= " ".join(trade_list)
	return trade_string #output trade code string	

def pop_mod (worldpop): #inputs the world population number
	"""
	generates the population multiplier
	"""
	popmod=0
	popmod=dice(2,6) - 2
	if worldpop==0:
		popmod=0
	if popmod>9:
		popmod=9
	return popmod #outputs the world population multiplier	

def planetoid_gen(worldsize): #input world size
	"""
	determine planetoid presence
	"""
	planetoid=0
	planetoid_presence=0
	planetoid_presence=dice(2,6)
	if planetoid_presence >= 4 or worldsize == 0:
		planetoid=dice(1, 6) - 3
		if planetoid < 1:
			planetoid = 1
	else:
		planetoid=0
	return planetoid #output planetoid belt number

def gas_gen():
	"""
	determine gas giant presence
	"""
	gas=0
	gas_presence=0
	gas_presence=dice(2,6)
	if gas_presence >= 5:
		gas=dice(1, 6) - 2
		if gas < 1:
			gas = 1
	else:
		gas=0
	return gas #output gas giant number

def pbg_gen(uwp_list): #inout world UWP list
	"""
	generates a three-digit code of the population multiplier, planetoid belt number, and gas giant number
	"""
	popmod=pop_mod(uwp_list[4])
	planetoid=planetoid_gen(uwp_list[1])
	gas=gas_gen()
	pbg = "%s%s%s" % (popmod, planetoid, gas)
	return pbg #output "PBG" three-digit code
	
def base_gen (starport): #input starship letter
	"""
	determine base presence
	"""
	base=" "
	naval=0
	naval_presence=0
	scout=0
	scout_presence=0
	pirate=0
	pirate_presence=0
	if starport in ["A", "B"]:
		naval_presence=dice(2, 6)
		if naval_presence >= 8:
			naval=1
		else:
			naval=0
	if starport in ["A", "B", "C", "D"]:
		scout_presence=dice(2, 6)
		if starport == "C":
			scout_presence -= 1
		if starport == "B":
			scout_presence -= 2
		if starport == "A":
			scout_presence -= 3
		if scout_presence >= 7:
			scout=1
	if starport != "A" and naval != 1:
		pirate_presence=dice(2, 6)
		if pirate_presence >= 12:
			pirate=1
		else:
			pirate=0
	if naval==1 and scout==1 and pirate!=1:
		base="A"
	if scout==1 and pirate==1 and naval!=1:
		base="G"
	if naval==1 and scout!=1 and pirate!=1:
		base="N"
	if naval!=1 and scout!=1 and pirate==1:
		base="P"
	if naval!=1 and scout==1 and pirate!=1:
		base="S"
	return base #output base letter

def zone_gen(uwp_list): #input UWP list
	"""
	determine Amber Zone presence
	"""
	zone=""
	if uwp_list[2] >= 10 or uwp_list[5] in [0, 7, 10] or uwp_list[6] == 0 or uwp_list[6] >= 9:
		zone=" A "
	else:
		zone="   "
	return zone #output Amber Zone

def uwp_gen():
		"""
		generate world UWP list
		List explanation:
		uwp_list[0] - starport
		uwp_list[1] - size
		uwp_list[2] - atmosphere
		uwp_list[3] - hydrographics
		uwp_list[4] - population
		uwp_list[5] - government
		uwp_list[6] - law level
		uwp_list[7] - tech-level
		"""
		worldsize=size_gen() #generate world size
		worldatmo=atmo_gen(worldsize) #generate world atmosphere
		worldhyd=hyd_gen(worldsize) #generate world hydrographics
		worldpop=pop_gen(worldsize, worldatmo, worldhyd) #generate world population
		starport=starport_gen(worldpop) #generate world starport
		worldgov=gov_gen(worldpop) #generate world government
		worldlaw=law_gen(worldgov) #generate world law level
		worldtech=tech_gen(starport, worldsize, worldatmo, worldhyd, worldpop, worldgov) #generate world tech-level
		uwp_list=uwp_list_gen(starport, worldsize, worldatmo, worldhyd, worldpop, worldgov, worldlaw, worldtech) #convert everything to a list
		return uwp_list #output UWP list

def uwp_hex (uwp_list): #input UWP list
	"""
	convert the UWP list to a pseudo-hex UWP string
	"""
	uwp=[]
	uwp.append(uwp_list[0])
	uwp.append(pseudo_hex(uwp_list[1]))
	uwp.append(pseudo_hex(uwp_list[2]))
	uwp.append(pseudo_hex(uwp_list[3]))
	uwp.append(pseudo_hex(uwp_list[4]))
	uwp.append(pseudo_hex(uwp_list[5]))
	uwp.append(pseudo_hex(uwp_list[6]))
	uwp.append(pseudo_hex(uwp_list[7]))
	uwp_string ="%s%s%s%s%s%s%s-%s " % (uwp[0],uwp[1],uwp[2],uwp[3],uwp[4],uwp[5],uwp[6],uwp[7])
	return uwp_string #output Cepheus-style UWP string

def star_gen(uwp_list): #generates realistic stellar data using Constantine Thomas' rules (version 3.0).
    n_stars=0
    size=""
    star_type=""
    startext1=""
    startext2=""
    startext3=""
    startext4=""
    startext=""
    throw=0
    throw1=0
    x=0
    tag=0
    decimal1=0
    decimal2=0
    decimal3=0
    primary=[]
    secondary=[]
    tretiary=[]
    throw=dice(2,6)
    if throw<=7:
        n_stars=1
    if throw>=8 and throw<=11:
        n_stars=2
    if throw==12:
        n_stars=3
    throw=dice(2,6) #generate primary star
    if uwp_list[2]>=4 and uwp_list[2]<=9:
        throw=throw+4
        tag=1
    if uwp_list[4]>=8 and tag==0:
        throw=throw+4
    if throw<=1:
        star_type="B"
    if throw==2:
        star_type="A"
    if throw>=3 and throw<=8:
        star_type="M"
    if throw==9:
        star_type="K"
    if throw==10:
        star_type="G"
    if throw>=11:
        star_type="F"
    if throw==12:
        star_type="K"
    if throw>=13:
        star_type="G"
    decimal1=dice(1,10)-1
    throw1=dice(2,6)
    if uwp_list[2]>=4 and uwp_list[2]<=9:
        throw1=throw1+4
        tag=1
    if uwp_list[4]>=8 and tag==0:
        throw1=throw1+4
    if throw1<=2:
        throw=dice(1,6)
        if throw>=1 and throw<=3:
            size="D"
        if throw>=4 and throw<=5:
            size="III"
        if throw==6:
            size="II"
    if throw1==3:
        size="IV"
    if throw1>=4:
        size="V"
    if star_type=="A" or star_type=="F" or star_type=="G":
        if size=="D" or size=="II" or size=="III":
            size="V"
    if star_type=="M" and size=="IV":
        size="V"
    if star_type=="K" and size=="IV" and decimal1>=2:
        size="V"
    if size=="D" and uwp_list[2]>=1:
        size="V"
    if size=="D":
        star_type=""
        decimal1=""
    primary.append(star_type)
    primary.append(decimal1)
    primary.append(size)
    startext1="%s%s%s " % (primary[0], primary[1], primary[2])
    if n_stars==2 or n_stars==3: #generate secondary star
        decimal2=0
        secondary=[]
        size=""
        star_type=""
        throw=dice(2,6)
        if throw<=1:
            star_type="B"
        if throw<=2:
            star_type="A"
        if throw>=3 and throw<=8:
            star_type="M"
        if throw==9:
            star_type="K"
        if throw==10:
            star_type="G"
        if throw>=11:
            star_type="F"
        if throw==12:
            star_type="K"
        if throw>=13:
            star_type="G"
        decimal2=dice(1,10)-1
        throw1=dice(2,6)
        if throw1==2:
            throw=dice(1,6)
        if throw>=1 and throw<=3:
            size="D"
        if throw>=4 and throw<=5:
            size="III"
        if throw==6:
            size="II"
        if throw1==3:
            size="IV"
        if throw1>=4:
            size="V"
        if star_type=="A" or star_type=="F" or star_type=="G":
            if size=="D" or size=="II" or size=="III":
                size="V"
        if star_type=="M" and size=="IV":
            size="V"
        if star_type=="K" and size=="IV" and decimal1>=2:
            size="V"
        if size=="D":
            star_type=""
            decimal2=""
        secondary.append(star_type)
        secondary.append(decimal2)
        secondary.append(size)
        startext2="%s%s%s " % (secondary[0], secondary[1], secondary[2])
    if n_stars==3: #generate tretiary star
        decimal3=0
        secondary=[]
        size=""
        star_type=""
        throw=dice(2,6)
        if throw<=1:
            star_type="B"
        if throw==2:
            star_type="A"
        if throw>=3 and throw<=8:
            star_type="M"
        if throw==9:
            star_type="K"
        if throw==10:
            star_type="G"
        if throw>=11:
            star_type="F"
        if throw==12:
            star_type="K"
        if throw>=13:
            star_type="G"
        decimal3=dice(1,10)-1
        throw1=dice(2,6)
        if throw1==2:
            throw=dice(1,6)
            if throw>=1 and throw<=3:
                size="D"
            if throw>=4 and throw<=5:
                size="III"
            if throw==6:
                size="II"
        if throw1==3:
            size="IV"
        if throw1>=4:
            size="V"
        if star_type=="A" or star_type=="F" or star_type=="G":
            if size=="D" or size=="II" or size=="III":
                size="V"
        if star_type=="M" and size=="IV":
            size="V"
        if star_type=="K" and size=="IV" and decimal1>=2:
            size="V"
        if size=="D":
            star_type=""
            decimal3=""
        tretiary.append(star_type)
        tretiary.append(decimal3)
        tretiary.append(size)
        startext3="%s%s%s " % (tretiary[0], tretiary[1], tretiary[2])

    startext4=startext1+startext2+startext3
    startext=str.join('', startext4)
    return startext	

def name_gen():
	"""
	randomly chooses a name from a list
	"""
	name=""
	file_check=check_file_exists("names.txt")
	if file_check==False:
		base_name=""
	if file_check==True:
		try:
			name_file=open("names.txt", "r")
			name_list=name_file.readlines()
			base_name=random_choice(name_list)
			base_name=base_name.strip()
		finally:
			name_file.close()
	char_list=[base_name]
	length_count=int(7-len(base_name)//2)
	if int(len(base_name)%2)==0:
		length_count+=1
	if length_count<=0:
		length_count=0
	for i in range (1, length_count):
		char_list.append(" ")
	name= " ".join(char_list)
	return name #output random name
	
def world_gen (worldhex): #input hex number
	"""
	primary world-generating function
	"""
	worldname=name_gen() #generates world name from list
	allegiance="Na" #currently a placeholder
	stellar=" "
	uwp_list=uwp_gen() #generate UWP list
	uwp_string=uwp_hex(uwp_list) #convert UWP list to string
	base=base_gen(uwp_list[0]) #generate base code
	trade_list=trade_gen(uwp_list) #generate trade codes
	trade_string=trade_stringer(trade_list) #convert trade codes to string
	pbg=pbg_gen(uwp_list) #generate PBG code
	zone=zone_gen(uwp_list) #check for Amber Zone
	stellar=star_gen(uwp_list)
	preliminary_world_string=worldname, str(worldhex), uwp_string, base, trade_string, zone, pbg, allegiance, stellar
	world_string=str.join(' ', preliminary_world_string)
	return world_string #output world row string compatible with a SEC file

def sec_gen (maxcolumn, maxrow): #input maximum generated space row and column. as well as the file name for generation
	"""
	SEC file generating function
	"""
	sector_name=savefile()
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
				throw=dice(1,6)
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
		clear_screen() #clears screen before any new appearance of the menu
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