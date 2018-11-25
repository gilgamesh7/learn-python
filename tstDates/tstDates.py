import os 
from datetime import date 
from datetime import time
from datetime import datetime
from datetime import timedelta

def tstMyDate():
    today=date.today()
    dateTuple="["+str(today.day)+","+str(today.month)+","+str(today.year)+"]"
    #print("{0}".format(dateTuple))
    for i,myStr in enumerate(dateTuple):
        print("{0},{1}".format(i,myStr))
  
    myEnv=os.name
    print("{0}".format(myEnv))
    
    myTime=datetime.time(datetime.now())
    myHr=myTime.hour
    myMin=myTime.minute
    mySec=myTime.second
    print("{0},{1},{2}".format(myHr,myMin,mySec))
    
    nowTime=datetime.now()
    print(nowTime.strftime("The year is : %Y,%y,%a,%A,%b,%B,%D,%d"))
    print(nowTime.strftime("LOcale : %c , %x, %X, %C"))
    print(nowTime.strftime("Time : %I,%H,%M,%S,%p"))
    
    nowDate = datetime.now()
    print("8 months ago was : {0}".format(str(nowDate - timedelta(days=240))))
    
    nowDate = datetime.today()
    aprilFD = datetime(nowDate.year,4,1)
    if (aprilFD < nowDate) :
        aprilFD=aprilFD.replace(year=nowDate.year+1)
        
    print("Today : {0} , aprilFD : {1}".format(nowDate,aprilFD))
    deltaAFD = nowDate-aprilFD
    print("Days to/From AFD this year : {0}".format(deltaAFD))
    
    nowDate=datetime.today()
    twoMonthsFromNow = nowDate.replace(month=nowDate.month+1)
    print("Now : {0} , 2 months from now : {1}".format(nowDate,twoMonthsFromNow))

if __name__ == '__main__':
    tstMyDate()
    
exit(1)