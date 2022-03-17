from xml.sax.handler import ContentHandler


class EventHandler(ContentHandler):
    def __init__(self, target):
        self.target = target

    def startElement(self, name, attrs):
        self.target.send(("start", (name, attrs._attrs)))

    def endElement(self, name):
        self.target.send(("end", name))

    def characters(self, content):
        self.target.send(("characters", content))
