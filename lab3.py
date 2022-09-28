#Write a function to calculate factorial of a number using recursive function
def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)

num =8

#checking if the number is negative
if(num<0):
    print("Sorry, Factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of num",num,"is",recur_factorial(num))