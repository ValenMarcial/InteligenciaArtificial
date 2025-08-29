from deap import base, creator, tools, algorithms
import random

creator.create("FitnessMax", base.Fitness, weights=(1.0,)) #creo una clase FitnessMax que hereda de la clase base.fitness
creator.create("Individual", list, fitness= creator.FitnessMax) #creo una clase individuo que tiene como atributo la fitness

toolbox = base.Toolbox() #creo una caja de herramientas
toolbox.register("atr_bool", random.randint, 0, 1) #un atributo booleano con 0 o 1
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.atr_bool, 20) #creo un individuo que es una lista de 20 atr_bool
toolbox.register("population", tools.initRepeat, list, toolbox.individual) #creo una poblacion que es una lista de individuos

#Funcion de evaluacion, cuenta unos de cada individuo
def eval_maxones(individual):
  return sum(individual),
toolbox.register("evaluate", eval_maxones)

#operadores geneticos
toolbox.register("mate", tools.cxTwoPoint) #Intercambia dos alelos
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05) # indpb probabilidad de mutacion, funcion que cambia bits dependiendo la proba
toolbox.register("select", tools.selTournament, tournsize=3) #funcion que selecciona 3 individuos


def main():
  random.seed(42)
  pop = toolbox.population(n=50) #Tamaño 50 de la poblacion
  hof = tools.HallOfFame(1)

  # Estadísticas opcionales
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  stats.register("max", lambda fits: max(f[0] for f in fits))
  
  algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=20, stats=stats, halloffame=hof, verbose=True) #selección → cruce → mutación → evaluación, repetido ngen veces
  best_ind = tools.selBest(pop, k=1)[0]  # k=1 => devuelve el mejor
  print("Mejor individuo es:", best_ind)
  print("Fitness del mejor:", best_ind.fitness.values)
  
if __name__ == "__main__":
    main()