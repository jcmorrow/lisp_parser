from expecter import expect
from src.parser import Parser


class TestParser():
    def test_ast_from_tokens(self):
        expect(Parser([("list_start", "("),
                       ("symbol", "list"),
                       ("integer", "1"),
                       ("integer", "9"),
                       ("list_end", ")"),
                       ]).run()[0]) == ["list", 1, 9]

    def test_broken_ast_from_tokens(self):
        with expect.raises(Exception):
            Parser(
                [("list_start", "("), ("list_end", ")"), ("list_end", ")")]
            ).run()
