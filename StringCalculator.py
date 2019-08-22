import math
def add(numbers):

    if len(numbers) == 0:
            return 0
    elif len(numbers) == 1:
        return int(numbers)
    else: 
        my_result = 0
        my_delim = ','
        if numbers[1] != ',':
            my_delim = '\n'
        my_num = numbers.split(my_delim)
        for digit in my_num:
            my_result += int(digit)
        return my_result
   