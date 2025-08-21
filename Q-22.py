#### Q-22  / WAP to print the largest number among three number

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

if a>b:
    if a>c:
        print(a," is the largest among ",a,",",b,"&",c)
    else:
        print(c," is the largest among ",a,",",b,"&",c)
else:
    if b>c:
        print(b,"is the largest among ",a,",",b,"&",c)
    else:
        print(c,"is the largest among ",a,",",b,"&",c)
