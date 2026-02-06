# LA#1: Convert years to seconds

# Get input from user
years = float(input("Enter number of years: "))

# Conversion
# 1 year = 365 days
# 1 day = 24 hours
# 1 hour = 60 minutes
# 1 minute = 60 seconds
seconds = years * 365 * 24 * 60 * 60

# Result
print(int(seconds))