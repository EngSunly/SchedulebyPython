
from datetime import datetime
date = datetime.now().date()
day = date.weekday()+1

    
monday = 'Info Sys Analysis and Computer Network'
tuesday = 'Info Sys Analysis and Java Program'
wednesday = 'Statistic Analysis and C# Dot Net Program'
thursday = 'Computer Network and Java Program'
friday = 'Statistic Analysis and C# Dot Net Program'
saturday = 'Enjoy'
sunday = 'Enjoy'


def sec():
    print('A simple program for finding schedule of the day\n')

    if day == 1:
        print('Monday')
        print(monday+'\nTmr\n'+tuesday)
    if day == 2:
        print('Tuesday')
        print(tuesday+'\nTmr\n'+wednesday)
    if day == 3:
        print('Wednesday ')
        print(wednesday+'\nTmr\n'+thursday)
    if day == 4:
        print('Thursday')
        print(thursday+'\nTmr\n'+friday)
    if day == 5:
        print('Friday')
        print(friday+'\nTmr\n'+saturday)
    if day == 6:
        print('Saturday')
        print(saturday+'\nTmr\n'+sunday)
    if day == 7:
        print('Sunday')
        print(sunday+'\nTmr\n'+monday)
    print("\nFull Week Class\n"+monday+"\t"+tuesday+"\t"+wednesday+"\n"+thursday+"\t"+friday+"\t"+saturday)
    input('Press Any key to Exit ')


sec()

