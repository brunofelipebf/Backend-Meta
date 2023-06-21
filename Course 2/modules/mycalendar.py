import sys
import calendar

#sys
locations = sys.path
print(locations)

for i in locations:
    print(i)



#calendar
calendar.leapdays(2000, 2050)
#print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)