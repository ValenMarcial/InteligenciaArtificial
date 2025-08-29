from deap import base, creator, tools, algorithms
import random
import math

COLOR_DADO = [111, 150, 25]

creator.create("FitnessMin", base.Fitness, weights=(-1.0,)) #creo una clase FitnessMax que hereda de la clase base.fitness
creator.create("Individual", list, fitness= creator.FitnessMin) #creo una clase individuo que tiene como atributo la fitness

toolbox = base.Toolbox() #creo una caja de herramientas
toolbox.register("atr_color", random.randint, 1, 255) #un atributo booleano con 0 o 1
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.atr_color, 3) #creo un individuo que es una lista de 3 atr_color
toolbox.register("population", tools.initRepeat, list, toolbox.individual) #creo una poblacion que es una lista de individuos

#Funcion de evaluacion, cuenta unos de cada individuo
def eval_maxones(individual):
  res = dist_euclidean(individual, COLOR_DADO)
  return res, 
toolbox.register("evaluate", eval_maxones)

def dist_euclidean(individual, color):
  list = [0, 0 ,0]
  suma = 0
  for i in range(len(individual)):
    suma = color[i] - individual[i]
    suma **= 2
    list[i] = suma
  suma = sum(list)
  return math.sqrt(suma)

#operadores geneticos
def cxProm(individual1, individual2):
  child1 = creator.Individual([(a + b) / 2 for a, b in zip(individual1, individual2)])
  child2 = creator.Individual([abs(a - b) for a, b in zip(individual1, individual2)])
  return child1, child2

def cxMate(individual1, individual2):
  list = [0,0,0]
  list1 = [0,0,0]
  for i in range(len(list)-1):
    if i % 2 == 0:
      list[i] = individual2[i] 
      list1[i]= individual1[i]
    else:
      list[i] = individual1[i] 
      list1[i]= individual2[i]
  child1 = creator.Individual(list)
  child2 = creator.Individual(list1)
  return child1, child2

#crea dos individuos nuevos tomando dos cosas de un lado y una de uno
def Picante(ind1, ind2):
  list = [ind1[0], ind2[1], ind2[2] ]
  list1 = [ind2[0], ind1[1], ind1[2] ]
  child1 = creator.Individual(list)
  child2 = creator.Individual(list1)
  return child1, child2
    

toolbox.register("mate", Picante)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3) # indpb probabilidad de mutacion, funcion que cambia bits dependiendo la proba
toolbox.register("select", tools.selTournament, tournsize=3) #funcion que selecciona 3 individuos

def main():
  random.seed(20)
  pop = toolbox.population(n=1000) #Tamaño 50 de la poblacion
  hof = tools.HallOfFame(1)

  # Estadísticas opcionales
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  stats.register("min", lambda fits: min(f[0] for f in fits))
  
  algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.5, ngen=100, stats=stats, halloffame=hof, verbose=True) #selección → cruce → mutación → evaluación, repetido ngen veces
  best_ind = tools.selBest(pop, k=1)[0] # k=1 => devuelve el mejor
  best_ind.reverse()
  print("Mejor individuo es:", best_ind)
  print("Fitness del mejor:", best_ind.fitness.values)
  
if __name__ == "__main__":
    main()