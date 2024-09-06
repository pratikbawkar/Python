""" for i in [0,1,2]:
    print("Meow") """

#  if we want to print million times we need to write many numbers
# so to avoid that we can write a function 

""" for i in range(3):
    print("Meow") """
    
# one intresting way is 

""" print("meow\n" * 3,end="") """

# ask user how many time does he want cat to meow 

while True:
    n = int(input("How many times do you want the cat to Meow ?"))
    if n > 0:
        break
    
for i in range(n):
    print("Meow")