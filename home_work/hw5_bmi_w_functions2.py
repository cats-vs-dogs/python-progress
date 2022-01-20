def get_user_data():
    user_data = {}
    while True:
        try:
            name = input('Your name is: ')
            assert len(name) >= 2
        except AssertionError:
            print('Your name must be at least 2 letters long! Please enter your name again!')
        else:
            break
    while True:
        try:
            weight = float(input('Your weight in kilograms is: '))
            assert 50 < weight < 250
        except AssertionError:
            print('Your weight must be in the range 50 to 250 kg! Please enter your weight again!')
        else:
            break    
    while True:
        try:
            height = float(input('Your height in meters is: '))
            assert 0.5 < height < 2.5
        except AssertionError:
            print('Your height must be in the range 0.5 - 2.5 m! Please enter your height again!')
        else:
            break  
    
    user_data['name'] = name
    user_data['weight'] = weight
    user_data['height'] = height
    return user_data

user_data = get_user_data()
print(user_data)

def calc_bmi(w, h):    
    bmi = w / (h**2)
    return bmi
    
n = user_data['name']
w = user_data['weight']
h = user_data['height']

bmi = calc_bmi(w, h)
print(f'{n}, your bmi is {round(bmi, 2)}')







