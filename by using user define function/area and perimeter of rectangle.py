def area( length,breadth):
    a=(breadth)*(length)
    print("area of rectangle is:",a)

def perimeter(length,breadth):
    a=int(2*(length+breadth))
    print("perimeter of square is:",a)
        
b=int(input("enter the length of rectangle:"))
c=int(input("enter the breadth of rectangle:"))    
area(b,c) # function call for area of rectangle
perimeter(b,c)  # function call for perimeter of rectangle
