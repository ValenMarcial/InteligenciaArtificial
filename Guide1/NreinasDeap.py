from deap import base, creator, tools, algorithms
import random
CANT_REINAS = int(input("Cantidad de reinas:"))

creator.create("FitnessMin", base.Fitness, weights=(-1.0,)) #creo una clase FitnessMax que hereda de la clase base.fitness
creator.create("Individual", list, fitness= creator.FitnessMin) #creo una clase individuo que tiene como atributo la fitness

toolbox = base.Toolbox() #creo una caja de herramientas
def init_individual():
  individuo = list(range(CANT_REINAS * CANT_REINAS))
  random.shuffle(individuo)
  return creator.Individual(individuo)

toolbox.register("individual", init_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual) #creo una poblacion que es una lista de individuos

def fitness(individual):
  sum = 0
  for i in individual:
    row = i
    j = individual[i]
    if i != 0:
      if i!= CANT_REINAS:
        if j != 0:
          if j != CANT_REINAS:
            #puedo ver a los alrededores
            if individual[i-1] != -1:
              sum += 1
            if individual[i+1] != -1:
              sum += 1
            if individual[i] != -1:
            
  

toolbox.register("evaluate", fitness)


toolbox.register("mate", )
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