# timer
Set short-term alerts or timers in bash.

## Usage
Set a countdown timer:

`timer -t 4m25s` - set a timer for 4 minutes and 25 seconds
`timer -t 1h18m`
`timer -t 30s -m "put a message to display here"`

Set an alarm:

`timer -a 0800 -m "Get ready for the important meeting" &` - sets an alarm for 8am. Make sure to send to the background with '&'.
