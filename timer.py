#!/usr/bin/python
# installed via symbolic link: sudo ln -s $HOME/Documents/github/shtimer/shtimer.py /usr/local/bin/shtimer
import argparse
from datetime import datetime, timedelta
import time

argparser = argparse.ArgumentParser(prog='timer')
# common args
argparser.add_argument('-m', "--message", type=str, help='Display a message when timer or alarm completes.')

arggroup = argparser.add_mutually_exclusive_group(required=True)
arggroup.add_argument('-t', '--timer', help='Set a timer for the specified duration. Examples: 4m30s, 5m, 8h12m9s, "1m 8s".')
arggroup.add_argument('-a', '--alarm', help='Set an alarm to alert at a specified time. Examples: 0800, 1230, 1727.')
args = argparser.parse_args()
# print(args)


alert = """

████████╗██╗███╗   ███╗███████╗██╗
╚══██╔══╝██║████╗ ████║██╔════╝██║
   ██║   ██║██╔████╔██║█████╗  ██║
   ██║   ██║██║╚██╔╝██║██╔══╝  ╚═╝
   ██║   ██║██║ ╚═╝ ██║███████╗██╗
   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝
                                  
"""


def parse_time(value: str):
    time = {}
    units = ''

    for c in value:
        if c.isdigit():
            units += c
        if c.isalpha():
            time[c] = int(units)
            units = ''

    return time


def convert_to_seconds(value: str):
    time = parse_time(value)

    seconds = 0
    for k,v in time.items():
        if k == 'h':
            seconds += v * 60 * 60
        if k == 'm':
            seconds += v * 60
        if k == 's':
            seconds += v

    return seconds


def buzzer():
    print(alert)
    if args.message:
        print(args.message)
    for i in range(3):
        print('\007')
        time.sleep(.1)


def countdown(seconds: int):
    ani_str = '        >>'

    while seconds > 0:
        time_string = ' ' + time.strftime('%H:%M:%S', time.gmtime(seconds)) + ' '
        for i in range(10):
            if i == 0:
                t = time_string
            else:
                t = ani_str[-i:] + (time_string[i:])
            print(f"\r{t}", end="\r")
            time.sleep(.1)
        seconds -= 1
    print("          ", end="\r")
    print(f"\r{time.strftime('%H:%M:%S', time.gmtime(seconds))}")
    buzzer()


def alarm(set_time: str):
    alarm_time = datetime.strptime(datetime.now().strftime('%Y%m%d ') + set_time, '%Y%m%d %H%M')
    time.sleep((alarm_time - datetime.now()).seconds)
    buzzer()


if args.timer:
    seconds = convert_to_seconds(args.timer)
    countdown(seconds)
if args.alarm:
    alarm(args.alarm)
