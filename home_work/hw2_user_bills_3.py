names = ['Maria', 'Ivan', 'Asen']
numbers = ['+39587111111', '+39587222222', '+39587333333']
bills = [20.5, 30.48, 5.98]

# keys = ['names', 'numbers']
# users = list(zip(names, numbers))
# dict_list_users = []
# for i in range(len(names)):
#     dict_list_users.append(dict(zip(keys, users[i])))
# print(dict_list_users)
# users_data = dict(enumerate(dict_list_users, 1))

users_data = {}
for i in range(len(names)):
    users_data[i+1] = {'name': names[i], 'number': numbers[i]}
print(users_data, '\n', '-'*140)

# adding a record:
users_data[len(users_data) + 1] = {'name': 'Joe', 'number': '+39587444444'}

print('|{}|{:5s}|{:12s}|'.format('id', 'name', 'number'))
for id, user in users_data.items():
    print('|{:2d}|{:5s}|{:12s}|'.format(id, list(user.values())[0], list(user.values())[1]))
print('-'*22)

users_bills = {}
for i in range (3):
    users_bills[i+1] = {'bill': bills[i]}

print('|{}|{:5s}|'.format('id', 'bill'))
for id, bill in users_bills.items():
    print('|{:2d}|{:5.2f}|'.format(id, list(bill.values())[0]))
print('-'*22)

max_bill = max(b['bill'] for b in users_bills.values())
for id, bill in users_bills.items():
    if list(bill.values())[0] == max_bill:
        print('The user with highest bill - {} is {}'.format(list(bill.values())[0], list(users_data[id].values())[0]))

min_bill = min(b['bill'] for b in users_bills.values())
for id, bill in users_bills.items():
    if list(bill.values())[0] == min_bill:
        print('The user with lowest bill - {} is {}'.format(list(bill.values())[0], list(users_data[id].values())[0]))

     