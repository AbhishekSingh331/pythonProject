# 1.) The " = " operator is used  to assign a value to a variable , Where as " == "
# operator is used to compare 2 values to see if they are equal. It returns True if the values
# are equal, and False otherwise.
x= 10
y=20
result=(x==y)
print(result)
# 2.)the ** operator is used for exponentiation, meaning it raises the left operand to the
# power of the right operand.
# 3.) the ^ operator is the bitwise XOR operator. It performs a bitwise exclusive OR operation
# between two integers, which means it sets each bit to 1 if exactly one of the corresponding
# bits in the two operands is 1.

#program==>1
num = 2
square = num ** 2
cube = num ** 3
print("square of num", square)
print ("cube of num" , cube)

#program==>2
number1=(input("Enter a number1"))
number2=(input("Enter a number2"))
if number1 > number2:
    print("number1 is greater")
elif number2 > number1:
    print("number2 is greater")
elif number1 == number2:
    print("Both are equal")


