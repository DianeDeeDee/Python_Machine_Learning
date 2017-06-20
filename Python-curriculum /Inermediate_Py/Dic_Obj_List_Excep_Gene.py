#import beginner_python_1 as bp1
print("--------------------Dictionaries")
"""
When to Use It: When describing what you want to do, 
if you use the word "map" (or "match"), chances are good you need a dictionary. 
Use whenever a mapping from a key to a value is required.
"""


state_capitals={
    'New York': 'Albany', #"New York" is a key and "Albany" is a value
    'New Jersey': 'Trenton', 'France': 'Paris', 'UK': 'London',
    'Canada': 'Ottawa'
    }
print("Items=",state_capitals.items())
#for key, value  in state_capitals.items():
NewYork_capital = 'Albany'
print("state_capitals=", state_capitals)
print("NewYork_capital=", NewYork_capital)
print("Other way to get NewYork_capital=" , state_capitals["New York"])
print("Keys of state_capitals=", state_capitals.keys())
#for value in state_capitals.values():
print("values of state_capitals=", state_capitals.values())
print("\n")
"""
If you're searching for a value in a dictionary and you use a for loop, 
you're doing it wrong. Use the below statement instead:
"""
valueNY = state_capitals['New York']
print("valueNY=", valueNY)
print("Other way to get the value of NY=", state_capitals.get('New York', None))

print("\n")
Copy_state_capitals=state_capitals.copy()
print("Cp state_capitals: Copy_state_capitals=", Copy_state_capitals)
#state_capitals.clear()
#print("Removing state_capitals:",state_capitals)
print("The the number of stored items:", len(state_capitals))
del state_capitals["New York"]
#print("Removing NY:", del state_capitals["New York"])
print("After removing NY, state_capitals=", state_capitals)

print("\n")
my_list = [1, 2, 3]
my_dictionary = dict.fromkeys(my_list, 0)
print("my_dictionary with with all values initialized to 0=", my_dictionary)

my_dictionary1 = {1: 1, 2: 2, 3: 3}
my_dictionary1 = dict.fromkeys(my_dictionary1, None)
new_dictionary1 = dict.fromkeys(my_dictionary1)
print("my_dictionary with all values automatically initialized to None=", my_dictionary1)

my_dictionary2 = {'hello': 1, 'goodbye': 2}
foo_value = my_dictionary2.pop('hello', None)
print("foo_value=", foo_value)
print("then my_dictionary2=", my_dictionary2)

print("\n")
"""
Pop (i.e. delete and return) a random element from the dictionary (d)
Returns a (key, value) tuple if d is not empty.
Raises KeyError if d is empty.
"""
try:
    key, value = state_capitals.popitem()
    print('Got the random element from state_capitals = {}: {}'.format(key, value))
except KeyError:
    print('Done')

"""
Count the number of times each word is seen in a file:

Question:
#words = {}
#for number in bp1:
 #   occurrences = words.setdefault(number, 0)
 #   words[number] = occurrences + 1
How do I import bp1 from another location?

The code is not working: for number in bp1:
TypeError: 'module' object is not iterable
"""

first = {'a': 1}
second = {'b': 2}
third = {'c': 3}
fourth = {'d': 4}
first.update(second)
first.update(fourth)
first.update(third)
print ("updated first=",first)
print("second=",second)

print( "Another way using keyargument for other:" )
first = {'a': 1}
first.update( b=2, d=4, c=3 )
print( "New first=",first )

print( "\n" )
print( "--------------------Objects" )

original_string = '    some text    '

# remove leading and trailing whitespace
#fonction strip, cette fonction supprime les espaces en début
# et en fin de chaîne.
string1 = original_string.strip()
print( "string1=", string1 )
# make uppercase
string2 = string1.upper()
print( "string2=", string2 )
# make lowercase
string2.lower() == string1
True

# create a dictionary the normal way
a_dict = {
    'key' : 'value',
    'key2' : 'value2'
    }
# use 'dict' to create one
list_of_tuples = [('key', 'value'),
                 ('key2', 'value2') ]
a_dict_2 = dict(list_of_tuples)
print ( "a_dict=", a_dict )
print ( "a_dict_2=", a_dict_2 )
#
print ( "Hola=", a_dict == a_dict_2)
True
"""
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

"""
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
choice = input( 'Enter one, two, or three :' )
#
# call one of the functions
try:
    result = switch[choice]
except KeyError:
    print( 'I didn\'t understand your choice.' )
else:
    result()
    print( "choice=",choice )


class OurClass(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
    def printargs(self):
        print( "self.arg1=", self.arg1 )
        print( "self.arg2=", self.arg2 )

instance = OurClass('arg1', 'arg2') #instance of OurClass
print( type(instance))
instance.printargs() #When we call instance.printargs() these original arguments are printed.
