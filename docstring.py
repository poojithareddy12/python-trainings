def func1():
    """ This is single line docstring  in triple quotes. """
    print("hello")

print(func1.__doc__)
print(type(func1.__doc__))


def func2():
    """
This is multiline docstring
Doc string should be immediate to function definition in triple quotes
    """
    print("hi")

print(func2.__doc__)
print(type(func2.__doc__))
