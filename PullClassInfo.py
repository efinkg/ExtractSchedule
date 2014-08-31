__author__ = 'glassman'
import extractDaysTimes
import makeCalendar
import getDates
#We plan to make iCal files Google Calendar can understand

from BeautifulSoup import BeautifulSoup

classList = BeautifulSoup(open('Class Schedule.html'))

semester = classList.find(selected="selected")
fallSpring = semester.contents[0][0:2]
year = semester.contents[0][2:6]
firstMonth,firstDay,lastMonth,lastDay = getDates.findBeginEnd(fallSpring,year)
classYear = int(year)
enrolledClasses = []

classesTable = classList.find(id='tabSched')
rows = classesTable.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    classInfo = []
    classCSVRow = []
    for td in cols:
        for item in td:
            classInfo.append(item.string)
    if classInfo[0] == 'Enrolled':
        classTime = classInfo[5]
        classDayTime = classTime.split(' ') #classDayTime[0] is the days of the week
                                            #classDatTime[1] is the start-end time
        classStartHour,classStartMinute,classEndHour,classEndMinute = extractDaysTimes.extractStartStopTimes(classDayTime)
        classDaysOfWeek = extractDaysTimes.extractDaysOfWeek(classDayTime)
        className = classInfo[2]
        classLocation = classInfo[6]
        enrolledClasses.append([className,classLocation,classYear,firstMonth,lastMonth,firstDay,lastDay,classStartHour,classStartMinute,classEndHour,classEndMinute,classDaysOfWeek])
makeCalendar.write(enrolledClasses)