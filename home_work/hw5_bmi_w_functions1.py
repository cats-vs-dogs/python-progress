def get_user_data():
    user_data = {}
    name = input('Your name is: ')
    weight = float(input('Your weight in kilograms is: '))    
    height = float(input('Your height in meters is: '))
    user_data['name'] = name
    user_data['weight'] = weight
    user_data['height'] = height
    return user_data

def calc_bmi(w, h):    
    bmi = w / (h**2)
    return bmi

user_data = get_user_data()
n = user_data['name']
w = user_data['weight']
h = user_data['height']

bmi = calc_bmi(w, h)
print(f'{n}, your bmi is {round(bmi, 2)}')






