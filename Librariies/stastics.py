# We will use stastics library here 
# this library does is do stastical functions like mean,median,mode 

# lets find average 

""" import statistics

print(statistics.mean([100,90])) """


# command line arguments 
# it provides arguments that is input to the program when we are executing at the command 
# lets use sys module 

"""import sys """ #provides functions and variables which are used to manipulate different parts of the Python Runtime Environment

"""print("Hello, my name is ",sys.argv[1]) """ # why index one ? cause python saves filename at sys.argv at index 0

# We might get Index error we dont type anything in index 1 so to avoid this we use condition 

"""import sys """

"""if len(sys.argv) < 2:""" # is the index has less than 2 names (1 is file name and second is user name ) it will show error
"""   print("Too few arguments")
elif len(sys.argv)> 2: """# if the index has more than 2 names than it will show message as too many arguments message.
"""   print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1])"""

# by using sys.exit - with the systems health its gonna exit the from then and there.

""" import sys
if len(sys.argv) < 2: 
    sys.exit("Too few arguments")
elif len(sys.argv)> 2: 
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1]) """

# If the user wants to add his full name waht he can do is write in this format " Name1 LastName "  
# we are using a for loop here to iterate over a list. the list in question here is sys.argv 
# it will update the variable for us as loop will keep going 
""" import sys
if len(sys.argv) < 2: 
    sys.exit("Too few arguments")
for arg in sys.argv:
    print("Hello, my name is", arg) """

# slice - to take a slice of a list means to take a subset of it. be it form the beginning or maybe from the middle or end 

import sys
if len(sys.argv) < 2: 
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:  # in square brackets [] specify the start and the end of the list that we want to retain
#  so this is gonna slice of the first index which is the file name and start with user names directly 
    print("Hello, my name is", arg)

