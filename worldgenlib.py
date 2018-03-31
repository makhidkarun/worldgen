# worldgenlib.py
# Cepheus Engine world generation data and rules library
# v1.1, March 31st, 2018
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

# import modules
import random
import string
import stellagama


def size_gen():
    """
	generates the size number
	"""
    worldsize = 0
    worldsize = stellagama.dice(2, 6) - 2
    return worldsize  # outputs world size number


def atmo_gen(worldsize):  # inputs world size number
    """
	generates the atmosphere number
	"""
    worldatmo = 0
    worldatmo = stellagama.dice(2, 6) - 7 + worldsize
    if worldsize == 0:
        worldatmo = 0
    if worldatmo < 0:
        worldatmo = 0
    if worldatmo > 15:
        worldatmo = 15
    return worldatmo  # outputs atmosphere number


def hyd_gen(worldsize):  # inputs world size number
    """
	generates the hydrographics number
	"""
    worldhyd = 0
    worldhyd = stellagama.dice(2, 6) - 7 + worldsize
    if worldsize == 0:
        hyd = worldhyd - 4
    if worldsize == 1:
        hyd = worldhyd - 4
    if worldsize >= 10:
        hyd = worldhyd - 4
    if worldsize == 0:
        worldhyd = 0
    if worldhyd < 0:
        worldhyd = 0
    if worldhyd > 10:
        worldhyd = 10
    return worldhyd  # outputs hydrographics number


def pop_gen(
    worldsize, worldatmo, worldhyd
):  # inputs world size, atmospehere, and hydrographics numbers
    """
	generates the population number
	"""
    worldpop = 0
    worldpop = stellagama.dice(2, 6) - 2
    if worldsize <= 2:
        worldpop -= 1
    if worldatmo >= 10:
        worldpop -= 2
    if worldatmo == 6:
        worldpop += 3
    if worldatmo in [5, 8]:
        worldpop += 1
    if worldhyd == 0 and worldatmo < 3:
        worldpop -= 2
    if worldpop < 0:
        worldpop = 0
    return worldpop  # outputs population number


def starport_gen(worldpop):  # inputs the world population number
    """
	generate starport letter
	"""
    starport = "X"
    starport_roll = stellagama.dice(2, 6) - 7 + worldpop
    if worldpop == 0:
        starport = "X"
    if starport_roll <= 2:
        starport = "X"
    if starport_roll in [3, 4]:
        starport = "E"
    if starport_roll in [5, 6]:
        starport = "D"
    if starport_roll in [7, 8]:
        starport = "C"
    if starport_roll in [9, 10]:
        starport = "B"
    if starport_roll >= 11:
        starport = "A"
    return starport  # outputs the starport letter


def gov_gen(worldpop):  # inputs the world population number
    """
	generate government number
	"""
    worldgov = 0
    worldgov = stellagama.dice(2, 6) - 7 + worldpop
    if worldgov < 0:
        worldgov = 0
    if worldgov > 15:
        worldgov = 15
    if worldpop == 0:
        worldgov = 0
    return worldgov  # outputs the world government number


def law_gen(worldgov):  # inputs the world government number
    """
	generate law level number
	"""
    worldlaw = 0
    worldlaw = stellagama.dice(2, 6) - 7 + worldgov
    if worldgov == 0:
        worldlaw = 0
    if worldlaw < 0:
        worldlaw = 0
    return worldlaw  # outputs the world law level number


def tech_gen(
    starport, worldsize, worldatmo, worldhyd, worldpop, worldgov
):  # input the world's starport, size, atmosphere, hydrographics, population, and government ratings - 6 parameters
    """
		generate tech-level number
		"""
    worldtech = 0
    worldtech = stellagama.dice(1, 6)
    if starport == "A":
        worldtech += 6
    if starport == "B":
        worldtech += 4
    if starport == "C":
        worldtech += 2
    if starport == "X":
        worldtech -= 4
    if worldsize in [0, 1]:
        worldtech += 2
    if worldsize in [2, 3, 4]:
        worldtech += 1
    if worldatmo in [0, 1, 2, 3, 10, 11, 12, 13, 14, 15]:
        worldtech += 1
    if worldhyd in [0, 9]:
        worldtech += 1
    if worldhyd == 10:
        worldtech += 2
    if worldpop == 0:
        worldtech = 0
    if worldpop in [1, 2, 3, 4, 5, 9]:
        worldtech += 1
    if worldpop == 10:
        worldtech += 2
    if worldpop == 11:
        worldtech += 3
    if worldpop == 12:
        worldtech += 4
    if worldgov in [0, 5]:
        worldtech += 1
    if worldgov == 7:
        worldtech += 2
    if worldgov in [13, 14]:
        worldtech -= 2
    if worldhyd in [0, 10] and worldpop >= 6 and worldtech < 4:
        worldtech = 4
    if worldatmo in [4, 7, 9] and worldtech < 5:
        worldtech = 5
    if worldatmo < 3 or worldatmo in [10, 11, 12]:
        if worldtech < 7:
            worldtech = 7
    if worldatmo in [13, 14] and worldhyd == 10 and worldtech < 7:
        worldtech = 7
    if worldtech < 0:
        worldtech = 0
    return worldtech  # outputs the world tech level number


