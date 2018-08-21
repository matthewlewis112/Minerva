from datetime import date
from datetime import timedelta

#Parent class for attributes
class attributes:
    id = 0
    name = ""
    def __init__(self, id, name):
        self.id = id
        self.name = name

#Version 1.0
class time(attributes):

    day = date.today()
    error = False

    def __init__(self):
        self.id = 1
        self.name = "time"
        self.day = date.today()
        self.error = False

    #Search for string that determines day
    def parseString(self, str):
        self.day = date.today()
        if "today" in str:
            return
        elif "tomorrow" in str:
            self.day += timedelta(days = 1)
        elif "yesterday" in str:
            self.day -= timedelta(days = 1)
        elif "days" in str:
            #check for day
            if "two" in str:
                coefficient = timedelta(days = 2)
            elif "three" in str:
                coefficient = timedelta(days = 3)
            elif "four" in str:
                coefficient = timedelta(days = 4)
            elif "five" in str:
                coefficient = timedelta(days = 5)
            elif "six" in str:
                coefficient = timedelta(days = 6)
            elif "seven" in str:
                coefficient = timedelta(days = 7)
            else:
                self.error = True

            #Add or subtract days
            if not self.error:
                if "ago" in str:
                    self.day -= coefficient
                elif "days from now" in str:
                    self.day += coefficient
                else:
                    self.error = True

class location(attributes):
    location = ""

    def __init(self):
        super(2, "location")
