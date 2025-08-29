#DAY = 15
#date = 25-5-2025
# porject = 2 good m
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
if(timestamp == "13:24:00"):
    print("Good Morning sir")
elif(timestamp == "13:28:00"):
    print("Good After noon Sir")
else:
    print("Good Day Sir")