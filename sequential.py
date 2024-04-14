import networkx as nx
import random
from is_Graphical import is_Graphical


def candidates_SA(dict_seq, vertex, G_alg):

    values = list()

    for v in dict_seq:
        if vertex == v:  # check for v != vertex (= chosen i)
            continue
        else:
            if G_alg.has_edge(vertex, v):  # check for {i,j} being in edge set
                continue
            else:
                dict_copy = dict_seq.copy()
                # check if the degree sequence with 1 subtracted from the degrees of i and j is graphical
                dict_copy[v] -= 1  # vertices have labels 1..n while indices in list start from 0. hence the -1
                dict_copy[vertex] -= 1
                degrees = list(dict_copy.values())
                if is_Graphical(degrees):
                    values.append(v)

    return values


def Sequential(algorithm_sequence, filenames, n):
    algorithm_sequence_copy = algorithm_sequence.copy()

    # Check if the degree sequence is graphical, if not return 0 as a text file
    if not is_Graphical(algorithm_sequence_copy):
        f = open(filenames[1], "w+")
        f.write("0")
        f.close()
    else:
        # Create n vertices without any edges
        G_SA = nx.Graph()
        for i in range(n):
            G_SA.add_node(i + 1)

        # Create a dictionary with vertex labels as keys and assign them to the degrees in the sequence.
        # For the rest of my code, the degree of vertex i is found by sequence[i-1].
        # Or, sequence[j] is the degree of vertex j-1
        graph = dict()

        for i in range(n):
            graph[i + 1] = algorithm_sequence[i]

    # The empty list E in the algorithm is G with no edges in my code. I'll add the corresponding edges to G
    sorted_dict = {k: graph[k] for k in sorted(graph, key=graph.get)}

    while len(sorted_dict) != 0:  # terminate if d = 0
        # choose the least i with di a minimal positive entry
        sorted_dict = {k: sorted_dict[k] for k in sorted(sorted_dict, key=sorted_dict.get)}
        # sorts dictionary(vertices) in increasing order with respect to their degrees
        i = next(iter(sorted_dict))  # getting the first vertex of dictionary, i.e. i with minimal positive degree

        while sorted_dict[i] != 0:
            J_l = candidates_SA(sorted_dict, i, G_SA)
            probs = [graph[x] for x in J_l]  # degrees of vertices in J
            j = random.choices(J_l, weights=probs, k=1)[0]
            sorted_dict[i] += -1
            sorted_dict[j] += -1
            G_SA.add_edge(j, i)

        sorted_dict.pop(i)

    return G_SA



