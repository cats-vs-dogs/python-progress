w = float(input('Your weight in kilograms is: '))
h = float(input('Your height in meters is: '))

bmi = w / (h**2)

if bmi <= 18.5:
    category = 'Underweight'
elif 18.5 < bmi < 24.9:
    category = 'Normal'
elif 25 < bmi < 29.9:
    category = 'Overweight' 
else:
    category = 'Obesity'

print('Your BMI Category is {}.'.format(category))


