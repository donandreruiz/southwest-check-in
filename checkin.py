#! usr/bin/python
# southwest airlines check in script

# imports
from selenium import webdriver
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import schedule
import time
import datetime
#from datetime import datetime
import sys

# get user name and flight information 
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
confirmation_num = input("Please enter your confirmation number: ")
flight_date = input("What date is your flight on? (format: YY-MM-DD): ")
flight_time = input("At what time is the flight? (ex 2:45AM or 2:45PM): ")





def time_to_run(date2):
    fmt = '%Y-%m-%d %H:%M:%S'
    now = str(datetime.datetime.now())
    now = now[0:16]
    now = now+':00'
    d1 = datetime.datetime.strptime(now, fmt)
    d2 = datetime.datetime.strptime(date2, fmt)

    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())

    times = int(d2_ts - d1_ts) / 60
    return times



def convert_time():
    minutes = flight_time[3:5]
    hour = flight_time[:2]
    if flight_time[-2:].lower() == 'pm':
        if hour == 12:
            hour = 0
        else:
            hour_int = int(hour)
            hour_int+= 12
            hour = str(hour_int)
        time_check = hour+':'+minutes+'PM'
    else:
        time_check = hour+':'+minutes+"AM"

    return time_check


def check_me_in():
    print("Checking you in now!")

    # load the southwest webpage
    browser = webdriver.Safari()
    browser.get('https://www.southwest.com/air/check-in/index.html')

    # enter the values given
    browser.find_element_by_id('confirmationNumber').send_keys(confirmation_num)
    browser.find_element_by_id('passengerFirstName').send_keys(first)
    browser.find_element_by_id('passengerLastName').send_keys(last)

    # submit the form
    browser.find_element_by_id('form-mixin--submit-button').click()



time_check = convert_time()
time_check = flight_date+' '+time_check[:-2]+':00'


def scheduler_check_in(check_minutes):
    print("I'm waiting to check in!.. Please don't turn me off")
    check_minutes = int(check_minutes)
    schedule.every(check_minutes).minutes.do(check_me_in)
    while True:
        schedule.run_pending()
        time.sleep(1)


time_check_user = input('Just to confirm, your flight is at '+time_check+', your name is '+first +' ' +last+' and your confirmation number is ' +confirmation_num+ ' correct? (Y/N): ' )


if time_check_user.lower() == 'y':
    minute_until_check = time_to_run(time_check)
    scheduler_check_in(minute_until_check)
else:
    print('restart the whole process!')
    sys.exit()






