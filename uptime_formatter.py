"""
Author: Durim Miziraj
2023-06-03T20:26:13
"""

import utime

class StandardFormat:

    def formatted_uptime_info():
            
        # Calculating total uptime in seconds, minutes, hours and days
        uptime_seconds = int((utime.ticks_ms())/1000)
        uptime_minutes = int(uptime_seconds/60)
        uptime_hours = int(uptime_minutes/60)
        uptime_days = int(uptime_hours/24)

        # Calculating the current duration of uptime in a standard format 
        current_seconds = uptime_seconds % 60
        current_minutes = uptime_minutes % 60
        current_hours = uptime_hours % 24

        # Formatting the current uptime in days, hours, minutes and seconds
        return f"{uptime_days} days, {current_hours} hours, {current_minutes} minutes, {current_seconds} seconds"
