from dataclasses import dataclass
from typing import Union


@dataclass
class Token:
    """Data class for token
    """
    type_: str
    value: Union[str, None]


class InterpreterCalc:
    """Interpreter for evaluating a single digit arithmetic operation
    """
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
        self.token: Token = None

    def error(self) -> None:
        """Error fn to raise exception
        """
        raise Exception("error parsing input")

    def get_next_token(self) -> Token:
        """Method responsible for tokenisation
        """
        if self.pos > len(self.text) - 1:
            return Token("EOF", None)
        curr_token = self.text[self.pos]
        if curr_token.isdigit():
            self.pos += 1
            return Token("INTEGER", int(curr_token))
        elif curr_token == "+":
            self.pos += 1
            return Token("PLUS", curr_token)

        # only handling plus and digit
        self.error()

    def eat(self, token_type) -> Token:
        """Method to get the current token if the type matches
        """
        if self.token.type_ == token_type:
            self.token = self.get_next_token()
        else:
            self.error()

    def expr(self) -> None:
        """Method to evaluate an expression like 3+5 left PLUS right
        """
        self.token = self.get_next_token()

        left = self.token
        self.eat("INTEGER")

        op = self.token
        self.eat("PLUS")

        right = self.token
        self.eat("INTEGER")

        return left.value + right.value

def main():
    """Main loop
    """
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = InterpreterCalc(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
