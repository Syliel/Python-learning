#!/usr/bin/env python3

while True:
	print('What is spam?')
	spam = input()
	if spam == '1':
		print('Howdy!')
		continue
	elif spam == '2':
		print('Hello!')
		continue
	else:
		print('Who the heck are you?')
		break
