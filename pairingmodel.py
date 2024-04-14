import networkx as nx
import random
from is_Graphical import is_Graphical

# eliminates loops and parallel edges as choices. Used in pairing model.
def candidates_PM(vertex1, vertices, G_alg):
    possible_vertices = list()

    for groups in vertices:  # iterate over the vertex groups created
        if vertex1 in groups:  # skip the group where vertex1 is in
            continue
        else:
            for element in groups:
                try:  # if vertex1 is already matched to another vertex, if it has a neighbor, continue
                    next(G_alg.neighbors(element))
                except:
                    # Check if the any vertices in the groups of vertex 1 and element are matched
                    for g in vertices:
                        if vertex1 in g:
                            list1 = g
                        elif element in g:
                            list2 = g

                    matched = False
                    for u in list1:
                        for v in list2:
                            if G_alg.has_edge(u, v):
                                matched = True

                    if not matched:
                        possible_vertices.append(element)
                else:
                    continue

    return possible_vertices


# takes a perfect matching graph with n * sum(sequences) vertices, returns a graph with n vertices with
# corresponding edges
def final_graph(matching_graph, vertices, n):
    # create a dictionary where keys are vertex numbers and values are their groups
    group_number = 1
    vertex_dict = {}
    for group3 in vertices:
        for element3 in group3:
            vertex_dict[element3] = group_number
        group_number += 1

    G2 = nx.Graph()  # create the final graph where groups are shrank into one vertex
    for i in range(n):
        G2.add_node(i + 1)

    for edge in list(matching_graph.edges()):
        u, v = edge
        vertex_u = vertex_dict[u]
        vertex_v = vertex_dict[v]

        G2.add_edge(vertex_u, vertex_v)

    return G2


def PairingModel(algorithm_sequence, filenames, n):
    algorithm_sequence_copy = algorithm_sequence.copy()

    # Check if the degree sequence is graphical, if not return 0 as a text file
    if not is_Graphical(algorithm_sequence_copy):
        f = open(filenames[1], "w+")
        f.write("0")
        f.close()
    else:
        # Create n groups, where each one has d_i vertices, add the vertices to the graph
        G_PM = nx.Graph()

        # The list vertices has lists as elements, where each list has d_i elements.
        # For example for degree sequence (2,1) the list vertices would be [[1,2], [3]]
        vertices = list()
        count = 1
        for i in range(n):
            group = list()
            for j in range(algorithm_sequence[i]):
                group.append(count)
                G_PM.add_node(count)
                count += 1

            vertices.append(group)

        # Start with the first vertex and create a candidates list. Pick the first vertex in the candidates list and add
        # an edge between the vertices.
        for v in range(sum(algorithm_sequence)):  # iterate over every vertex
            try:  # if v is is not matched to another vertex, below code will given an error. So handle that with
                # try-except. If there is no error, v has an edge so continue
                next(G_PM.neighbors(v + 1))
            except:
                choices = candidates_PM(v + 1, vertices, G_PM)
                v2 = random.choice(choices)
                G_PM.add_edge(v + 1, v2)
            else:
                continue

    G_final = final_graph(G_PM, vertices, n)

    return G_final