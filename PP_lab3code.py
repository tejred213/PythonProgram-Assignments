#Write a python program that accepts the length of three sides of a triangle as inputs. 
#The Program should indicate whether or not the triangle is a right angled triangle using function with exception handling

def tri(x,y,z):
    print(int(input("Enter the Length of side 1 :",x)))
    print(int(input("Enter the Length of side 2 :",y)))
    print(int(input("Enter the Length of side 3 :",z)))
    
def right_angled(x, y, z): 
    if (x*x+y*y==z*z) or (z*z+y*y==x*x) or (x*x+z*z==y*y) : 
        return "The triangle is Right-Angled" 
    else: 
        return "The triangle is not Right-Angled"

#Exception Handling

try:
    a=int(input("Enter length of side 1:"))
    b=int(input("Enter length of side 2:"))
    c=int(input("Enter length of side 3:"))
    if(c**2==a**2+b**2):
        print("The triangle is a right-angled triangle")
        else:
            print("The triangle is not a right-angled triangle")
 except TypeError:
    print("Unsupported operation")
 except ZeroSideError:
    print("One side is zero, thus the triangle does not exist")
    
