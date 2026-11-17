# Student Event Registration - Version 3

from datetime import datetime

print("Student Event Registration Summary")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

# String formatting
first_name = first_name.strip().title()
last_name = last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

full_name = first_name + " " + last_name

# Date formatting
event_date = datetime(year, month, day)
formatted_date = f"{event_date:%B} {event_date.day}, {event_date.year}"

# Display output
print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", formatted_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")