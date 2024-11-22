#!/usr/bin/env python3
# Student ID: ivassiljenko

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    # Convert time objects to seconds
    t1_sec = time_to_sec(t1)
    t2_sec = time_to_sec(t2)
    
    # Add the seconds
    total_sec = t1_sec + t2_sec
    
    # Convert total seconds back to time object
    return sec_to_time(total_sec)

def change_time(time, seconds):
    """Change time by a given number of seconds (can be positive or negative)"""
    # Convert current time to total seconds
    total_sec = time_to_sec(time)
    
    # Add the seconds to total seconds
    total_sec += seconds
    
    # Convert total seconds back to time object
    return sec_to_time(total_sec)

def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0"""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def time_to_sec(t):
    """Convert a Time object to the total number of seconds since midnight"""
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    """Convert a number of seconds since midnight into a Time object"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return Time(hours, minutes, seconds)
