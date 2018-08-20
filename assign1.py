import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson


def poissongraph(n, mu):
    z = np.zeros(n)   # n is number of nodes
    for i in range(n):
        z[i] = poisson.rvs(mu)    # mu is the expected value
    G = nx.expected_degree_graph(z)
    return G


def getGraph(type="given"):
    if type == "given":
        g = nx.read_edgelist("pagerank.txt")
    elif type == "erdos_renyi":
        g = nx.dense_gnm_random_graph(40, 200)
    elif type == "poisson":
        g = poissongraph(40, 5)

    return g


def showGraph(graph):
    nx.draw(graph, with_labels=1)
    plt.show()


def findMaxDensitySubgraph(g, dens):
    max_dens = dens
    max_dens_subg = nx.DiGraph()
    nodelist = list(g.nodes())
    for node in nodelist:
        g.remove_node(node)
        if len(g.nodes()) > 0:
            new_dens = len(g.edges())/len(g.nodes())
            if new_dens > max_dens:
                max_dens_subg = g
                max_dens = new_dens
    if not len(max_dens_subg.nodes()):
        return None, max_dens
    return max_dens_subg, max_dens


def atleastk():
    


def main():
    graph_type = "erdos_renyi"
    g = getGraph(graph_type)
    nx.write_edgelist(g, "temp_graph")
    showGraph(g)
    dens = len(g.edges())/len(g.nodes())
    print("Density of given graph is: ", dens)

    max_dens_subg, max_dens = findMaxDensitySubgraph(g, dens)
    print("Density of max-density-subgraph: ", max_dens)
    if max_dens_subg is not None:
        showGraph(max_dens_subg)
    else:
        g = nx.read_edgelist("temp_graph")
        showGraph(g)


if __name__ == '__main__':
    main()
