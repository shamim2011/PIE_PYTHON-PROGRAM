#### Q-25  / WAP to input a number between 1 to 7 and print daynames

n=int(input("Enter a number:"))
if n==0:
    print("SUNDAY")
elif n==1:
    print("MONDAY")
elif n==2:
    print("TUESDAY")
elif n==3:
    print("WEDNESDAY")
elif n==4:
    print("THURSDAY")
elif n==5:
    print("FRIDAY")
elif n==6:
    print("SATURDAY")
else:
    print("NOT A WEEKDAY!!")