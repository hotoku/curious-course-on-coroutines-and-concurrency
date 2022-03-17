from buses import buses_to_dicts, filter_on_filed, location
from coexpat import expat_parse


expat_parse(
    open("bus.xml", "rb"),
    buses_to_dicts(
        filter_on_filed(
            "id", "7574",
            location()
        )
    )
)
