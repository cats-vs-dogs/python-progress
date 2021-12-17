name = ['Maria', 'Ivan', 'Asen']
number = ['+39587111111', '+39587222222', '+39587333333']
bills = [20.5, 30.48, 5.98]

users = [{name: number} for name, number in zip(name, number)]
users_data = dict(enumerate(users, 1))
print(users_data, '\n', '-'*86)

# adding a record:
users_data[len(users_data) + 1] = {'Joe': '+39587444444'}

print('|{}|{:5s}|{:12s}|'.format('id', 'name', 'number'))
for id, user in users_data.items():
    for k, v in user.items():
        print('|{:2d}|{:5s}|{}|'.format(id, k, v))
print('-'*22)

users_bills = dict(enumerate(bills, 1))
print('|{}|{:5s}|'.format('id', 'bill'))
for k, v in users_bills.items():
    print('|{:2d}|{:5.2f}|'.format(k, v))
print('-'*22)

for id, bill in users_bills.items():
    if bill == max(users_bills.values()):
        print('The user with highest bill - {} is {}'.format(bill, list(users_data[id].keys())[0]))

for id, bill in users_bills.items():
    if bill == min(users_bills.values()):
        print('The user with lowest bill - {} is {}'.format(bill, list(users_data[id].keys())[0]))