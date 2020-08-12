from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    today=date.today()
    print("Todays date is ", today)
    print(today.day, today.year, today.month, today.weekday())
    days=["MON","TUE", "WED", "THUR","FIR", "SAT", "SUN"]
    print("today day is ", days[today.weekday()])
    today=datetime.now()
    print(today.strftime("adf %Y\n%a\n%A\n%b\n%B\n%d\n%D\n%x\n%X \n%c"))
    # time formatting
    print(today.strftime("%I:%M:%S %p") )
    # 24 hour
    print(today.strftime("%H:%M:%S") )
    
main()