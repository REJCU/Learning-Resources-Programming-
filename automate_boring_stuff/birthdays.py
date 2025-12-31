birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + 'is birthday of'+ name)
    else:
        print("no info for "+name)
        bday = input("Birthday???")
        birthdays[name] = bday
        print('birthday database update')
