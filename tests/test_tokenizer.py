from expecter import expect
from src.parser import Tokenizer


class TestTokenizer:
    def test_with_one_token(self):
        expect(Tokenizer("(list 1 9)").run()) == [
            ("list_start", "("),
            ("symbol", "list"),
            ("integer", "1"),
            ("integer", "9"),
            ("list_end", ")"),
        ]

    def test_with_invalid_token(self):
        with expect.raises(Exception):
            Tokenizer("abc!").run()
