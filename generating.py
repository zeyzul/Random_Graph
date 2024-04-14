import random
from is_Graphical import is_Graphical

randomlist = list()
number_of_vertices = 70
max_degree = 25
for i in range(0, number_of_vertices):
    n = random.randint(1,max_degree)
    randomlist.append(n)

lst = randomlist.copy()
success = is_Graphical(randomlist)
if not success:
    print("Random list is not graphical. Try again.")
else:
    print("Successfully generated input.")
    file_name = "inputs/I-70-1.txt"
    # Output to txt file
    f = open(file_name, "w+")
    v = str(number_of_vertices)
    f.write(v)
    f.write('\n')
    f.write(' '.join([str(elem) for elem in lst]))
    f.write('\n')
    f.close()





