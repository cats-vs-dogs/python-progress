from random import randint

a = 1
b = 10
machine_number = randint(a, b)
number_of_tries = 5


# for loop:

for i in range (1, number_of_tries + 1):    
    if i < number_of_tries:
        user_guess = int(input('Your guess {} for the number between {} and {} is: '.format(i, a, b)))
        if user_guess == machine_number:
            print('Congratulations! You guessed the number! It is {} indeed!'.format(machine_number))
            break
        elif user_guess < machine_number:
            print('Your guess is less than my number. Try again!')
        else:
            print('Your guess is greater than my number. Try again!')
    else:
        user_guess = int(input('Your guess {} for the number between {} and {} is: '.format(i, a, b)))
        if user_guess == machine_number:
            print('Congratulations! You guessed th9e number! It is {} indeed!'.format(machine_number))
            break
        else:
            print('Sorry, you lost! My number was {}.'.format(machine_number))


# while loop:

# i = 1
# while i <= number_of_tries:
#     if i < number_of_tries:
#         user_guess = int(input('Your guess {} for the number between {} and {} is: '.format(i, a, b)))
#         if user_guess == machine_number:
#             print('Congratulations! You guessed the number! It is {} indeed!'.format(machine_number))
#             break
#         elif user_guess < machine_number:
#             print('Your guess is less than my number. Try again!')
#         else:
#             print('Your guess is greater than my number. Try again!')        
#     else:
#         user_guess = int(input('Your guess {} for the number between {} and {} is: '.format(i, a, b)))
#         if user_guess == machine_number:
#             print('Congratulations! You guessed th9e number! It is {} indeed!'.format(machine_number))
#             break
#         else:
#             print('Sorry, you lost! My number was {}.'.format(machine_number))       
#     i += 1