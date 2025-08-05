# Written 25/05/2025

import datetime
#adding our date and time functions

start_date = datetime.datetime(year=2023, month=1, day=1)
#inputting first day of 2023

end_date = datetime.datetime(year=2023, month=12, day=31)
#inputting last day of 2023

days_in_2023 = (end_date - start_date).days + 1
#adding var for our print
#we need to add +1 to make sure the code takes the first day into account

print(days_in_2023)
#printing our var to get the total days in 2023
