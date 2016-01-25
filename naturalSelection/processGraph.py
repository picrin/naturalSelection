import json
import collections
#networkx is imported lazily so that pypy doesn't complain.

def loadGraph(fileObj, fromVar=None):
    """
    fileObj is a file representation of the population graph generated and written to disk by one of
    generatePopulation* functions from generateGraph module.
    Returns a simulation: a set of all sims represented as a networkx graph, and lists of uids of
    respectively first and last generation sims, to facilitate navigation of the graph.
    """
    import networkx
    simsGraph = networkx.DiGraph()
    if fileObj is not None:
        sims = json.load(fileObj)
    else:
        if fromVar is not None:
            sims = fromVar
    first = []
    last = []
    for sim in sims:
        sim["visitedBy"] = -1
        sim["descendants"] = 0 
        simsGraph.add_node(sim["uid"], sim)
        for parent in ["parentA", "parentB"]:
            if sim[parent] is not None:
                simsGraph.add_edge(sim[parent], sim["uid"])
        if sim["generation"] == "last":
            last.append(sim["uid"])
        if sim["generation"] == "first":
            first.append(sim["uid"])
    simulation = {"graph": simsGraph, "firstGeneration": first, "lastGeneration": last}
    return simulation

def countDescendants(simulation):
    def countDescendantsInner(nodeID, uid):
        node = simulation["graph"].node[nodeID]
        if node["visitedBy"] == uid:
            return
        else:
            node["descendants"] += 1
            node["visitedBy"] = uid
            if node["parentA"] is not None:
                countDescendantsInner(node["parentA"], uid)
            if node["parentB"] is not None:
                countDescendantsInner(node["parentB"], uid)
    for nodeID in simulation["lastGeneration"]:
        countDescendantsInner(nodeID, nodeID)

def MRCA(simulation):
    """
    Finds an ancestor of entire population, whose distance from all sims in the last generation is the smallest,
    with the distance between any two sims defined only when they are related, and is an integer equal to 
    the number of generations that separate them.
    
    For example, assume that A -> B means that A is a parent of B. Then if A -> B and B -> C we can say that the distance
    between A and A is 0, A and B is 1 and A and C is 2.
    """
    countDescendants(simulation)
    fifo = {}
    for i in simulation["lastGeneration"]:
        fifo[i] = True
    lastGenerationCount = len(simulation["lastGeneration"])
    generationNo = 0
    while len(fifo) != 0:
        newFifo = {}
        for key in fifo:
            exploreNode = simulation["graph"].node[key]
            if exploreNode["descendants"] == lastGenerationCount:
                return key, generationNo
            A = exploreNode["parentA"]
            B = exploreNode["parentB"]
            for parent in [A, B]:
                if parent is not None and parent not in newFifo:
                    newFifo[parent] = True
        fifo = newFifo
        generationNo += 1
    return None
