# timer
Set short-term alerts or timers in bash.

Alarms and timers are NOT saved, if you close your shell they are gone - which is part of the point of this timer. It's meant for quick and easy short-term notifications.

## Installation
Clone to your preferred spot.

Create a symlink to the python file: `sudo ln -s <path to timer.py> /usr/local/bin/timer`

..or use whatever is your preferred method.

## Usage
Set a countdown timer:

`timer -t 4m25s` - set a timer for 4 minutes and 25 seconds

`timer -t 1h18m`

`timer -t 30s -m "put a message to display here"`

Set an alarm:

`timer -a 0800 -m "Get ready for the important meeting" &` - sets an alarm for 8am. Make sure to send to the background with '&'.
