import sys

def say_hello():
    if sys.version.startswith('3.7'):
        raise Exception()
    return "hello"
