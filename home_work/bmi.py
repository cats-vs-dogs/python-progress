w = float(input('Your weight in kilograms is: '))
h = float(input('Your height in meters is: '))

bmi = w / (h**2)

print('Your Body Mass Index is: ', round(bmi, 2))