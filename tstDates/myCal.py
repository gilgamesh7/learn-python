import calendar

def tstCal():
   myCal=calendar.TextCalendar(calendar.MONDAY)
   fmtMyCal=myCal.formatmonth(2018, 11, 1, 1)
   print(fmtMyCal)

   for myMonth in range(1,13):
       myCal=calendar.TextCalendar(calendar.MONDAY)
       fmtMyCal=myCal.formatmonth(2018,myMonth,1,1)
       print(fmtMyCal)
       
if __name__ == '__main__':
    tstCal()
    
exit(1)