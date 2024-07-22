class Solution:
    def convertToDays(date):
        #Converting the date to days
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        days = 0
        for i in range(1971, year):
            if i % 4 == 0:
                days += 366
            else:
                days += 365
        
        for i in range(1, month):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                days += 31
            elif i == 2:
                if year % 4 == 0:
                    days += 29
                else:
                    days += 28
            else:
                days += 30
                
        days += day
        return days
    
    def daysBetweenDates(date1, date2):
        #Converting the dates to days
        date1 = date1.split("-")
        date2 = date2.split("-")
        days1 = Solution.convertToDays(date1)
        days2 = Solution.convertToDays(date2)
        if days1 > days2:
            return days1 - days2
        else:
            return days2 - days1

    
date1 = "2020-01-15"
date2 = "2019-12-31"

answer = Solution.daysBetweenDates(date1, date2)
print(answer)  # Output: 15