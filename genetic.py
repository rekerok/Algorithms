import random


class Equation:
    def __init__(self, x1=0, x2=0, x3=0, x4=0, x5=0):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5

    def __str__(self):
        return (
            f"{{x1={self.x1}, x2={self.x2}, x3={self.x3}, x4={self.x4}, x5={self.x5}}}"
        )

    @staticmethod
    def generate_one(min_value, max_value):
        return Equation(
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
        )

    @staticmethod
    def generate_genome(min_value, max_value):
        return random.randint(min_value, max_value)

    @staticmethod
    def generate_population(size, min_value, max_value):
        return [Equation.generate_one(min_value, max_value) for _ in range(size)]


class EquationHandler:
    def __init__(self, powers, result):
        self.min_value = -100
        self.max_value = 100
        self.population_count = 10
        self.mutation_chance_for_offspring = 0.5
        self.powers = powers
        self.result = result

    def solution_error(self, equation):
        return abs(
            equation.x1 ** self.powers[0][0]
            * equation.x2 ** self.powers[0][1]
            * equation.x3 ** self.powers[0][2]
            * equation.x4 ** self.powers[0][3]
            * equation.x5 ** self.powers[0][4]
            + equation.x1 ** self.powers[1][0]
            * equation.x2 ** self.powers[1][1]
            * equation.x3 ** self.powers[1][2]
            * equation.x4 ** self.powers[1][3]
            * equation.x5 ** self.powers[1][4]
            + equation.x1 ** self.powers[2][0]
            * equation.x2 ** self.powers[2][1]
            * equation.x3 ** self.powers[2][2]
            * equation.x4 ** self.powers[2][3]
            * equation.x5 ** self.powers[2][4]
            + equation.x1 ** self.powers[3][0]
            * equation.x2 ** self.powers[3][1]
            * equation.x3 ** self.powers[3][2]
            * equation.x4 ** self.powers[3][3]
            * equation.x5 ** self.powers[3][4]
            + equation.x1 ** self.powers[4][0]
            * equation.x2 ** self.powers[4][1]
            * equation.x3 ** self.powers[4][2]
            * equation.x4 ** self.powers[4][3]
            * equation.x5 ** self.powers[4][4]
            - self.result
        )

    def fitness_function(self, equation):
        return 1 / (0.00000001 + abs(self.solution_error(equation)))

    def start(self):
        population = Equation.generate_population(
            self.population_count, self.min_value, self.max_value
        )
        best_solution_error = self.fitness_function(population[0])
        best_solution = population[0]
        iteration = 0
        while best_solution_error > 0.0001 and iteration < 1000:
            iteration += 1
            new_population = []
            for _ in range(self.population_count):
                parent1 = self.select_parent(population)
                parent2 = self.select_parent(population)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)

            population = new_population

            for equation in population:
                equation_error = self.solution_error(equation)
                equation_fitness = self.fitness_function(equation)
                if equation_fitness > best_solution_error:
                    best_solution_error = equation_fitness
                    best_solution = equation

        return best_solution

    def select_parent(self, population):
        fitness_sum = sum(self.fitness_function(equation) for equation in population)
        probability = [
            self.fitness_function(equation) / fitness_sum for equation in population
        ]
        return random.choices(population, weights=probability)[0]

    def crossover(self, parent1, parent2):
        child = Equation()
        for i in range(5):
            parent = random.choice([parent1, parent2])
            setattr(child, f"x{i + 1}", getattr(parent, f"x{i + 1}"))
        return child

    def mutate(self, equation):
        mutated_equation = Equation()
        for i in range(5):
            gene = getattr(equation, f"x{i + 1}")
            if random.random() < self.mutation_chance_for_offspring:
                gene = self.generate_genome(self.min_value, self.max_value)
            setattr(mutated_equation, f"x{i + 1}", gene)
        return mutated_equation


# Example usage:
powers = [
    [2, 1, 3, 2, 1],
    [1, 2, 2, 1, 3],
    [3, 1, 1, 2, 2],
    [1, 2, 1, 3, 1],
    [2, 1, 2, 1, 3],
]
result = 100

equation_handler = EquationHandler(powers, result)
best_solution = equation_handler.start()
print(best_solution)
