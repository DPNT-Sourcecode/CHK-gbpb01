from solutions.HLO import hello_solution
"""
Tests the hello function in order to see if the implementation
is working
"""

class TestHello():
    def test_hello(self):
        assert hello_solution.hello('Mihail') == 'Hello, Mihail!'