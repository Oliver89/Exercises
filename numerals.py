# Exercise Script to translate between Roman Numerals and integers

# Possible values to check
possibles1 = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
possibles2 = list(range(0, 10))

theNums = []
num = ''

translationString = list(input('''Please input either an integer or a 
Roman numeral: '''))

for i in list(translationString):
	if i in possibles1:
		theNums = translationString
		theNums.append(0)
		#if len(theNums) < len(translationString):
		for index, item in enumerate(theNums):
			if item == 'I' and theNums[index + 1] == 'V':
				theNums[index] = 4
				theNums[index + 1] = 0
			if item == 'I' and theNums[index + 1] == 'X':
				theNums[index] = 9
				theNums[index + 1] = 0
			if item == 'X' and theNums[index + 1] == 'L':
				theNums[index] = 40
				theNums[index + 1] = 0
			if item == 'X' and theNums[index + 1] == 'C':
				theNums[index] = 90
				theNums[index + 1] = 0
			if item == 'C' and theNums[index + 1] == 'D':
				theNums[index] = 400
				theNums[index + 1] = 0
			if item == 'C' and theNums[index + 1] == 'M':
				theNums[index] = 900
				theNums[index + 1] = 0
		
	# Check the other values in the numeral

		for index, item in enumerate(theNums):
			if item == 'I':
				theNums[index] = 1
			if item == 'V':
				theNums[index] = 5
			if item == 'X':
				theNums[index] = 10
			if item == 'L':
				theNums[index] = 50
			if item == 'C':
				theNums[index] = 100
			if item == 'D':
				theNums[index] = 500
			if item == 'M':
				theNums[index] = 1000

	# Put it all together
	
		finalNum = sum(theNums)
		print('\nIn Arabic numbers, your numeral is ', str(finalNum))
		break
		
# If it doesn't contain numerals, it should contain integers!
	elif int(i) in possibles2:
		theInt = translationString
		if len(theInt) > 0:
			while len(theInt) < 4:
				theInt = '0' + theInt

	# Turn the input into integers
		
		a = int(theInt[0])
		b = int(theInt[1])
		c = int(theInt[2])
		d = int(theInt[3])
	
	# Rationalise the integer value into the numeral parts
		
		if a > 0:
			num = 'M' * a
		if b == 9:
			num += 'CM'
		if 8 >= b >= 5:
			num = num + 'D' + ((b - 5) * 'C')
		if b == 4:
			num += 'CD'
		if b <= 3:
			num = num + (b * 'C')
		if c == 9:
			num += 'XC'
		if 8 >= c >= 5:
			num = num + 'L' + ((c - 5) * 'X')
		if c == 4:
			num += 'XL'
		if c <= 3:
			num = num + (c * 'X')
		if d == 9:
			num += 'IX'
		if 8 >= d >= 5:
			num = num + 'V' + ((d - 5) * 'I')
		if d == 4:
			num += 'IV'
		if d <= 3:
			num = (d * 'I')
		
		print('\nIn Roman numerals, your number is ' + num)
		break
