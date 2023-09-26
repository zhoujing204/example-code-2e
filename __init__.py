# Inside __init__.py

def greet():
    print("Hello! Welcome to the parent package.")

class MyClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)
