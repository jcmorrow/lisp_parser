from expecter import expect
from src.parser import Parser


class TestParser():
    def test_ast_from_tokens(self):
        expect(Parser([("list_start", "("),
                       ("atom", "list"),
                       ("integer", "1"),
                       ("integer", "9"),
                       ("list_end", ")")
                       ]).run()[0]) == ["list", 1, 9]
