import datetime
def getDate():
    x = datetime.datetime.now
    return str(x().date())
def getTime():
    x=datetime.datetime.now
    return str(x().strftime("%I:%M:%S %p"))
