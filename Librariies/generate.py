# I want to generate random information so generate.py

"""import random """# gives me access to all the functions in that random specific module 

"""coin = random.choice(["heads", "tails"])"""
"""print(coin)"""


# we can use keyword called as "from" to import more specific function than import 

"""  from random import choice """  # this will load function-choice into current namespace 
"""  coin = choice(["heads", "tails"])""" # now we dont need to specify choice function 
"""print(coin) """

#just to experiment I want to generate a random number betwn 1-10
""" import random

number = random.randint(1,10)
print(number)
 """

# Want to test random.shuffle(x) it shuffles them for eg. a deck of card


import random

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)


