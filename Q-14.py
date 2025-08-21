#### Q-14  / WAP to enter days and convert it into months and days

# Input days
days = int(input("Enter the number of days: "))

# Convert to months and remaining days
months = days // 30
remaining_days = days % 30

# Print the result
print(days, "days is equal to ",months, "months and ",remaining_days, "days.")