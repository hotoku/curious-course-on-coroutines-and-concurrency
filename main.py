from buses import buses_to_dicts, filter_on_filed, location
from cosax import EventHandler
from cofollow import printer
from xml.sax import parse

handler = EventHandler(
    buses_to_dicts(
        filter_on_filed(
            "id", "7574",
            location()
        )
    )
)
parse("bus.xml", handler)
