from datetime import datetime


def my_function():
    now = datetime.now()
    print(f'{my_function.__name__}_{now.strftime("%Y-%m-%d_%H:%M:%S")}')
    pass


class MyClass(object):
    def method(self):
        pass


my_function()
print(my_function.__name__)  # gives "my_function"
print(MyClass.method.__name__)  # gives "method"

print(my_function.__qualname__)  # gives "my_function"
print(MyClass.method.__qualname__)
