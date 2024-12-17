from function.static_method import MathOperations

# show how to call a static method,
# both from the class and from an instance of the class
def test_static_method():
    assert MathOperations.add(3, 5) == 8
    math_operator = MathOperations()
    assert math_operator.add(3, 5) == 8
    