# We will make a 3 by 3 brick wall just like in Mario game 

""" def main():
    print_square(3)

def print_square(size):
    # for each row in square 

    for i in range(size):
    # for each brick in row 

        for j in range(size):
    # print brick 

            print("#",end="")
        print()

main() """

# By removing inner loop 

def main():
    print_square(3)

def print_square(size):
    # for each row in square 

    for i in range(size):
        print("#" * size) 
main()