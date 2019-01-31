from src.tokenizer import Tokenizer


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def run(self):
        tmp_tokens = self.tokens
        ast = []
        while tmp_tokens:
            next_token = tmp_tokens[0]
            tmp_tokens = tmp_tokens[1:]
            if next_token[0] == "list_start":
                (inner_list, tmp_tokens) = self.parse_inner_list(tmp_tokens)
                ast.append(inner_list)
            elif next_token[0] == "atom":
                ast.append(next_token[1])
            elif next_token[0] == "integer":
                ast.append(int(next_token[1]))
            elif next_token[0] == "operator":
                ast.append(next_token[1])

        return ast

    def parse_inner_list(self, tokens):
        parens = 0
        inner_list_contents = []
        while tokens:
            next_token = tokens[0]
            tokens = tokens[1:]
            if next_token[0] == "list_start":
                parens = parens + 1
            if next_token[0] == "list_end":
                if parens > 0:
                    parens = parens - 1
                else:
                    return (Parser(inner_list_contents).run(), tokens)
            inner_list_contents.append(next_token)
        raise Exception("Unterminated List")


def parse(code):
    return Parser(Tokenizer(code).run()).run()
