import ctypes
from datetime import date
import time
from suntime import Sun, SunTimeException

latitude = {Latitude}
longitude = {Longitude}
sun = Sun(latitude, longitude)
delay = 10 #check tim every nth minute

while True:

    o_time = time.strftime("%H:%M")

    c_date = date.today()
    sun_r = sun.get_local_sunrise_time(c_date).strftime('%H:%M')
    sun_s = sun.get_local_sunset_time(c_date).strftime('%H:%M')

    while True:

        c_time = time.strftime("%H:%M")

        if o_time > c_time:
            break

        if c_time >= sun_r and c_time < sun_s: #change to day
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "{Absolute Path to Daytime img}" , 0)
        elif c_time >= sun_s: #change to night
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "{Absolute Path to Nighttime img}" , 0)
        
        o_time = c_time
        time.sleep(60 * delay)

        