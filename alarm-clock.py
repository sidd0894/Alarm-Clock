import time as t
import datetime as dt
from win10toast import ToastNotifier

def setDate():
    print('\nProvide the reminder date-')
    while (True):
        try:
            dayMonthYear = (input('D-M-YYYY : ')).split('-')
            # dayMonthYear = dayMonthYear.split('-')
            dateList = []
            for e in dayMonthYear:
                dateList.append(int(e))


            # Check if input is in D-M-Y format or not.
            if (len(dayMonthYear) != 3):
                print('Invalid input')

            # Check if input month number is valid or not.
            elif (int(dayMonthYear[1]) < 1 or int(dayMonthYear[1]) > 12):
                print(f'Invalid month number- {int(dayMonthYear[1])}')

            # Check if input year is >= present year or not.
            elif (int(dayMonthYear[2]) < t.localtime().tm_year):
                print(f'Invalid year number- {int(dayMonthYear[2])}. Year should be {t.localtime().tm_year} or greater.')

            # Check if date is valid.
            elif (int(dayMonthYear[0]) > 0 and int(dayMonthYear[0]) < 32):

                if (int(dayMonthYear[1]) in [1, 3, 5, 7, 8, 10, 12] and int(dayMonthYear[0]) > 31):
                    print(f'Invalid Date-1 {int(dayMonthYear[0])}')
                elif (not int(dayMonthYear[1]) in [1, 3, 5, 7, 8, 10, 12] and int(dayMonthYear[0]) > 30):
                    print(f'Invalid Date2- {int(dayMonthYear[0])}')
                
                # Check if input date is valid for leap year.
                elif (int(dayMonthYear[2]) % 4 == 0):
                    if (int(dayMonthYear[1]) == 2 and int(dayMonthYear[0]) > 29):
                        print(f'Invalid Date3- {int(dayMonthYear[0])}')
                    else:
                        return dayMonthYear
                        # break

                # Check if input date is valid for non-leap year.
                elif (int(dayMonthYear[2]) % 4 != 0):
                    if (int(dayMonthYear[1]) == 2 and int(dayMonthYear[0]) > 28):
                        print(f'Invalid Date4- {int(dayMonthYear[0])}')
                    else:
                        return dayMonthYear
                        # break

            else:
                print(f'Invalid Date5- {int(dayMonthYear[0])}')
        except ValueError:
            print('Invalid input.')

# Set time.
def setTime():
    print('\nEnter the time in 24-hour format-')
    while (True):
        try:
            hourMin = input('H-M : ').split('-')
            timeList = []
            for e in hourMin:
                timeList.append(int(e))

            if (len(hourMin) != 2):
                print('Invalid input')

            elif (int(hourMin[0]) >= 0 and int(hourMin[0]) <= 23 and int(hourMin[1]) >= 0 and int(hourMin[1]) <= 59):
                return timeList
            else:
                print('Invalid time')
        except ValueError:
            print('Invalid input')

# Ask if the reminder is to be set for today. If not then ask for the date.
while (True):
    setReminderForToday = (input('Set reminder for today? Choose N to set other date. (Y/N): ')).lower()
    if (setReminderForToday in ['y', 'yes']):
        date = [dt.datetime.now().day, dt.datetime.now().month, dt.datetime.now().year]
        break
    elif (setReminderForToday in ['n', 'no']):
        date = setDate()
        break
    else:
        print('Invalid input')

time = setTime()

selectedTime = [date[2],
                date[1],
                date[0],
                time[0],
                time[1]]

# Here you can add your own tasks which will be executed after the selected time is reached.
def performTask():
    print('\nTime over !!')
    print(f'{dt.datetime.now()}')

print('\n--Do not close or stop the terminal--')
print(f'Reminder is set for {time[0]}:{time[1]} on {date[0]}-{date[1]}-{date[2]}.')

# This loop will run until the selected time is reached.
while(True):
    currentTime = [dt.datetime.now().year,
               dt.datetime.now().month,
               dt.datetime.now().day,
               dt.datetime.now().hour,
               dt.datetime.now().minute]
    if (currentTime >= selectedTime):
        performTask()
        toaster = ToastNotifier()
        toaster.show_toast('Reminder',
                           f'Time completed !!\n {dt.datetime.now().hour}:{dt.datetime.now().minute}',
                           duration=5)
        break
    else:
        t.sleep(1)
