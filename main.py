import numpy as np

# using the ofunu library for CEC 2017 benchmark test problems(https://opfunu.readthedocs.io)
import opfunu
function = opfunu.cec_based.F52017(ndim=30)

class LAB:
    def __init__(self, groups, individuals, dimensions, lower_bound, upper_bound, minimise):
        self.groups = groups
        self.individuals = individuals
        self.dimensions = dimensions
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.minimise = minimise

    # weights are required according to the number of individuals to be followed
    def weights(self, individuals_to_follow):
        w = np.random.random(individuals_to_follow)
        return np.sort(w / w.sum())[::-1]

    def fitness_function(self, generated_individuals):
        function_value = np.array([function.evaluate(individual) for individual in generated_individuals])
        return np.column_stack((generated_individuals, function_value))

    def intra_inter_sorting(self, population):
        sorted_population = [np.array(sorted(group, key=lambda x: x[-1], reverse=not self.minimise)) for group in population]
        # Sort the groups based on the first item's last element (fitness value) in ascending order
        return sorted(sorted_population, key=lambda set_group: set_group[0][-1])

    def generating_individuals(self):
        generated_individuals = np.random.uniform(self.lower_bound, self.upper_bound, (self.groups * self.individuals, self.dimensions))
        generated_individuals = self.fitness_function(generated_individuals)
        return self.intra_inter_sorting(np.array_split(generated_individuals, self.groups))

    # LAB algorithm formulations
    def update_search_direction(self, population):

        # updating the search direction for leaders
        # global_leader*weight1 + associated_advocate*weight2 + mean_associated_believers*weight3
        for l in range(self.groups):
            w = self.weights(3)
            population[l][0] = population[0][0]*w[0] + population[l][1]*w[1] + np.mean(population[l][2:], axis=0)*w[2]

        # updating the search direction for advocates
        # associated_leader*weight1 + mean_associated_believers*weight2
        for a in range(self.groups):
            w = self.weights(2)
            population[a][1] = population[a][0]*w[0] + np.mean(population[a][2:], axis=0)*w[1]

        # updating search direction for believers
        # associated_leader*weight1 + associated_advocate*weight2
        for g in range(self.groups):
            for b in range(self.individuals):
                w = self.weights(2)
                population[g][b] = population[g][0] * w[0] + population[g][1] * w[1]

        return population

    def run_iterations(self, num_iterations):
        self.population = self.generating_individuals()

        for iteration in range(num_iterations):
            # update follow direction of each individual using the update_follow_direction method
            self.population = np.array(self.population)
            self.population = self.update_search_direction(self.population)

            # calculate the fitness function for the updated individuals
            for g in range(self.groups):
                self.population[g] = self.fitness_function(self.population[g, :, :self.dimensions])

            # rank the individuals and establish global leader using the intra_inter_sorting method
            self.population = self.intra_inter_sorting(self.population)

            # viewing the global best individual at each iteration
            print(f"Iteration {iteration + 1}:{self.population[0][0]}")

if __name__ == "__main__":
    lab_instance = LAB(groups=3, individuals=5, dimensions=30, lower_bound=-100, upper_bound=100, minimise=True)
    lab_instance.run_iterations(num_iterations=10)
