from Intents import *

def main():
    weatherTester()

def weatherTester():
    relativeDay1 = date.today() - timedelta(days = 1)
    relativeDay2 = date.today()
    relativeDay3 = date.today() + timedelta(days = 1)
    relativeDay4 = date.today() + timedelta(days = 3)
    relativeDay5 = date.today() - timedelta(days = 2)
    relativeDay6 = date.today() + timedelta(days = 2)

    w1 = weather()
    w1.attributes["day"].parseString("What is the weather yesterday?")
    w2 = weather()
    w2.attributes["day"].parseString("What is the weather today?")
    w3 = weather()
    w3.attributes["day"].parseString("What is the weather tomorrow?")
    w4 = weather()
    w4.attributes["day"].parseString("What is the weather three days from now?")
    w5 = weather()
    w5.attributes["day"].parseString("What is the weather two days ago?")
    w6 = weather()
    w6.attributes["day"].parseString("What is the weather two days from now?")

    assert relativeDay1 == w1.attributes["day"].day
    assert relativeDay2 == w2.attributes["day"].day
    assert relativeDay3 == w3.attributes["day"].day
    assert relativeDay4 == w4.attributes["day"].day
    assert relativeDay5 == w5.attributes["day"].day
    assert relativeDay6 == w6.attributes["day"].day

if __name__ == "__main__":
    main()
