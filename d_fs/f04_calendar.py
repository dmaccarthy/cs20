"""
CSE 2130: Files & File Structures
Sequential & direct Access
"""

# Complete these functions only...

def saveEvent(event, f, n=None):
    f.write(event["description"])

def loadEvent(f, n):
    pass


# DO NOT EDIT any of the code below.

from datetime import date, time

def test():
    cal = [{
        "date": date(2019, 1, 31),
        "description": "Semester 2 Begins"
    }, {
        "date": date(2019, 2, 2),
        "time": time(11, 30),
        "endTime": time(13, 0),
        "description": "Workout in Fitness Centre"
    }, {
        "date": date(2019, 2, 7),
        "description": "No School - Teachers Convention"
    }]
    filename = "calendar.txt"
    with open(filename, "w", encoding="latin-1") as f:
        for event in cal:
            saveEvent(event, f)
    revised = {
        "date": date(2019, 2, 2),
        "time": time(11, 0),
        "endTime": time(12, 30),
        "description": "Workout in Fitness Centre"
    }
    with open(filename, "r+", encoding="latin-1") as f:
        saveEvent(revised, f, 1)
        for event in range(len(cal)):
            print(loadEvent(f, event))

test()
