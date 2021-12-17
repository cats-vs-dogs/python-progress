name = ['Maria', 'Ivan', 'Asen']
number = ['+39587111111', '+39587222222', '+39587333333']
bills = [20.5, 30.48, 5.98]

users = list(zip(name, number))
users_data = dict(enumerate(users, 1))

# adding a record:
users_data[len(users_data) + 1] = ('Joe', '+39587444444')

print('|{}|{:5s}|{:12s}|'.format('id', 'name', 'number'))
for k, v in users_data.items():
    print('|{:2d}|{:5s}|{}|'.format(k, v[0], v[1]))
print('-'*22)

users_bills = dict(enumerate(bills, 1))
print('|{}|{:5s}|'.format('id', 'bill'))
for k, v in users_bills.items():
    print('|{:2d}|{:5.2f}|'.format(k, v))
print('-'*22)

for id, bill in users_bills.items():
    if bill == max(users_bills.values()):
        print('The user with highest bill - {} is {}'.format(bill, users_data[id][0]))

for id, bill in users_bills.items():
    if bill == min(users_bills.values()):
        print('The user with lowest bill - {} is {}'.format(bill, users_data[id][0]))   