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
import random
from typing import List


class Individual:
    """Class to represent individual
    """
    def __init__(self, size: int = 5) -> None:
        self.size = size
        self.genes = [random.choice([0, 1]) for _ in range(self.size)]
        self.fitness = sum(self.genes)


class Population:
    """Class representing a collection of population
    """
    def __init__(self, size: int = 10) -> None:
        self.pop: List[Individual] = [Individual() for _ in range(size)]
        self.size = size
        self.fittest = None

    def get_fittest(self) -> int:
        """Method to get the fittest individual position from population
        """
        max_fit_score = float("-inf")
        fittest_idx = 0
        for position, individual in enumerate(self.pop):
            if individual.fitness > max_fit_score:
                fittest_idx = position
        self.fittest = self.pop[fittest_idx].fitness
        return self.pop[fittest_idx]

    def get_second_fittest(self) -> Individual:
        """Method to get the position of second fittest individual
        """
        second_idx = 0
        fit_score_first = fit_score_two = float("-inf")
        for position, individual in enumerate(self.pop):
            if individual.fitness > fit_score_first:
                _ = position
                fit_score_first = individual.fitness
            elif individual.fitness > fit_score_two:
                second_idx = position
                fit_score_two = individual.fitness
        return self.pop[second_idx]
    
    def min_fit_idx(self) -> int:
        """Method to get idx for individual with least fitness
        """
        idx = None
        min_score = float("inf")
        for position, individual in enumerate(self.pop):
            if min_score < individual.fitness:
                min_score = individual.fitness
                position = idx
        return position


class DemoGA:
    """Class to demonstrate sample Genetic algo
        Where size of chromosome if 5
        and fitness function is super simple count of 1's
    """
    def __init__(self, population: Population) -> None:
        self.population = population
        self.first_fittest: Individual = None
        self.second_fittest: Individual = None
        self.generation_count = 0
    
    def selection(self) -> None:
        """Method to get the fittest individual from population
        """
        self.fittest = self.population.get_fittest()
        self.second_fittest = self.population.get_second_fittest()

    def crossover(self) -> None:
        """Method to crossover between two individuals
        """
        crossover_point = random.randint(0, len(self.population[0].size))
        for i in range(crossover_point):
            self.first_fittest.genes[i], self.second_fittest.genes[i] = self.second_fittest.genes[i], self.first_fittest.genes[i]
        
    def run(self) -> None:
        pass

