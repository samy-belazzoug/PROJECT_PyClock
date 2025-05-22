import datetime
import sys
import time

def set_time(d:tuple,format:int):
    """setup time"""
    tempo = [item for item in d]
    d = tempo
    #seconds
    if d[2] < 60:
        d[2] += 1
    if d[2] >= 60:
        d[1] += 1
        d[2] = 0
    #minutes
    if d[1] >= 60:
        d[0] += 1
        d[1] = 0
    #hours
    if format == 24 and d[0] >= 24:
        d = (0,0,0)
    if format == 12 and d[0] >= 12:
        d = (0,0,0)

    tempo = (d[0],d[1],d[2])
    d = tempo
    return d

def display_time(date:tuple):
    """update date displayed"""
    
    if date[0] < 10 and date[1] < 10 and date[2] < 10:
        return f"0{date[0]}:0{date[1]}:0{date[2]}"
    
    if date[0] < 10 and date[1] < 10 and date[2] >= 10:
        return f"0{date[0]}:0{date[1]}:{date[2]}"
    
    if date[0] < 10 and date[1] >= 10 and date[2] < 10:
        return f"0{date[0]}:{date[1]}:0{date[2]}"
    
    if date[0] < 9 and date[1] >= 10 and date[2] >= 10:
        return f"0{date[0]}:{date[1]}:{date[2]}"
    
    if date[0] >= 10 and date[1] < 10 and date[2] < 10:
        return f"{date[0]}:0{date[1]}:0{date[2]}"
    
    if date[0] >= 10 and date[1] < 10 and date[2] >= 10:
        return f"{date[0]}:0{date[1]}:{date[2]}"
    
    if date[0] >= 10 and date[1] >= 10 and date[2] < 10:
        return f"{date[0]}:{date[1]}:0{date[2]}"
    
    if date[0] >= 10 and date[1] >= 10 and date[2] >= 10:
        return f"{date[0]}:{date[1]}:{date[2]}"

def alarm(t:tuple,delta:tuple):
    """set an alarm and display a message when done"""
    while t != delta:
        i = set_time(t)
        t = i
        print(t)
        time.sleep(0.2)
    print("C'EST L'HEURE!")
        
#BONUS

def display_mode(mode:int):
    """switch to AM/PM mode"""
    pass

def pause_time():
    """pause the time displayed"""
    
def display(d:tuple,format:int):
    while 1:
        i = set_time(d,format)
        d = i
        print(display_time(d))
        time.sleep(1)

hour = 11
minute = 59
second = 55
d = (hour,minute,second)

display(d,12)