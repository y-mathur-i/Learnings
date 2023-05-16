"""Module with a try for writing a genetic algorithm
    The idea is to have n no of children with basic features ?
    Then based on some evaluation criteria select few from them
    And introduce variations/mutations
    Until we find the generation that can actually succeed
    1. Initial pop
    2. Selection via Fitness function(2)
    4. Crossover
    5. Mutation

    Gene -> variable which are used to define an individual
    Chromosome -> Combination of those genes
    Fitness fn -> to generate the scrore for used for determining the proabiilty of selection
    Crossover -> crossover point (indx) and genes are interchanged 
                 between the parents (selected individuals)
    Mutuation -> random changes are introduced to allow diversity and prevent premature convergence
    Termination -> When better offsprings stop coming up
"""


class DemoGA:
    """Class to demonstrate sample Genetic algo
        Where size of chromosome if 5
        and fitness function is super simple count of 1's
    """



class Individual:
    """Class to represent individual
    """
    




