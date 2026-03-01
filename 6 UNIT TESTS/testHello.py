from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():
    assert hello("Alvin") == "Hello, Alvin" # will this work 
    # NO because it is not returning a value it is just printing
    # also 
    for name in ['Hermione','Harry','Ron']:
        assert hello(name) == f"Hello, {name}"
