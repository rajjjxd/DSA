#CREATING A SIMPLE CALC

number1= int(input('enter the first number'))
number2= int(input('enter the second number'))
operator= input('enter the operator:+,-,*,%')

if operator == '+':
    print(number1 +  number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '%':
    print(number1 % number2)   
else:
    print("Invalid operator!")             

