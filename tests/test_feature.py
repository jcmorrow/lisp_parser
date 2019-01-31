from expecter import expect
from src.parser import parse


class TestFeature:
    def test_ast_from_code(self):
        expect(
            parse("(first (list 1 (+ 2 3) 9))")
        ) == [["first", ["list", 1, ["+", 2, 3], 9]]]
