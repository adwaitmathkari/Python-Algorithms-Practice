import datetime

def getWorkday(date):

    day=date.day
    weekday=date.weekday()

    nonWorkDays=0
    for i in range(day, 0, -1):
        # print(i)
        if weekday==6 or weekday==5:
            nonWorkDays+=1
        if weekday==0:
            weekday=6
        else:
            weekday-=1

    workDay=day-nonWorkDays
    return workDay


# print(getWorkday(datetime.datetime(2019,10,15)))
# print(getWorkday(datetime.datetime.today()))

