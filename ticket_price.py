### Determine the ticket price based on age and whether the person is a student.

age = int(input("enter the age "))
student = input("are you a student :(yes/no)").lower()  # Convert to lowercase for consistency

if age<10:
    price = 10 
elif 10<age<16:
    price = 30 
elif 16<age<24:
    if student == 'yes':
        price = 30 
    else:
        price= 50 
else:
    price= 100 

print("your price is " , price)           

###
