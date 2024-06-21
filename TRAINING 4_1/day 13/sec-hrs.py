'''
ip:7262 seconds
op:2h:1m:2s
'''

def seconds_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours}h:{minutes}m:{seconds}s"
seconds = int(input())
print(seconds_to_hms(seconds))



#every month -30 days, week-6 days
#1 month = 5 weeks
#65476 days...how many years, months,weeks,days

def daysyears(days):
    years = days//360
    days%=360
    months = days//12
    days%=12
    weeks = days//6
    days%=6
    return f"{years}y:{months}m:{weeks}w:{days}d"
days = int(input())
print(daysyears(days))
    