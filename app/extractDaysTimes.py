__author__ = 'glassman'

    classStartEnd = classDayTime[1].split('-') #Want to seperate start and stop times
    if classStartEnd[0].endswith('a'): #Find classes that start in the morning
        classStartEnd[0] = classStartEnd[0][:-1] #Strip the 'a'
        classStartHour = int(classStartEnd[0].split(':')[0]) #Strip hours
        classStartMinute = int(classStartEnd[0].split(':')[1]) #Strip minutes
    if classStartEnd[0].endswith('p'): #Find classes that start in the afternoon
        classStartEnd[0] = classStartEnd[0][:-1]
        if int(classStartEnd[0].split(':')[0]) == 12: #Find classes that start at noon
            classStartHour = int(classStartEnd[0].split(':')[0])
        else:
            classStartHour = int(classStartEnd[0].split(':')[0]) + 12 #All other afternoon classes put into 24hr
        classStartMinute = int(classStartEnd[0].split(':')[1])

    if classStartEnd[1].endswith('a'):
        classStartEnd[1] = classStartEnd[1][:-1]
        classEndHour = int(classStartEnd[1].split(':')[0])
        classEndMinute = int(classStartEnd[1].split(':')[1])
    if classStartEnd[1].endswith('p'):
        classStartEnd[1] = classStartEnd[1][:-1]
        if int(classStartEnd[1].split(':')[0]) == 12:
            classEndHour = int(classStartEnd[1].split(':')[0])
        else:
            classEndHour = int(classStartEnd[1].split(':')[0]) + 12
        classEndMinute = int(classStartEnd[1].split(':')[1])

    return classStartHour,classStartMinute,classEndHour,classEndMinute

def extractDaysOfWeek(classDayTime): #Comes in format -T-R-
    classDays = classDayTime[0].split('-') #Seperate all the days from the '-'
    daysWithClass = {'freq':'weekly'} #Make a dictionary
    daysInClass = [] #Make a temporary list
    for item in classDays:
        if item == 'M':
            daysInClass.append('MO') #Put item in list
        if item == 'T':
            daysInClass.append('TU')
        if item == 'W':
            daysInClass.append('WE')
        if item == 'R':
            daysInClass.append('TH')
        if item == 'F':
            daysInClass.append('FR')
    daysWithClass.update({'byday':daysInClass}) #Append a list of values for key 'byday'
    return daysWithClass