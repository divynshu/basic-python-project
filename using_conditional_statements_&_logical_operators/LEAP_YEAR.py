#nomaral year have 365 days while leap year have 366,with an extra day..
year=int(input("enter any year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")

#This program can also be written in less lines by using logical operators.
#It just to know you about line by line process.