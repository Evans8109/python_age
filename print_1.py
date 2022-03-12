driving = input('do you drive before: ')
if driving != 'yes' and 'no':
	print ('only enter yes/no')
	raise SystemExit
age = input('please enter your age: ')
age = int(age)
if driving == 'yes':
	if age < 18:
		print("it's impassible")
	else:
		print('pass')
elif driving == 'no':
	if age > 18:
		print('you can go to test')
	else:
		print('you can test after 18')
