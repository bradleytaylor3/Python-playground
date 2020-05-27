import time
import random
import statistics

GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

if NUM_RATS % 2 != 0:
    NUM_RATS += 1

def populate(num_rats, min_wt, max_wt, mode_wt):
    return [int(random.triangular(min_wt, max_wt, mode_wt))for i in range(num_rats)]

def fitness(population, goal):
    ave = statistics.mean(population)
    return ave / goal

def select(population, toRetain):
    sortedPopulation = sorted(population)
    toRetainBySex = toRetain//2
    membersPerSex = len(sortedPopulation)//2
    females = sortedPopulation[:membersPerSex]
    males = sortedPopulation[membersPerSex:]
    selectedFemales = females[-toRetainBySex:]
    selectedMales = males[-toRetainBySex:]
    return selectedMales, selectedFemales

def breed(males, females, litter_size):
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):
            child = random.randint(female,male)
            children.append(child)

    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    for index, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[index] = round(rat*random.uniform(mutate_min, mutate_max))

    return children

def main():
    generations = 0

    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print("initial population weights = {}".format(parents))
    poplFitness = fitness(parents, GOAL)
    print("initial population fitness = {}".format(poplFitness))
    print("number to retain = {}".format(NUM_RATS))

    aveWt = []

    while poplFitness < 1 and generations < GENERATION_LIMIT:
        selectedMales, selectedFemales = select(parents, NUM_RATS)
        children = breed(selectedMales, selectedFemales, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selectedMales + selectedFemales + children
        poplFitness = fitness(parents, GOAL)
        print("Generation {} fitness = {:.4f}".format(generations, poplFitness))

        aveWt.append(int(statistics.mean(parents)))
        generations += 1
    print("average weight per generation = {}".format(aveWt))
    print("\nnumber of generations = {}".format(generations))
    print("number of years = {}".format(int(generations / LITTERS_PER_YEAR)))

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds".format(duration))