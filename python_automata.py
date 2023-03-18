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
from typing import Set, Dict

class DFA:
    """Class to represent Deterministic finite automata"""
    def __init__(self, possible_states: Set, final_states: Set,
                 initial_state: int, sigma: Set, delta: Dict) -> None:
        self.possible_states = possible_states  # set of states
        self.final_states = final_states  # set of final states
        self.initial_state = initial_state  # initial state
        self.sigma = sigma  # set of symbols
        self.delta = delta  # transition function

    def run(self, word: str) -> bool:
        """
        first we start from the inital state
        for each letter in word we make the transistion and
        check if the state we end up on after the transitions is a final state or not
        :return: bool If the word is acceptable as per the language
        """
        assert all(w in self.sigma for w in word)
        i = 0
        curr_state = self.initial_state
        while i < len(word):
            curr_state = self.delta[(curr_state, word[i])]
            i += 1
        return curr_state in self.final_states


def main():
    """
    main method
    """
    dfa_1 = DFA(possible_states={0, 1, 2}, final_states={0, 1}, initial_state=0, sigma={"a", "b"},
                delta={(0, "a"): 0, (0, "b"): 1, (1, "a"): 2, (1, "b"): 1, (2, "a"): 2, (2, "b"): 2})
    words = ["aa", "ab", "aab", "aabb"]
    for word in words:
        print(f"Output for {word}: ", dfa_1.run(word))
if __name__=="__main__":
    main()
