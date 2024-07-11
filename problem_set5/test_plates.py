from plates import is_valid 

def test_len():
    assert is_valid("A")==False
    assert is_valid("AAA")==True
    assert is_valid("ABWSBDA")==False

def test_fisr_digits():
    assert is_valid("11AA1")==False
    assert is_valid("AA11")==True

def test_symbol():
    assert is_valid("AA!1")==False
    
def test_sequence():
    assert is_valid("AA1W")==False
    assert is_valid("AA0")==False
