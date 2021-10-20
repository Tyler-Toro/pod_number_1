# add built-in date and time functionality
# add ability to have sound using pip3 install playsound (after pip install playsound didn't work)

# initial attempt unsuccessful, ran /opt/homebrew/opt/python@3.9/bin/python3.9 -m pip install --upgrade pip to upgrade pip, may resolve general pip issues have had, still unsure reasons playsound unresolved, but pip list now lists installs (do not need to run pip3 list)

# she throws the victory stance and the code crowd goes wild ... I closed out and re-entered and playsound is now resolved ...

# But alarm still not working
from datetime import datetime
from playsound import playsound

print('\nSET ALARM IN FORMAT HH:MM:SS')
alarm_time = input('Enter Alarm Time:\n')
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print('Alarm set ...')

while True:
    now = datetime.now()
    current_hour = now.strftime('%I')
    current_minute = now.strftime('%M')
    current_seconds = now.strftime('%S')
    current_period = now.strftime('%p')

    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print('Get Up! Get Up! Get Up!')
                    playsound('sounds/alarmclock.mp3')
                    break