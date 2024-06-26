## Random Graph Generation
Generating random graphs using the Havel Hakimi algorithm, the Pairing Model and the Sequential algorithm based on [this paper](https://www.tandfonline.com/doi/abs/10.1080/15427951.2010.557277).

### Packages

Packages used for this project are included in the `requirements.txt` file. They can be downloaded by the following code:
```sh
   !pip install -r requirements.txt
   ```
### Inputs

Inputs can be generated by using the file `generating_input.py`. The required number of vertices and maximum degree allowed for a vertex must be manually changed. The python file generates a random list, and saves it as input if the list is [graphical](https://en.wikipedia.org/wiki/Graph_realization_problem). Otherwise, an error message is given and the file needs to be run again as needed.

### Generation and Algorithms

Implementation of each algorithm is in their respective file and is imported to `main.py` for usage. After running `main.py`, a user input must be given in the *`input-file-name output-file-name`* format. The last the two letters of the output file indicates which algorithm is to be used. For example, *`I-50-2.txt O-50-2-HH.txt`* generates a graph using the Havel Hakimi algorithm based on the input file *`I-50-2.txt`*. 

### Results

After each run, the duration of the algorithm is printed. By trying for different vertex and maximum degree numbers, their efficiency was compared. Pairing Model was always the slowest while Havel Hakimi was always the fastest. More importantly, even though Sequential algorithm was slower than the Havel Hakimi algorithm, the graphs generated by the Sequential Algorithm follow a probability distribution so they are more helpful for real-life modelling. Therefore, a little efficiency can be sacrificed for a network more resembling real-life distribution by choosing the Sequential Algorithm. 

### Visualization

A visualization is saved after each graph generation. The bigger degree number for a vertex is represented with a darker color and a bigger node. Graphs generated by the Havel Hakimi algorithm follow a red gradient, the ones generated by the Pairing Model follow a green gradient and the ones generated by the Sequential algorithm follow a purple gradient. Three example visualizations are included in this repository for the input *`I-50-2.txt`*.

| Havel Hakimi Algorithm | Pairing Model | Sequential Algorithm |
| ------------- | ------------- | ------------- |
| ![](https://github.com/zeyzul/Random_Graph/blob/master/fig_HH.png) | ![](https://github.com/zeyzul/Random_Graph/blob/master/fig_PM.png) | ![](https://github.com/zeyzul/Random_Graph/blob/master/fig_SA.png) |


