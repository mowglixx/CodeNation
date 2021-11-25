#
#  Activity(1):
#
# Create a list of your favourite website (3 of them), and 
# then add another two once you’ve created the list. 
# Then remove the last website.
# 
rows =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# returns 9
print(rows[2][2])

# prints 1
print(rows[0][0])

rows ={
    "first_row": {'a': 1, 'b': 2, 'c': 3 },
    "second_row":{'d': 4, 'e': 5, 'f': 6 },
    "third_row": {'g': 7, 'h': 8, 'i': 9 }
    }

# returns 1
print(rows['first_row']['a'])
# returns 5
print(rows['second_row']['e'])
# returns 9
print(rows['third_row']['i'])



#
# Activity(2):
#
# Research on the following methods: remove(), reverse(), 
# sort(), count(), extend() (and many more). Create a 
# program to demonstrate the uses of each method, 
# some of these you may need more than one example. 
# (Pay attention: not all methods would permanently 
# updates/make changes to the lists themselves.)