def uwp_list_gen(
    starport, worldsize, worldatmo, worldhyd, worldpop, worldgov, worldlaw, worldtech
):  # input the world's starport, size, atmosphere, hydrographics, population, government, law, and tech-level ratings - 8 parameters
    """
	convert world variables into a UWP list
	"""
    uwp_list = [
        starport,
        worldsize,
        worldhyd,
        worldatmo,
        worldpop,
        worldgov,
        worldlaw,
        worldtech,
    ]
    return uwp_list  # outputs the UWP list


def trade_gen(uwp_list):  # input UWP list
    """
	determine trade codes from a UWP list
	"""
    trade_list = []
    if uwp_list[2] in [4, 5, 6, 7, 8, 9] and uwp_list[3] in [
        4, 5, 6, 7, 8
    ] and uwp_list[
        4
    ] in [
        5, 6, 7
    ]:
        trade_list.append("Ag")
    if uwp_list[1] == 0 and uwp_list[2] == 0 and uwp_list[3] == 0:
        trade_list.append("As")
    if uwp_list[4] == 0 and uwp_list[5] == 0 and uwp_list[6] == 0:
        trade_list.append("Ba")
    if uwp_list[2] >= 2 and uwp_list[3] == 0:
        trade_list.append("De")
    if uwp_list[2] >= 10 and uwp_list[3] >= 1:
        trade_list.append("Fl")
    if uwp_list[2] in [5, 6, 8] and uwp_list[3] in [4, 5, 6, 7, 8, 9] and uwp_list[
        4
    ] in [
        4, 5, 6, 7, 8
    ]:
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
    return trade_list  # output trade code list


def trade_stringer(trade_list):  # input trade code list
    """
	build a Trade Code string suitable for a SEC file
	Note that this is a plain text file formatted by spaces so the trade code string's length must be fixed.
	"""
    trade_string = ""
    trade_count = 6 - len(trade_list)
    if trade_count <= 0:
        trade_count = 0
    for i in range(1, trade_count):
        trade_list.append("  ")
    trade_string = " ".join(trade_list)
    return trade_string  # output trade code string


def pop_mod(worldpop):  # inputs the world population number
    """
	generates the population multiplier
	"""
    popmod = 0
    popmod = stellagama.dice(2, 6) - 2
    if worldpop == 0:
        popmod = 0
    if popmod > 9:
        popmod = 9
    return popmod  # outputs the world population multiplier


def planetoid_gen(worldsize):  # input world size
    """
	determine planetoid presence
	"""
    planetoid = 0
    planetoid_presence = 0
    planetoid_presence = stellagama.dice(2, 6)
    if planetoid_presence >= 4 or worldsize == 0:
        planetoid = stellagama.dice(1, 6) - 3
        if planetoid < 1:
            planetoid = 1
    else:
        planetoid = 0
    return planetoid  # output planetoid belt number


def gas_gen():
    """
	determine gas giant presence
	"""
    gas = 0
    gas_presence = 0
    gas_presence = stellagama.dice(2, 6)
    if gas_presence >= 5:
        gas = stellagama.dice(1, 6) - 2
        if gas < 1:
            gas = 1
    else:
        gas = 0
    return gas  # output gas giant number


def pbg_gen(uwp_list):  # inout world UWP list
    """
	generates a three-digit code of the population multiplier, planetoid belt number, and gas giant number
	"""
    popmod = pop_mod(uwp_list[4])
    planetoid = planetoid_gen(uwp_list[1])
    gas = gas_gen()
    pbg = "%s%s%s" % (popmod, planetoid, gas)
    return pbg  # output "PBG" three-digit code


