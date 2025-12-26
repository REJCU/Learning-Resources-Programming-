unit = input('Enter TB or GB for unit \n >').upper()

if unit == 'TB':
    discrepancy = 1000000000000 / 109951162776
elif unit == 'GB':
    discrepancy = 1000000000 / 1073741824

print('enter advertised capacity')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

real_capacity =  str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is' + real_capacity + ' ' + unit)


