from flask import Flask,jsonify
import re
import json
import num2words as n2w
import datetime
from datetime import time

app = Flask(__name__)

#current time shown in human friendly text
@app.route("/")
def current_time():
    today=datetime.datetime.now()
    t=timewords(today.hour,today.minute)
    return t

#specific time for human friendly text in terminal and json format in /time url
@app.route("/time")
def specific_time():
    #re for the HH:MM format
    pat = re.compile(r"(?:\d|[01]\d|2[0-3]):[0-5]\d")
    
    #Enter the time
    time = input("Enter the time in the HH:MM format: ")
    
    # Checks whether the input string matches the re.pattern
    if re.fullmatch(pat, time):
        full_time=time.split(':')
        hh=int(full_time[0])
        mm=int(full_time[1])
        t=timewords(hh,mm)
        print(t)
        return jsonify({'date': time,
                'human friendly clock':t})
    else:
        return f"'{time}' is NOT a valid time format !!. Please enter the time in HH:MM format."

def timewords(hh,mm):
    clock_time=''
    mid_words=''
    if hh >= 12:
        hours=hh % 12
    else:
        hours=hh
    numhh=n2w.num2words(hours)
    if mm == 0:
        clock_time=numhh +' '+ '''O'clock'''
    elif mm > 30:
        mid_words='to'
        hour=hh+1
        if hour >= 12:
            hours=hour % 12
        else:
            hours=hh
        numhh=n2w.num2words(hours)
        minutes=60-mm
        nummin=n2w.num2words(minutes)
        clock_time=nummin +' '+ mid_words +' '+ str(numhh)
    else:
        if mm == 30:
            nummin='half'
        else:
            nummin=n2w.num2words(mm)
        mid_words='past'
        clock_time=nummin +' '+ mid_words +' '+numhh
    time=clock_time.replace('-',' ')
    return time.capitalize()

if __name__=='__main__':
    app.run()