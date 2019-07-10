#pomodoro timer

import time


workTimeSec = 1500
breakTimeSec = 300

workTimeStartMessage = "Worktime has started. You have 25 minutes!"
workTimeDone = "Time to break!"

startTime = time.time()

print("Worktime has started. You have 25 minutes!")
while time.time() != startTime + workTimeSec:
    pass

breakTimerStartAlert = print(workTimeDone)
startTime = time.time()
while time.time() != startTime + breakTimeSec:
    pass
