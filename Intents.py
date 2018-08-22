from Attributes import *

#Parent class for intent
class intent:
    id = 0
    name = ""
    attributes = []

    def __init__(self, id, name, attributes):
        self.id = id
        self.name = name
        self.attributes = attributes

class weather(intent):

    def __init__(self):
        self.id = 1
        self.name = "weather"
        self.attributes = { "day" : time() }

    def parseString(self, str):
        arr = str.lower().strip("?.!").split(" ")

        assert type(arr) == list
        self.attributes["day"].parseString(arr)
