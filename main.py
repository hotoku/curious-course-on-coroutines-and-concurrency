from cobroardcast import broadcast
from cofollow import follow, printer
from copipe import grep


fp = open("access-log")
follow(
    fp,
    broadcast([
        grep("python", printer()),
        grep("ply", printer()),
        grep("swig", printer())
    ])
)
