# LA#1: Convert years to seconds

# Get input from user
years = int(input("Enter number of years: "))

# Time Conversion
# 1 year = 365 days
# 1 day = 24 hours
# 1 hour = 60 minutes
# 1 minute = 60 seconds

days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Result
print("Year: " + str(years))
print(str(days) + " days")
print(str(hours) + " hours")
print(str(minutes) + " minutes")
print(str(seconds) + " seconds")
