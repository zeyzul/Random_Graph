import random
import networkx as nx
from is_Graphical import is_Graphical


# Given a dictionary with vertices as keys and their degrees as values, return n vertices with the highest degrees
# Used in HH algorithm
def highest(a_sequence_dict, degree):  # n = degree
    vertices = list()
    sorted_dict = sorted(a_sequence_dict, key=a_sequence_dict.get, reverse=True)  # sorts vertices by their degrees
    for key in sorted_dict[:degree]:  # pick x keys from the sorted dict, where x is the degree of chosen j
        vertices.append(key)

    return vertices


def HavelHakimi(algorithm_sequence, filenames, n):
    algorithm_sequence_copy = algorithm_sequence.copy()

    # Check if the degree sequence is graphical, if not return 0 as a text file
    if not is_Graphical(algorithm_sequence_copy):
        f = open(filenames[1], "w+")
        f.write("0")
        f.close()
    else:
        # Create n vertices without any edges
        G_HH = nx.Graph()
        for i in range(n):
            G_HH.add_node(i + 1)

        # Create a dictionary with vertex labels as keys and assign them to the degrees in the sequence.
        # For the rest of my code, the degree of vertex i is found by sequence[i-1].
        # Or, sequence[j] is the degree of vertex j-1
        graph = dict()

        for i in range(n):
            graph[i + 1] = algorithm_sequence[i]

    while any(d > 0 for d in list(graph.values())):  # each iteration, check if all degrees are positive

        # Choose a random j from the vertex list with d_i > 0 from a list of possible choices
        possible_choices = [key for key, value in graph.items() if value >= 0]
        j = random.choice(possible_choices)

        # Remove j from the vertex list (dict keys)
        # Subtract 1 from the degree of d_j vertices with the highest degree
        # Add edges between j and each vertex from above step
        d_j = graph.pop(j, None)  # remove the vertex and store its degree
        highest_vertices = highest(graph, d_j)  # get d_j vertices with highest degree
        for vertex in highest_vertices:  # subtract 1 from each vertex
            graph[vertex] -= 1
            G_HH.add_edge(j, vertex)

    return G_HH






