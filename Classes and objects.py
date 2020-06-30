

# How to create a class
class Snake:
    pass

snake = Snake()
print(snake)

################################################################################################################################################################################
# Attributes and methods in class
class Snake:
    name = 'Python'  # Attributes : set an attribute 'name' of the class

snake = Snake()
print(snake.name)


class Snake:
    name = 'Python'

    # Methods
    def change_name(self,new_name): # note the first argument is self
        self.name = new_name    # access the class attribute with the self keyword


# Instatiate the class
snake = Snake()

# print the current object name
print(snake.name)

# change the name using change_name method
snake.change_name('anaconda')
print(snake.name)

################################################################################################################################################################################
# Instance attributes in python and the init method
class Snake:
    def __init__(self, name):
        self.name = name
    def change_name(self,new_name):
        self.name = new_name

# two variables are instantiated
python = Snake('python')
anaconda = Snake('anaconda')

# print the names of the two variables
print(python.name)
print(anaconda.name)

################################################################################################################################################################################