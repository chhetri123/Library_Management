import datetime
from datetime import date
def getDate():
    x = datetime.datetime.now
    return str(x().date())
def getTime():
    x=datetime.datetime.now
    return str(x().strftime("%I:%M:%S %p"))

def getRemainingDate(rdate):
    year=int(rdate[0])
    mon=int(rdate[1])
    day=int(rdate[2])+10  # return date is fixed i.e 10 you can change it 
    if day>30:
        mon=mon+day/30
        day=day%30
    if mon>12 :
        year=year+mon/12
        mon=mon%12
    returnDate = date(year, mon, day)
    currentDate = date.today()
    remainingDate = returnDate - currentDate   
    return remainingDate.days

