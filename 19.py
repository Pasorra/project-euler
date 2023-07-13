import datetime

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 12 + 1):
        date_string = f"01-{month}-{year}"
        date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
        day_of_week = date.strftime("%A").lower()
        if day_of_week == "sunday":
            sundays += 1

print(sundays)
