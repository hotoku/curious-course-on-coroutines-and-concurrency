from buses import buses_to_dicts
from cosax import EventHandler
from cofollow import printer
from xml.sax import parse

handler = EventHandler(buses_to_dicts(printer()))
parse("bus.xml", handler)
