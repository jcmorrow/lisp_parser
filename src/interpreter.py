def add(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total


RUNTIME = {"+": add}


class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def run(self):
        values = []
        for expression in self.ast:
            if isinstance(expression, list):
                try:
                    values.append(RUNTIME[expression[0]](*expression[1:]))
                except KeyError:
                    raise Exception(
                        "Unknown method: {}".format(expression[0])
                    )
            else:
                values.append(expression)

        if values:
            return values.pop()
