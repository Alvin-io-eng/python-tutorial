from calculator import main, square

# def main():
#     test_square()

# def test_square():
#     # if square(2) != 4:
#     #     print("2 squared was not 4")
#     # if square(3) != 9:
#     #     print("3 squared was not 9")
#     # OR - using assert keyword
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")

# # though it would be better to write lesser code for testing our code'
# # so lets create tools to do so, write less code for testing

# if __name__ == "__main__":
#     main()

# Using PYTEST
# now when you run the above code use pytest test_calculator.py instead of python3 test_calculator.py

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# this is so that even if one function fails the other functions will still be attempted

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# Raising for type error
import pytest

def test_str():
    with pytest.raises(TypeError):
        square("CAT")
    
