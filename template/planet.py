class Planet(object):
  import random

  def __init__(self, hex):
    self.hex = hex
    self.uwp = "777456"
    self.port = "S"
    self.tc_string = ""

  def trade_codes(self):
    # Do stuff to generate trade codes
    tc_list = ["Na", "NI"]
    for tc in tc_list:
      self.tc_string += tc + " "

  def print_line(self):
    self.trade_codes()
    p_string = ""
    for p in self.port:
      p_string += p + " "

    print("%6s %5s %-20s %10s" % 
      (self.hex, self.port, self.tc_string, self.uwp))

planet_list = []
# Do the bits to determine if there's a planet in place.
planet_list.append(Planet("0101"))
planet_list.append(Planet("0104"))

for x in planet_list:
  x.print_line()
