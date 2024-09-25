##here is the following condition to be a leap year
'''Explanation:
Divisible by 4: A year is generally a leap year if it is divisible by 4.
Divisible by 100: However, if the year is divisible by 100, it is not a leap year.
Divisible by 400: If the year is divisible by 100, but also divisible by 400, it is a leap year.'''

year = int(input('enter the year '))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('its a leap year')
        else:
            print('not a leap year')
    else:
        print ('its a leap year')
else:
    print('its not a leap year')      