from cobroardcast import broadcast
from cofollow import follow, printer
from copipe import grep


fp = open("access-log")
p = printer()
follow(
    fp,
    broadcast([
        grep("python", p),
        grep("ply", p),
        grep("swig", p)
    ])
)
