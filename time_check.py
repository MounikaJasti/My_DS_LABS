import time


current_time = time.localtime()
time_inhour = current_time.tm_hour

if time_inhour > 19:
    print("time to wakeup")
    print("come on getup")
else:
    print("sleep till 19:00 hrs")

print("have a good day")
