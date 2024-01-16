print("thank you for choosing us..")
size=input("enter size of pizza in 's','m','l'? :")
add_pepperoni=input("do you want pepperono?'y' or 'n' :")
extra_cheese=input("do you want exte cheese ?'y' or 'n'")
bill=0
if size=="s":
    bill+=15
elif size == "m":
    bill+=20
else:
    bill +=25
if add_pepperoni=='y':
    if size=="s":
        bill+=2 
    else:
        bill+=3
if extra_cheese=="y":
    bill+=1
print(f"your final bill is: ${bill}.")           