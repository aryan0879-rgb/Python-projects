# greets good morning, good afternoon, good evening and good night
from datetime import datetime
name= input ("enter your name: ")
current_time= datetime.now()
hour=current_time.hour
print (hour)
if 5<=hour<12:
    print ("good morning", name)
elif 12<=hour<16:
    print("good afternoon", name)
elif 16<=hour<21:
    print("good evening",name)
else:
    print("good night", name)