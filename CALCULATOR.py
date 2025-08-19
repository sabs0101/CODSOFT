print("A Simple Calculator\n".center(50))
a=int(input("Enter the first number: "))
print("\n")
b=int(input("Enter the second number:"))
print("\n")
c=input("Enter the arithmetic operation (+,-,*,/): ")
print("\n")
if c=="+":
    print("The Addition of the given two numbers is: ", a+b)
elif c=="-":
    print("The Subtraction of the given two numbers is: ", a-b)
elif c=="*":
    print("The Multiplication of the given two numbers is: ",a*b)
elif c=='/':
    print("The Division of the given two numbers is: ",a/b)
else:
    print("Please enter a valid operator")


