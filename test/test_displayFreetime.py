import pytest
import os
import sys
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/../src"))
from datetime import datetime
from datetime import timedelta
from datetime import time
from functionality.DisplayFreeTime import compute_free_time
from Event import Event


# all of the test cases data are generated by the date of today but with a fixed schedule hours of the events

def test_EventsAfterMidNight():

    # Test case if all of the events are not at midnight
    t = datetime.today()
    a = []
    a.append(Event('',datetime(t.year, t.month,t.day , 4 , 0),datetime(t.year, t.month,t.day , 5 , 0) ,'','' ))
    a.append(Event('',datetime(t.year, t.month,t.day , 1 , 0),datetime(t.year, t.month,t.day , 2 , 0) ,'','' ))
    o = compute_free_time(a)
    ex = 'Free time from 00:00 until 00:59:00\nFree time from 02:01:00 until 03:59:00\nFree time from 05:01:00 until 23:59'
    assert o.strip() == ex.strip()

    


def test_EventsStartsAtMidNight():

    # Test case if one of the events starts at midnight

    t = datetime.today()
    a = []
    a.append(Event('',datetime(t.year, t.month,t.day , 4 , 0),datetime(t.year, t.month,t.day , 6 , 0) ,'','' ))
    a.append(Event('',datetime(t.year, t.month,t.day , 7 , 0),datetime(t.year, t.month,t.day , 17 , 0) ,'','' ))
    a.append(Event('',datetime(t.year, t.month,t.day , 0 , 0),datetime(t.year, t.month,t.day , 2 , 0) ,'','' ))
    o = compute_free_time(a)
    ex = 'Free time from 02:01:00 until 03:59:00\nFree time from 06:01:00 until 06:59:00\nFree time from 17:01:00 until 23:59'
    assert o.strip() == ex.strip()


def test_EventsEndsAtMidNight():

    # Test case if one of the events ends at midnight

    t = datetime.today()
    a = []
    a.append(Event('',datetime(t.year, t.month,t.day , 14 , 0),datetime(t.year, t.month,t.day , 16 , 0) ,'','' ))
    a.append(Event('',datetime(t.year, t.month,t.day , 17 , 0),datetime(t.year, t.month,t.day , 23 , 59) ,'','' ))
    a.append(Event('',datetime(t.year, t.month,t.day , 0 , 0),datetime(t.year, t.month,t.day , 2 , 0) ,'','' ))
    o = compute_free_time(a)
    ex = 'Free time from 02:01:00 until 13:59:00\nFree time from 16:01:00 until 16:59:00'
    assert o.strip() == ex.strip()

test_EventsAfterMidNight()
test_EventsStartsAtMidNight()
test_EventsEndsAtMidNight()