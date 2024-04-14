import networkx as nx  # using networkx package for graph data structure
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from havelhakimi import HavelHakimi
from sequential import Sequential
from pairingmodel import PairingModel

file_names = input()  # Reads input and output file names from the user in that order.
# Example input: I-50-2.txt O-50-2-HH.txt -> reads the values from the first txt file and
# writes the result into the second txt file. Second text file includes HH as keyword so it uses Havel-Hakimi algorithm.

file_names = list(file_names.split(" "))

# Read input from files to a list called lines. line[0] is the number of vertices and line[1] is the degree sequence
with open(file_names[0]) as f:
    lines = f.readlines()
    lines[0] = lines[0].replace('\n', '')  # remove the backspace character from the first line

n = int(lines[0])  # number of vertices
sequence = list(map(int, lines[1].split(' ')))  # degree sequence
f.close()

# a copy for writing the degree sequence into a txt file after algorithms. A copy is needed because the implementation
# of algorithms pops elements in each iteration, hence creating a null sequence at the end.
sequence_copy_2 = sequence.copy()

# calculating duration
start_time = timer()

if file_names[1][-6:-4] == "HH":
    Graph = HavelHakimi(sequence, file_names, n)
    colormap = plt.cm.Reds
elif file_names[1][-6:-4] == "SA":
    Graph = Sequential(sequence, file_names, n)
    colormap = plt.cm.Purples
elif file_names[1][-6:-4] == "PM":
    succeed = False
    try_count = 1
    while not succeed:
        try:
            Graph = PairingModel(sequence, file_names, n)
            succeed = True
            print("Took", try_count,  "tries.")
        except:
            print("An error occurred. Perfect matching couldn't be found. Starting again.")
            succeed = False
            try_count += 1
    colormap = plt.cm.Greens


end_time = timer()
print('Duration: {}'.format(end_time - start_time))

# Output to txt file
f = open(file_names[1], "w+")
n = str(n)
f.write(n)
f.write('\n')
sequence_copy_2 = ' '.join([str(elem) for elem in sequence_copy_2])
f.write(sequence_copy_2)
f.write('\n')
for vertx in Graph.nodes():
    neighbors = list()  # storing the neighbor vertices for each vertex in the graph and writing them to output file
    neighbors.append(vertx)
    for ne in Graph.neighbors(vertx):
        neighbors.append(ne)
    line = ' '.join([str(elem) for elem in neighbors])
    f.write(line)
    f.write('\n')
f.close()


draw_graph = True

if draw_graph:
    # Drawing the graph
    fig, ax = plt.subplots()
    fig = plt.figure(1, figsize=(1, 1), dpi=800)
    d = dict(Graph.degree)
    nx.draw(Graph, with_labels=False, font_weight='normal', font_size=5,
            node_color=range(int(file_names[0].split("-")[1])), node_size=[v * 5 for v in d.values()], width=0.3,
            cmap=colormap, edge_color='#C0C0C0')
    ax.set_facecolor("#ffffff")
    ax.axis('off')
    fig.set_facecolor('#ffffff')
    plt.savefig('fig_HH.pdf')





