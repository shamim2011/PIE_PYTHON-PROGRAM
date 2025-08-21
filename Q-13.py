#### Q-13  / WAP to enter time in second and convert it in minutes and second

# Input time in seconds
time_in_seconds = int(input("Enter time in seconds: "))

# Convert to minutes and seconds
minutes = time_in_seconds // 60
seconds = time_in_seconds % 60

# Print the result
print(time_in_seconds, "seconds is equal to" ,minutes, "minutes and ",seconds, "seconds.")