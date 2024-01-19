row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \nfirst digit for row and second for column:")

horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[horizontal -1][vertical -1] = "X"
print(horizontal)

print(f"{row1}\n{row2}\n{row3}")