'''
Author:    Michael Sherif Naguib
Date:      May 7, 2019
@:         University of Tulsa

Question #19: 
You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

#Converts a month number index to a name: 0=jan... 11=dec
def monthIndexToStr(idx):
    nameLookup={0:'jan',1:'feb',2:'mar',3:'apr',4:'may',5:'jun',6:'jul',7:'aug',8:'sep',9:'oct',10:'nov',11:'dec'}
    return nameLookup[idx]

#determines if a given year is a leap year
def isLeapYear(year):
    return ((year%100==0) and(year%400==0)) or ((year%4==0) and (not year%100==0))

if __name__ =="__main__":
    '''
    my approach: brute force (although must be efficient) is probably not that bad... 999 years * approx 365 ... approx 1k*365 = 365k
    '''
    
    #indexed Jan = month 0 and Dec = month 11: each holds normal day count...
    monthsDays={0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
    #Set the starting year...
    year=1900
    #let the numbers 0-6 represent the days of the week: Sun=0 Mon=1 Tues=3 ... Sat=6; set the curent day of the week (mon)
    weekDay=1
    #let this count how many days have passed in the moth example 1st of jan ==> day=1 22 of jan day=22 ....ect...
    day=1#INIT TO ZERO TO CHECK THE FIRST DAY
    #set the current month (jan)
    month=0
    #keeps track of the sundays...
    sundayCount=0
    while not (year==2000 and month==11 and day==31):
        #========================================== LOG
        #if year%10==0 and month==11 and day == 1:
        #    print("Year:{0}".format(year))

        #Check if condition met
        if weekDay==0 and day==1 and year>=1901:
            sundayCount+=1

        #is it a year where feburary must change # of days?
        if isLeapYear(year):
            monthsDays[1]=29
        else:
            monthsDays[1]=28
        #Turn the year: (increment year)
        inc_year_condition=(month==11 and day==monthsDays[11])
        if inc_year_condition:
            month=0
            day=1
            year+=1
        #turn the month: increment month: if its not this super specific day of the year in feb
        inc_month_condition= (day == monthsDays[month])
        if inc_month_condition:
            day=1
            month+=1
        #increment the week day and day
        if not (inc_month_condition or inc_year_condition):
            day+=1
            weekDay = (weekDay+1)%7



print(sundayCount)
        



        

    
    
    