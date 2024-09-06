""" x =int(input("Add your number: "))
print(f"x is {x}") """

# the above code will crash if someone types charc type in input 
# to solve this we can use try and except keyword 

""" try:
    x =int(input("Add your number: "))
    print(f"x is {x}") 
except ValueError:
    print("x is not an integer, Please type integer value ")
 """

# the above code is running but do reduce some lines of code and make it more better we can do this 
""" 
try:
    x =int(input("Add your number: "))
except ValueError:
    print("x is not an integer, Please type integer value ")

print(f"x is {x}")   """

# If I try this to do minimum lines of code but it will give me Error as NameError 
# casue it will run the last line again and the x will not be defined 
# we can add else in this code like :

""" try:
    x =int(input("Add your number: "))
except ValueError:
    print("x is not an integer, Please type integer value ")
else:
    print(f"x is {x}")
 """
# But what if I want it to keep going in loop until the user types integer 
# we can do is this 
# using keyword while True and break keyword once we get our answer 


""" while True:
    try:
        x =int(input("Add your number: "))
    except ValueError:
        print("x is not an integer, Please type integer value ")
    else:
        break

print(f"x is {x}") """

# we can use function so we can use it many times or share if someone wants the same thing 
""" def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x =int(input("Add your number: "))
        except ValueError:
            print("x is not an integer, Please type integer value ")
        else:
            return x  #we created return cause we need to hand back a value from the function

main() """

# to make it more reusable we can do this as : 

def main():
    x = get_int("Whats x ? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x =int(input(prompt))
        except ValueError:
            print("x is not an integer, Please type integer value ")
        else:
            return x  #we created return cause we need to hand back a value from the function

main()