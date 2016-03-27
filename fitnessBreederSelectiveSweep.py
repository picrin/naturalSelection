from naturalSelection import *
import time
import sys
initialSize = 100
generations = 700
count = 0

def SSDWFBS(size, generations):
    """
    stands for Selective Sweep Dominant Wanderer Fitness Breeder Simulation.
    """
    def firstGeneration():
       return simsFrame(populationSize = size, mutator = firstMutator)
    def nextGeneration(nextFrame):
       return nextFrame(migrator=wandererMigrator, breeder=slimAdvantageFitnessBreeder, mutator = dominantSingleAlleleMutator)
    return generatePopulationPure(generations, firstGeneration, nextGeneration)

def slimAdvantageFitnessBreeder(sims):
    return fitnessBreeder(sims, 1.05, len(sims))

def firstMutator(allSims):
    for sim in allSims:
        sim["genotype"]["isDominant"] = True
    dominantSingleAlleleMutator(allSims)
    sim["genotype"]["hasCopy1"] = True

def nullMutator(allSims): 
    pass


filename = "fitnessBreederResults/checkMRCASmall"
with open(filename, "w") as result:
    writePopulation(result, SSDWFBS(initialSize, generations))

with open(filename, "r") as result:
    simulation = loadGraph(result)
    print(quickMRCA(simulation, -1, 2**64))
