from StringCalculator import add

def test_empty_strings():
  assert add("") == 0

def test_add_two_strings():
  assert add("1,2") == 3

def test_add_unknown_strings():
    assert add("1,2,3,4") == 10

def test_handle_new_lines():
 	assert add('//;\n1,2,3')
	
def test_add_negative():
	assert add('-1,-2,-3')
	
def test_handle_mulitple_delimeters():
  assert add('//****\n1****2****3') == 6

def test_numbers_bigger_than_thousand():
  assert add('1002,3040,2339') 
