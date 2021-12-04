from datetime import date
# import task1 
import json
year=int(input("enter the year : "))
month=int(input("enter the month : "))
date1=int(input("enter the date : "))
my_date = date(year, month, date1)
 
with open ("Booking file.json","r")as p:
    data=json.load(p)
print(str(my_date))
for i in data:
    # print(i)
    if i["meeting_date"]==str(my_date):
        print(i["Meeting Time"],i["Employee Id"])
    # else:
print("this date is no any meeting available")
        # break