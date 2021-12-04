from datetime import date
from datetime import datetime as dt
import json
import os

def hr():
    if hr1>=9 and hr1<=17:
        return str(hr1)+":"+str(minutes)
    else:
        print("it is not valid time.")
        print("office time is 09:00:00 to 17:00:00")
        hr()

print("***** welcome to unique booking system***** ")

print(("The company office timing is 09:00:00 to 17:00:00"))
 
today = date.today()

now = dt.now()

s = now.strftime("%H:%M:%S")

employee_id=input("enter the employee id : ")
year=int(input("enter the year : "))
month=int(input("enter the month : "))
date1=int(input("enter the date : "))
my_date = date(year, month, date1)


hr1=int(input("which time do you want meeting?(in hour) : ")) 
minutes=int(input("which time do you want meeting?(in minutes) : "))
meeting_duration=int(input("enter the meeting time duration: "))
meeting=str(hr1+meeting_duration)+":"+str(minutes)


hour=hr()  
meeting_time=hour+" "+"to"+" "+meeting


 
print(today,s,employee_id)
print(my_date,hour,meeting_duration,meeting_time)
file=os.path.exists("Booking file.json")
if file==True:
    w=open("Booking file.json","r")
    usname=w.read()
    if  str(my_date)in usname:
        if hour in usname:
            print("your booking is cancelled")
            print("Because of this time meeting is already booked ")
    if str(my_date)in usname:
        if hour not in usname:
            mylist=[]
            mydic={}
            mydic["Employee Id"]=employee_id
            mydic["Submission Date"]=str(today)
            mydic["Submission Time"]=s
            mydic["meeting_date"]=str(my_date)
            mydic[" Start Meeting Time"]=hour
            mydic["Meeting Duration"]=meeting_duration
            mydic["Meeting Time"]=meeting_time
            # mylist.append(mydic)
            with open("Booking file.json","r")as p:
                data=json.load(p)
                data.append(mydic)
                with open("Booking file.json","w")as p:
                    json.dump(data,p,indent=4)

    else:
        
        mydic={}
        mydic["Employee Id"]=employee_id
        mydic["Submission Date"]=str(today)
        mydic["Submission Time"]=s
        mydic["meeting_date"]=str(my_date)
        mydic[" Start Meeting Time"]=hour
        mydic["Meeting Duration"]=meeting_duration
        mydic["Meeting Time"]=meeting_time

        with open("Booking file.json","r")as p:
                data=json.load(p)
                data.append(mydic)
                with open("Booking file.json","w")as p:
                    json.dump(data,p,indent=4)

else:
    mylist=[]
    mydic={}
    mydic["Employee Id"]=employee_id
    mydic["Submission Date"]=str(today)
    mydic["Submission Time"]=s
    mydic["meeting_date"]=str(my_date)
    mydic[" Start Meeting Time"]=hour
    mydic["Meeting Duration"]=meeting_duration
    mydic["Meeting Time"]=meeting_time
    mylist.append(mydic)

    with open("Booking file.json","a")as p:
        json.dump(mylist,p,indent=4)
 



 