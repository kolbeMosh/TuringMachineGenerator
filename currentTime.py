# Written By: Kolbe Mosher
# Purpose: A helper class to get the current time
#          and format to use for file paths

import time

class currentTime:
    def __init__(self):
        self.date = time.gmtime()
        self._year = self.date[0]
        self._month = self.date[1]
        self._day = self.date[2]
        self._hour = self.date[3]
        self._minute = self.date[4]
        self._second = self.date[5]

    def _getYear(self):
        return self._year
    
    def _getMonth(self):
        return self._month
    
    def _getDay(self):
        return self._day
    
    def _getHour(self):
        return self._hour
    
    def _getMinute(self):
        return self._minute
    
    def _getSecond(self):
        return self._second
    
    
    year = property(_getYear)
    month = property(_getMonth)
    day = property(_getDay)
    hour = property(_getHour)
    minute = property(_getMinute)
    second = property(_getSecond)

    def __str__(self):
        return f'{self._year}_{self._month}_{self._day}_{self._hour}_{self._minute}_{self._second}'