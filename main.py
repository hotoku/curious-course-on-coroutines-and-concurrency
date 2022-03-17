import xml.sax
from basicsax import Handler

xml.sax.parse("bus.xml", Handler())
