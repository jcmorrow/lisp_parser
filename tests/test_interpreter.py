from expecter import expect

from src.interpreter import Interpreter


class TestInterpreter:
    def test_addition_statement(self):
        expect(Interpreter([["+", 1, 2, 3]]).run()) == 6

    def test_value(self):
        expect(Interpreter([1, 2]).run()) == 2
