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

    def cacl_fitness(self) -> int:
        """Method to calc the fitness of the individual
           represeneted via the no of 1s in genes
        """
        self.fitness = sum(self.genes)
        return self.fitness


class Population:
    """Class representing a collection of population
    """

    def __init__(self, size: int = 10) -> None:
        self.pop: List[Individual] = [Individual() for _ in range(size)]
        self.size = size
        self.fittest = 0

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

    def get_least_fit_idx(self) -> int:
        """Method to get idx for individual with least fitness
        """
        idx = None
        min_score = float("inf")
        for position, individual in enumerate(self.pop):
            if min_score > individual.fitness:
                min_score = individual.fitness
                idx = position
        return idx

    def reset_population(self, pop_size: int = 10) -> None:
        """Method to reset the population
        """
        self.pop = [Individual() for _ in range(pop_size)]
        self.size = pop_size
        self.fittest = None

    def calc_fitness(self) -> None:
        """Method to recalculate the fitness of all the individuals
        """
        for ind in self.pop:
            ind.cacl_fitness()
        self.get_fittest()


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
        self.first_fittest = self.population.get_fittest()
        self.second_fittest = self.population.get_second_fittest()

    def crossover(self) -> None:
        """Method to crossover between two individuals
        """
        crossover_point = random.randint(0, self.population.pop[0].size-1)
        for i in range(crossover_point):
            self.first_fittest.genes[i], self.second_fittest.genes[i] = self.second_fittest.genes[i], self.first_fittest.genes[i]

    def mutation(self) -> None:
        """Method to introduce mutation to genes
           by making change to genes for fittest and second fittest at random point
        """
        mutation_point = random.randint(0, self.population.pop[0].size-1)
        self.first_fittest.genes[mutation_point] = 1 if not self.first_fittest.genes[mutation_point] else 0
        mutation_point = random.randint(0, self.population.pop[0].size-1)
        self.second_fittest.genes[mutation_point] = 1 if not self.second_fittest.genes[mutation_point] else 0

    def get_fittest_offspring(self) -> Individual:
        """Method to get the fittest of the the fit offsprings
        """
        return self.first_fittest if self.first_fittest.fitness > self.second_fittest.fitness else self.second_fittest

    def add_fittest_offspring(self) -> None:
        """Remove the least fit offspring and 
        """
        self.first_fittest.cacl_fitness()
        self.second_fittest.cacl_fitness()
        least_fit_index = self.population.get_least_fit_idx()
        self.population.pop[least_fit_index] = self.get_fittest_offspring()


def main(population_size: int = 10) -> None:
    """Main method
    """
    population = Population(population_size)
    demo_ga = DemoGA(population=population)
    while demo_ga.population.fittest < 5:
        print("*"*10 + f" Processing generation {demo_ga.generation_count}" + "*"*10)
        demo_ga.generation_count += 1
        demo_ga.selection()
        demo_ga.crossover()

        if (random.randint(1, 10) == 7):
            demo_ga.mutation()

        demo_ga.add_fittest_offspring()

        demo_ga.population.calc_fitness()
        print(f"Fitness scores for all the individuals after generatio {demo_ga.generation_count} is")
        for ind in demo_ga.population.pop:
            print(ind.fitness, end=" ")
        print()


    print("Fitness scores for all the individuals is")
    for ind in demo_ga.population.pop:
        print(ind.fitness)


if __name__ == "__main__":
    main()
