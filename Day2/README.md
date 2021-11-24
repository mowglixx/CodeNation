# Day 2
## variables and `format()`

> `Activity3.min.py` is not for this course, it is purely for experimentation

Today we covered the small topic of variables and how to store and manipulate data, namely 'strings', or in python3, `str()`.

## Variables
### Store data
```py
my_variable_name = "My Variable Value" # Store a string

my_number = 23 # Store an Interger

my_number_with_decimals = 69.420 # Store a Float Number

my_true_or_false = True # Store an Boolean

my_everything = None # Store a None value

```

### Built in Functions to data-types
**When you create a variable, you create a type of data that has built in functions depending on the data**

A 'String' data type has certain methods that you can can "**call**" with 'dot-notation', better represented as an example below
```py
# declare a string variable to have access to the '.format()' function/method, because it is a string, like all strings, it has access to 'format()'
my_string = "This is a string {}"

# use dot notation to use the 'format()' function
my_string.format(", Hi!")
#        ^Heres the dot
```