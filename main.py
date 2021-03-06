from xml.sax import parse

from buses import buses_to_dicts, filter_on_filed, location
from cosax import EventHandler
from cothread import threaded


parse(
    "bus.xml",
    EventHandler(
        buses_to_dicts(
            threaded(
                filter_on_filed(
                    "id", "7574",
                    location()
                )
            )
        )
    )
)
