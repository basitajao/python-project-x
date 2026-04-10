age = input('enter your age: ')

if int(age) >= 18:
    print('You are old enough to drive.')
elif int(age) < 18 and int (age) >=0:
    print(f'You need {18 - int(age)} more years to learn to drive.')
else:
    print('You are not old enough to drive.')


my_age = 25

your_age = input('enter your age: ')

if my_age > int(your_age):
    print(f'I am {my_age - int(your_age)} years older than you.')
elif my_age < int(your_age):
    print(f'You are {int(your_age) - my_age} years older than me.')
else:
    print('We are of the same age.')

