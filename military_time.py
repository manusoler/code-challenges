# Determine if the time you are given is AM or PM, then convert that value to the way that if would apper on a 24 hour clock
import re

if __name__ == "__main__":
    time = input()
    pattern = r"^([01]?[0-9]):([0-5][0-9]) (AM|PM)$"

    match = re.search(pattern, time)
    if match:
        hour = int(match.group(1))
        minutes = match.group(2)
        m = match.group(3)

        if m == "PM":
            hour = (hour + 12) % 24
        
        print("{:02d}:{}".format(hour, minutes))
    else:
        print("Incorrect time format, must be: HH:MM (AM|PM)")