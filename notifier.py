import pync
import datetime as d
import google_sheet_to_sql
import time

pync.Notifier.NOTIFIER = "/opt/homebrew/bin/terminal-notifier"
today = d.date.today().strftime('%A')

# call function to load data from google sheet to sql db one time only
# google_sheet_to_sql.load_data_to_sql()   

# data = google_sheet_to_sql.get_data_from_sql()

notifier_activity = set()

system_time = d.datetime.now().strftime('%H:%M')
for index,row in data.iterrows():
    if row['Day'] == today:
        schedule_start_time = row['Time'].split('-')[0].strip().split(' ')[0]
        period = row['Time'].split('-')[0].strip().split(' ')[1]

        if period == 'PM' and schedule_start_time != 12:
            schedule_start_time = str(int(schedule_start_time) + 12)

        if period == 'AM' and schedule_start_time == 12:
            schedule_start_time = '00'    

        schedule_start_time = f'{schedule_start_time}:00'
        if  schedule_start_time == system_time and row['Activity'] not in notifier_activity:
            pync.Notifier.notify(row['Activity'],title = 'Study', sound = 'Sonar')
            notifier_activity.add(row['Activity'])


