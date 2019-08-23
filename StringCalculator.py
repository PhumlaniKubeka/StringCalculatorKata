import math
def add(numbers):

    if len(numbers) == 0:
            return 0
    elif len(numbers) == 1:
        return int(numbers)
    elif numbers[0] == '/':
	    my_delim = ""
	    line_split = numbers.split('\n')
	    lengths = len(line_split[0])
	    for char in range(2,lengths):
		    my_delim += line_split[0][char]
	    my_num = line_split[1].split(my_delim)
	    return more_numbers(my_num)


    else:
	    my_delim = ","
	    if numbers[1] != ",":
		    my_delim = "\n"
	    my_num = numbers.split(my_delim)
	    return more_numbers(my_num)

def more_numbers(numbers):
    result = 0
    for digit in str(numbers):
        try:
            result += int(digit)
        except ValueError:
            print(AssertionError)
    return result