import re


class Tokenizer:
    TOKENS = [
        ("\\(", "list_start"),
        ("\\)", "list_end"),
        ("[a-zA-z+*:-]+", "symbol"),
        ("\\b[0-9]+\\b", "integer"),
    ]

    def __init__(self, code):
        self.code = code.strip()

    def run(self):
        tmp_code = self.code
        tokens = []

        while len(tmp_code):
            (token, match) = self.next_token_from_code(tmp_code)
            if match:
                tokens.append((token[1], tmp_code[:match.end()]))
                tmp_code = tmp_code[match.end():].strip()
            else:
                raise Exception("Unexpected Token: {}".format(tmp_code))

        return tokens

    def next_token_from_code(self, code):
        for token in self.TOKENS:
            match = re.match(re.compile(token[0]), code)
            if match:
                return (token, match)
        return (None, None)
