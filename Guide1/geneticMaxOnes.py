import random

POP_SIZE = 20 # Tamaño de la población
GENS = 30 # Número de generaciones
CXPB = 0.08  # Probabilidad de cruce
MUTPB = 0.05  # Probabilidad de mutación
GENOME_LENGHT = 20 # Longitud del genoma

# Fitness function
def fitness(individual):
  return sum(individual)

# Create a random individual
def create_individual():
  return [random.randint(0, 1) for _ in range(GENOME_LENGHT)]

# Create initial population
def create_population():
  return [create_individual() for _ in range(POP_SIZE)]

# Genetic Operation
def slection(population):
  # Selection for competition
  k = 3
  selected = []
  for _ in range(POP_SIZE):
    aspirants = random.sample(population, k)
    winner = max(aspirants, key=fitness)
    selected.append(winner)
  return selected

def crossover(parent1, parent2):
  # one point combination
  if random.random() < CXPB:
    point = random.randint(1, GENOME_LENGHT - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
  return parent1[:], parent2[:]

def mutate(individual):
  for i in range(GENOME_LENGHT):
    if random.random() < MUTPB:
      individual[i] = 1 - individual[i]  # Flip the bit
  return individual

#Main algoritm

def genetic_algorithm():
  population = create_population()
  for gen in range(GENS):
    #evaluate and show the best
    population.sort(key=fitness, reverse=True)
    print(f"GEN {gen}: BEST = {population[0]}, FITNESS = {fitness(population[0])}")
    
    #Selection
    selected = slection(population)
    
    #Reproduction
    next_gen = []
    for i in range(0, POP_SIZE, 2):
      offspring1, offspring2 = crossover(selected[i], selected[i+1])
      next_gen.append(mutate(offspring1))
      next_gen.append(mutate(offspring2))
    
    popilation = next_gen
  
  return max(population, key=fitness)

best = genetic_algorithm()
print(f"Best Individual found: {best}, Fitness: {fitness(best)}")
    
    