
class Groceries

"""
Objective: Check your understanding of dictionaries, objects and list comprehension.
Architecture: Your code will consist of one module.
class Groceries: Make a grocery list tracker. Begin by defining a class called Groceries. 
As part of the Groceries __init__() method, define an empty Python dictionary called 
grocery_list, which should be initialized as an empty dict.
"""
    def add_item(item):

"""
add_item is a function used to add an item to your grocery_list dict (as a key).
Every time an item is added to grocery_list, its value within the dict
should default to False, indicating that the item has not yet been purchased.
"""
        return item

    def remove_item(item):

"""
remove_item is a function which allows you to remove an item from your grocery_list dict.
"""
        return item

    def check_item(item):

"""
Function check_item changes the value of the key item in grocery_list to True,
indicating that the item has been purchased.
"""
        return item

    def items_remaining():

"""
items_remaining uses list comprehension to return the number of items
that have not yet been purchased.
"""
        return item


#Functions are Objects
if value == 'one':
    # do something
    function1()
elif value == 'two':
    # do something else
    function2()
elif value == 'three':
    # do something else
    function3()


def function1():
    print
    'You chose one.'


def function2():
    print
    'You chose two.'


def function3():
    print
    'You chose three.'
    #
    # switch is our dictionary of functions


switch = {
    'one': function1,
    'two': function2,
    'three': function3,
}
#
# choice can eithe be 'one', 'two', or 'three'
choice = input('Enter one, two, or three :')
#
# call one of the functions
try:
    result = switch[choice]
except KeyError:
    print('I didn\'t understand your choice.')
else:
    result()
    print(choice)