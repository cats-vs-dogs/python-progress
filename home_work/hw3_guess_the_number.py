from random import randint

a = 1
b = 10
machine_number = randint(a, b)

user_guess = int(input('Your guess for the number between {} and {} is: '.format(a, b)))

if user_guess == machine_number:
    print('Congratulations! You guessed the number! It is {} indeed!'.format(machine_number))
elif user_guess < machine_number:
    print('Your guess is less than my number. My number is {}. Try again!'.format(machine_number))
else:
    print('Your guess is greater than my number. My number is {}. Try again!'.format(machine_number))