def base_gen(starport):  # input starship letter
    """
	determine base presence
	"""
    base = " "
    naval = 0
    naval_presence = 0
    scout = 0
    scout_presence = 0
    pirate = 0
    pirate_presence = 0
    if starport in ["A", "B"]:
        naval_presence = stellagama.dice(2, 6)
        if naval_presence >= 8:
            naval = 1
        else:
            naval = 0
    if starport in ["A", "B", "C", "D"]:
        scout_presence = stellagama.dice(2, 6)
        if starport == "C":
            scout_presence -= 1
        if starport == "B":
            scout_presence -= 2
        if starport == "A":
            scout_presence -= 3
        if scout_presence >= 7:
            scout = 1
    if starport != "A" and naval != 1:
        pirate_presence = stellagama.dice(2, 6)
        if pirate_presence >= 12:
            pirate = 1
        else:
            pirate = 0
    if naval == 1 and scout == 1 and pirate != 1:
        base = "A"
    if scout == 1 and pirate == 1 and naval != 1:
        base = "G"
    if naval == 1 and scout != 1 and pirate != 1:
        base = "N"
    if naval != 1 and scout != 1 and pirate == 1:
        base = "P"
    if naval != 1 and scout == 1 and pirate != 1:
        base = "S"
    return base  # output base letter


def zone_gen(uwp_list):  # input UWP list
    """
	determine Amber Zone presence
	"""
    zone = ""
    if uwp_list[2] >= 10 or uwp_list[5] in [0, 7, 10] or uwp_list[6] == 0 or uwp_list[
        6
    ] >= 9:
        zone = " A "
    else:
        zone = "   "
    return zone  # output Amber Zone


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
    worldsize = size_gen()  # generate world size
    worldatmo = atmo_gen(worldsize)  # generate world atmosphere
    worldhyd = hyd_gen(worldsize)  # generate world hydrographics
    worldpop = pop_gen(worldsize, worldatmo, worldhyd)  # generate world population
    starport = starport_gen(worldpop)  # generate world starport
    worldgov = gov_gen(worldpop)  # generate world government
    worldlaw = law_gen(worldgov)  # generate world law level
    worldtech = tech_gen(
        starport, worldsize, worldatmo, worldhyd, worldpop, worldgov
    )  # generate world tech-level
    uwp_list = uwp_list_gen(
        starport,
        worldsize,
        worldatmo,
        worldhyd,
        worldpop,
        worldgov,
        worldlaw,
        worldtech,
    )  # convert everything to a list
    return uwp_list  # output UWP list


def uwp_hex(uwp_list):  # input UWP list
    """
	convert the UWP list to a pseudo-hex UWP string
	"""
    uwp = []
    uwp.append(uwp_list[0])
    uwp.append(stellagama.pseudo_hex(uwp_list[1]))
    uwp.append(stellagama.pseudo_hex(uwp_list[2]))
    uwp.append(stellagama.pseudo_hex(uwp_list[3]))
    uwp.append(stellagama.pseudo_hex(uwp_list[4]))
    uwp.append(stellagama.pseudo_hex(uwp_list[5]))
    uwp.append(stellagama.pseudo_hex(uwp_list[6]))
    uwp.append(stellagama.pseudo_hex(uwp_list[7]))
    uwp_string = "%s%s%s%s%s%s%s-%s " % (
        uwp[0], uwp[1], uwp[2], uwp[3], uwp[4], uwp[5], uwp[6], uwp[7]
    )
    return uwp_string  # output Cepheus-style UWP string


