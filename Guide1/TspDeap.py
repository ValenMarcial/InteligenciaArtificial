from deap import base, creator, tools, algorithms
import random
CANT_CIUDADES = int(input("Cantidad de ciudades:"))
cant_ciudades = CANT_CIUDADES
LIST = [[-1 for _ in range(cant_ciudades)] for _ in range(cant_ciudades)]
for i in range(cant_ciudades):
  for j in range(cant_ciudades):
    if i != j:
      if LIST[i][j] == -1:
        LIST[i][j] = int(input(f"Distancia entre ciudad {i+1} y ciudad {j+1}: "))
        LIST[j][i] = LIST[i][j]
    else:
      LIST[i][j] = 0
      LIST[j][i] = 0
      

print("Matriz de distancias:")
for row in LIST:
  print(row)


creator.create("FitnessMin", base.Fitness, weights=(-1.0,)) #creo una clase FitnessMax que hereda de la clase base.fitness
creator.create("Individual", list, fitness= creator.FitnessMin) #creo una clase individuo que tiene como atributo la fitness

toolbox = base.Toolbox() #creo una caja de herramientas
def init_individual():
  individuo = list(range(CANT_CIUDADES))
  random.shuffle(individuo)
  return creator.Individual(individuo)

toolbox.register("individual", init_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual) #creo una poblacion que es una lista de individuos

def fitness(individual):
  total_distance = 0
  for i in range(len(individual)):
    from_city = individual[i]
    to_city = individual[(i + 1) % len(individual)]  # Siguiente ciudad, volviendo al inicio
    total_distance += LIST[from_city][to_city]
  return total_distance,

toolbox.register("evaluate", fitness)

#con dos padres generamos dos hijos, cortamos un padre hasta cierto punto y el resto lo completamos con el otro padre
def crossover(p1, p2):
  n = len(p1)
  a, b = sorted(random.sample(range(n), 2))

  # Crear hijos vacíos como Individuals
  h1 = creator.Individual([None] * n)
  h2 = creator.Individual([None] * n)

  # Copiar segmento fijo
  h1[a:b+1] = p1[a:b+1]
  h2[a:b+1] = p2[a:b+1]

  def fill_child(hijo, otro_padre):
      pos = (b+1) % n
      for gene in otro_padre:
          if gene not in hijo:
              # Buscar próxima posición libre
              while hijo[pos] is not None:
                  pos = (pos+1) % n
              hijo[pos] = gene
              pos = (pos+1) % n
  
  # Rellenamos los huecos
  fill_child(h1, p2)
  fill_child(h2, p1)
  child1 = creator.Individual(h1)
  child2 = creator.Individual(h2)
  return child1, child2

toolbox.register("mate", crossover)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3) # indpb probabilidad de mutacion, funcion que cambia bits dependiendo la proba
toolbox.register("select", tools.selTournament, tournsize=3) #funcion que selecciona 3 individuos

def main():
  random.seed(20)
  pop = toolbox.population(n=50) #Tamaño 50 de la poblacion
  hof = tools.HallOfFame(1)

  # Estadísticas opcionales
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  stats.register("min", lambda fits: min(f[0] for f in fits))
  
  algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.5, ngen=100, stats=stats, halloffame=hof, verbose=True) #selección → cruce → mutación → evaluación, repetido ngen veces
  best_ind = tools.selBest(pop, k=1)[0] # k=1 => devuelve el mejor
  print("Mejor individuo es:", best_ind)
  print("Fitness del mejor:", best_ind.fitness.values)
  siis = [0,1,2,3]
  print("AAAAAAAA:",fitness(siis))
  
if __name__ == "__main__":
    main()