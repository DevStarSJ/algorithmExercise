# 0 : Sunday ~ 6: Saturday
def getDay(current, days):
    return (current + days) % 7

def isLeafYear(year):
    if year % 100 == 0:
        return True if year % 400 == 0 else False
    return year % 4 == 0

DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def moveNextMonth(currentYear, currentMonth, currentDay):
    days = DAYS[currentMonth - 1]
    if isLeafYear(currentYear) and currentMonth == 2:
        days += 1
    nextDay = getDay(currentDay, days)
    nextMonth = (currentMonth % 12) + 1
    nextYear = currentYear if nextMonth > 1 else currentYear + 1
    return nextYear, nextMonth, nextDay

year, month, day = 1900, 1, 1
count_sunday = 0

while year < 2001:
    year, month, day = moveNextMonth(year, month, day)
    if 1901 <= year <= 2000:
        if day == 0:
            count_sunday += 1

print(count_sunday)

