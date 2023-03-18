# langugage ? collection of vocab
# word ? sequence of symbols
# symbol ? element of alphabet sigma(finite set of alphabets)
# sigma = {a, b}
# L = {words that starts with a and ends with b}
# aa - Y
# ba - N
# epsilon - Y (nothing empty)

# DFA -> deterministic fintite automata
# fintite set of state where there is transition between states and has a q0 (start state) and then a final state

# sigma = {a, b}
# language = {enve no of a and even number of b or odd number of a and odd number of b}


class DFA:
    def __init__(self, Q, f, q0, sigma, delta) -> None:
        self.Q = Q  # set of states
        self.f = f  # set of final states
        self.q0 = q0  # initial state
        self.sigma = sigma  # set of symbols
        self.delta = delta  # transition function



def main():
    pass

if __name__=="__main__""
    main()
