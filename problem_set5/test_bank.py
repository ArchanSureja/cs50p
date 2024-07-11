from bank import value

def test_hello():
    assert value("hello") == 0 

# starting from the h or H
def test2():
    assert value("Hii")==20
    assert value("hii")==20

# for other words
def test3():
    assert value("what's up")==100