import xml.sax.handler
import xml.sax


class Handler(xml.sax.handler.ContentHandler):
    def startElement(self, name, attrs):
        print("startElement", name)

    def endElement(self, name):
        print("endElement", name)

    def characters(self, content):
        print("characters", repr(content)[:40])
