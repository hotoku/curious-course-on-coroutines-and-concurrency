# cocrash.py
#
# An example of hooking coroutines up in a way that might cause a potential
# crash.   Basically, there are two threads feeding data into the
# printer() coroutine.

from copipe import grep
from cobroardcast import *
from cofollow import printer
from cothread import threaded

p = printer()
target = broadcast([threaded(grep('foo', p)),
                    threaded(grep('bar', p))])

# Adjust the count if this doesn't cause a crash
for i in range(10):
    target.send("foo is nice\n")
    target.send("bar is bad\n")

del target
del p
