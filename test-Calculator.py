from StringCalculator import add

def test_empty_strings():
  assert add("") == 0

def test_add_two_strings():
  assert add("1,2") == 3

def test_add_unknown_strings():
    assert add("1,2,3,4") == 10

def test_add_handle_new_lines():
    assert add('1\n2,3') == 6