from Square import square
""" def main():
    Test_Square() """


""" def Test_Square():
    if square(2) != 4:
        print(" 2 squared was not 4")
    if square(3) != 9:
        print("3 squared is not 9") """

# we have written more lines of code to test than main program 
# if we keep writing like this we need to write many lines of code to. This will become more lines for Test program than main program 
# to resolve such issue there is a keyword called "assert" 

# Assert is a keyword in python which is used to assert if something is true.To boldy claim that something is true 
# if it is not true that is if a boolean equation is false we will actually see some kind of error on screen 

""" def Test_Square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4 ")
    try:
        assert square(3) == 9  # thats if no if, no indented print. just need to assert simply these two things that want to be true 
    except AssertionError:
        print("3 squared was not  9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4 ")
    try:
        assert square(0) == 0  # need to check many test cases cause we have written some wrong code in main program 
    except AssertionError:
        print("0 squared was not 0 ")
 """
# we have written many lines of code just to test two lines of code in main Square .py program 

# pytest is a third party program that will automate the testing of our code. It adopts some conventions so that we dont need to write so many lines of code manually 
# unit tests are typically testing functions that we have written 

""" def test_Sqaure():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4 
    assert square(0) == 0 """

# to improve this design # what we can do is seprate numbers by negative, positive and zero or even odd or any other pattern
# this will make the pytest run all tests and not stop after one fails 

def test_positive():
    assert square(2) == 4 
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4 
    assert square(-3) == 9

def test_zero():
    assert(0) == 0
# good feature of pytest is even if one function fails it will test other function as well 

# after running pytest Test_Square.py it should show some errors as we have used + sign instead of * 
""" if __name__ == "__main__":
    main()
 """
 