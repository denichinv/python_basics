day = input()
result = ""

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday"  or day == "Friday":
    result = "Working Day"
elif day == "Saturday" or day == "Sunday":
    result = "Weekend"
else:
    result = "Error"

print(result)