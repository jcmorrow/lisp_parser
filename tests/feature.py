from expecter import expect
from parser import parse


class TestFeature:
    def test_ast_from_code(self):
        expect(
            parse(code="(first (list 1 (+ 2 3) 9))")
        ) == ["first", ["list", 1, ["+", 2, 3], 9]]
