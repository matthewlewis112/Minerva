from datetime import date
from datetime import timedelta

#Parent class for attributes
class attributes:
    id = 0
    name = ""
    def __init__(self, id, name):
        self.id = id
        self.name = name

#Version 1.1
class time(attributes):

    day = date.today()
    error = False

    def __init__(self):
        self.id = 1
        self.name = "time"
        self.day = date.today()
        self.error = False

    #Search for string that determines day
    def parseString(self, textStr):
        self.day = date.today()
        if "today" in textStr:
            textStr.remove("today")
            return textStr
        elif "tomorrow" in textStr:
            self.day += timedelta(days = 1)
            textStr.remove("tomorrow")
            return textStr
        elif "yesterday" in textStr:
            self.day -= timedelta(days = 1)
            textStr.remove("yesterday")
            return textStr
        elif "days" in textStr:
            return self.daysFromToday(textStr)

    def daysFromToday(self, textStr):
        #check for errors
        assert "days" in textStr
        index = textStr.index("days")
        dayNumbers = { "two" : 2,
                      "three": 3,
                      "four": 4,
                      "five": 5,
                      "six": 6,
                      "seven": 7 }
        #assert textStr[index - 1] in dayNumbers, textStr[index - 1]
        self.day = date.today()

        if "ago" == textStr[index + 1]:
            self.day -= timedelta(days = dayNumbers[textStr[index - 1]])
            del textStr[index - 1]
            textStr.remove("days")
            textStr.remove("ago")
            return textStr
        else:
            self.day += timedelta(days = dayNumbers[textStr[index - 1]])
            del textStr[index - 1]
            textStr.remove("days")
            textStr.remove("from")
            textStr.remove("now")
            return textStr


class location(attributes):
    location = ""

    def __init(self):
        super(2, "location")