def star_gen(
    uwp_list
):  # generates realistic stellar data using Constantine Thomas' rules (version 3.0).
    n_stars = 0
    size = ""
    star_type = ""
    startext1 = ""
    startext2 = ""
    startext3 = ""
    startext4 = ""
    startext = ""
    throw = 0
    throw1 = 0
    x = 0
    tag = 0
    decimal1 = 0
    decimal2 = 0
    decimal3 = 0
    primary = []
    secondary = []
    tretiary = []
    throw = stellagama.dice(2, 6)
    if throw <= 7:
        n_stars = 1
    if throw >= 8 and throw <= 11:
        n_stars = 2
    if throw == 12:
        n_stars = 3
    throw = stellagama.dice(2, 6)  # generate primary star
    if uwp_list[2] >= 4 and uwp_list[2] <= 9:
        throw = throw + 4
        tag = 1
    if uwp_list[4] >= 8 and tag == 0:
        throw = throw + 4
    if throw <= 1:
        star_type = "B"
    if throw == 2:
        star_type = "A"
    if throw >= 3 and throw <= 8:
        star_type = "M"
    if throw == 9:
        star_type = "K"
    if throw == 10:
        star_type = "G"
    if throw >= 11:
        star_type = "F"
    if throw == 12:
        star_type = "K"
    if throw >= 13:
        star_type = "G"
    decimal1 = stellagama.dice(1, 10) - 1
    throw1 = stellagama.dice(2, 6)
    if uwp_list[2] >= 4 and uwp_list[2] <= 9:
        throw1 = throw1 + 4
        tag = 1
    if uwp_list[4] >= 8 and tag == 0:
        throw1 = throw1 + 4
    if throw1 <= 2:
        throw = stellagama.dice(1, 6)
        if throw >= 1 and throw <= 3:
            size = "D"
        if throw >= 4 and throw <= 5:
            size = "III"
        if throw == 6:
            size = "II"
    if throw1 == 3:
        size = "IV"
    if throw1 >= 4:
        size = "V"
    if star_type == "A" or star_type == "F" or star_type == "G":
        if size == "D" or size == "II" or size == "III":
            size = "V"
    if star_type == "M" and size == "IV":
        size = "V"
    if star_type == "K" and size == "IV" and decimal1 >= 2:
        size = "V"
    if size == "D" and uwp_list[2] >= 1:
        size = "V"
    if size == "D":
        star_type = ""
        decimal1 = ""
    primary.append(star_type)
    primary.append(decimal1)
    primary.append(size)
    startext1 = "%s%s%s " % (primary[0], primary[1], primary[2])
    if n_stars == 2 or n_stars == 3:  # generate secondary star
        decimal2 = 0
        secondary = []
        size = ""
        star_type = ""
        throw = stellagama.dice(2, 6)
        if throw <= 1:
            star_type = "B"
        if throw <= 2:
            star_type = "A"
        if throw >= 3 and throw <= 8:
            star_type = "M"
        if throw == 9:
            star_type = "K"
        if throw == 10:
            star_type = "G"
        if throw >= 11:
            star_type = "F"
        if throw == 12:
            star_type = "K"
        if throw >= 13:
            star_type = "G"
        decimal2 = stellagama.dice(1, 10) - 1
        throw1 = stellagama.dice(2, 6)
        if throw1 == 2:
            throw = stellagama.dice(1, 6)
        if throw >= 1 and throw <= 3:
            size = "D"
        if throw >= 4 and throw <= 5:
            size = "III"
        if throw == 6:
            size = "II"
        if throw1 == 3:
            size = "IV"
        if throw1 >= 4:
            size = "V"
        if star_type == "A" or star_type == "F" or star_type == "G":
            if size == "D" or size == "II" or size == "III":
                size = "V"
        if star_type == "M" and size == "IV":
            size = "V"
        if star_type == "K" and size == "IV" and decimal1 >= 2:
            size = "V"
        if size == "D":
            star_type = ""
            decimal2 = ""
        secondary.append(star_type)
        secondary.append(decimal2)
        secondary.append(size)
        startext2 = "%s%s%s " % (secondary[0], secondary[1], secondary[2])
    if n_stars == 3:  # generate tretiary star
        decimal3 = 0
        secondary = []
        size = ""
        star_type = ""
        throw = stellagama.dice(2, 6)
        if throw <= 1:
            star_type = "B"
        if throw == 2:
            star_type = "A"
        if throw >= 3 and throw <= 8:
            star_type = "M"
        if throw == 9:
            star_type = "K"
        if throw == 10:
            star_type = "G"
        if throw >= 11:
            star_type = "F"
        if throw == 12:
            star_type = "K"
        if throw >= 13:
            star_type = "G"
        decimal3 = stellagama.dice(1, 10) - 1
        throw1 = stellagama.dice(2, 6)
        if throw1 == 2:
            throw = stellagama.dice(1, 6)
            if throw >= 1 and throw <= 3:
                size = "D"
            if throw >= 4 and throw <= 5:
                size = "III"
            if throw == 6:
                size = "II"
        if throw1 == 3:
            size = "IV"
        if throw1 >= 4:
            size = "V"
        if star_type == "A" or star_type == "F" or star_type == "G":
            if size == "D" or size == "II" or size == "III":
                size = "V"
        if star_type == "M" and size == "IV":
            size = "V"
        if star_type == "K" and size == "IV" and decimal1 >= 2:
            size = "V"
        if size == "D":
            star_type = ""
            decimal3 = ""
        tretiary.append(star_type)
        tretiary.append(decimal3)
        tretiary.append(size)
        startext3 = "%s%s%s " % (tretiary[0], tretiary[1], tretiary[2])

    startext4 = startext1 + startext2 + startext3
    startext = str.join('', startext4)
    return startext


def name_gen():
    """
	randomly chooses a world name from a list
	"""
    with open("names.txt") as namefile:
        name_list = namefile.readlines()
    base_name = stellagama.random_choice(name_list)
    base_name = base_name.strip()
    char_list = [base_name]
    length_count = int(7 - len(base_name) // 2)
    if int(len(base_name) % 2) == 0:
        length_count += 1
    if length_count <= 0:
        length_count = 0
    for i in range(1, length_count):
        char_list.append(" ")
    name = " ".join(char_list)
    return name  # output random name


# Testing area

print(name_gen())
