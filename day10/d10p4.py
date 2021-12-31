def alarm_clock(day, is_vacation):
    if is_vacation == False:
        if 1 <= day <= 5:
            alarm = '7:00'
        elif day == 0 or day == 6:
            alarm = '10:00'
        return alarm
    elif is_vacation == True:
        if 1 <= day <= 5:
            alarm = '10:00'
        elif day == 0 or day == 6:
            alarm = 'off'
        return alarm

alarm = alarm_clock(6, True)
print(alarm)
alarm = alarm_clock(5, False)
print(alarm)
alarm = alarm_clock(0, False)
print(alarm)