from minpkg import say_hello, say_goodbye

def test_say_hello():
    assert say_hello() == 'hello'

def test_say_goodbye():
    assert say_goodbye() == 'Goodbye!!'
