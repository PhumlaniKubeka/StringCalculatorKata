import math
def add(numbers):

    if len(numbers) == 0:
            return 0
    elif len(numbers) == 1:
        return int(numbers)
    elif numbers[0] == '/':
	result = 0
	my_delim = ''
	line_split numbers.split('\n')
	length = len(line_split[0])
	for char in range(2,length):
		my_delim = my_delim+ line_split[0][char]
	my_num = line_split[1].split(my_delim)
	#my_delim = numbers[start_delim]
	# if numbers[(start_delim+1)] != '\\':
		#my_delim = my +numbers[start_delim]
		#start_delim += 1
	#my_num = numbers.split('\n')[1].split(my_delim)
	return more_numbers(my_num)


    else:
	    result
	    my_delim = ""
	if numbers[1] != ',':
		my_delim = "\n"
	my_num = numbers.split(my_delim)
	# for digit in my_num:
		# result += int(my_num)
	return more_numbers(my_num)

	def more_numbers(my_num):
		result = 0
		for digit in my_num:
			result += int(digit)
		return result
   