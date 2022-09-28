#Python program to print the reciprocal of even numbers using assert
try:
    num=int(input("Enter a number:"))
    assert num%2==0
except:
    print("not an even number!")
else:
    reciprocal=1/num
    print(reciprocal)

#Python program to show how to use assert keyword
#defining a function
def square_root(Number):
    assert (Number < 73), "Give a positive Integer"
    return Number**(1/2)

#Calling function and passing values
print(square_root(36))
print(square_root(-36))

import sys
try:
    num1=input("enter 1st number:")
    num2=input("enter 2nd number:")
    result = (int(num1) / int(num2))
except:
    print("error",sys.exc_info()[0],"occured")
print (result)


num0=10

try:
    num1=input("Enter 1st number :")
    num2=input("enter 2nd number :")
    result =(int(num1) * int(num2))/(num0 *int(num2))
except ValueError as ve:
    print(ve)
    exit()
except ZeroDivisonError as zde:
    print(zde)
    exit()
except TypeError as te:
    print(te)
    exit()
except:
    print("Unexpected Error!")
    exit()
    
#print (result)    

#Write a function which will print all even numbers in a range from 1 to 100
def even():
    
    for i in range(1,100):
     if i%2==0:
        print(f"Even Numbers are :",i)
even()  
