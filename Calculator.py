""" x = 1 
y=2
z= x + y

print(z) """

# this is program 2 to ask input from user 
#   from user test 
""" x = input("what's x ?")
y = input("what's y ?")

z= x  + y

print(z) """

# the above program gives output as string so to avoid that we need to take input as integer
""" 
x = input("what's x ?")
y = input("what's y ?")

z= int(x)  + int(y)

print(z) """

# To make improvements in above code we can do this as : This is called as nest function 

""" x = int(input("what's x ?"))
y = int(input("what's y ?"))

print(x+y) 
 """
# Nesting all things in one line :: but can make more mistakes in this complicated type

# print(int(input("what's x ?")) + int(input("what's y ?"))) 

# Float program : if a person types input in decimal rather than integer

""" x = float(input("what's x ?"))
y = float(input("what's y ?"))

print(x+y)  """

# round to user input for eg: 4.6 - 5

""" x = float(input("what's x ?"))
y = float(input("what's y ?"))

z = round(x+y)
print(z)  """

#  To give commas and to format string and to use syntax for this 

""" x = float(input("what's x ?"))
y = float(input("what's y ?"))

z = round(x+y)
print(f"{z:,}") """

# Dividing program

""" x = float(input("what's x ?"))
y = float(input("what's y ?"))

# z = x/y

z = round(x/y,2)

print(z) """

# If want to use format string 

x = float(input("what's x ?"))
y = float(input("what's y ?"))

z = x/y

# z = round(x/y,2)


