# Python Notebook Simulator

The **Python Notebook Simulator** is a project designed to help learn how deterministic and reproducible execution works in Python-like notebook environments.

By organizing Python code into well-defined cells using familiar Python comments (e.g., ##cellid and ##), it enables clear and structured execution. The simulator examines the dependencies between these cells to establish a fixed order in which they should be executed, ensuring that every run of the script yields the same results under identical conditions — this is the essence of deterministic execution.

Furthermore, the simulator enhances learning by visualizing the dependencies among code cells. This visualization shows how each cell is interconnected, providing insights into the flow of data and the impact of each section of code on subsequent computations. After execution, the simulator generates an HTML file that captures both the output and the visual graphs of cell relationships. 

# How Does It Work?

Simply mark each cell in your Python file between ##cell and ## comments. It analyzes dependencies and execute your cells in the right order. Dependency and execution graphs are automatically created. Get your results in an HTML file, including both your output and the graphs.

# Additional Details

### Marking Cells:
You start by structuring your Python script into segments or "cells," each marked by ##cell at the beginning and ending with ##. These markers help the simulator identify discrete blocks of code that need to be analyzed and executed.

### Dependency Analysis:
Once the cells are marked, the simulator analyzes the code within each cell to detect dependencies. Dependencies occur when a cell uses data or variables defined in another cell. For instance, if Cell B calculates averages based on data processed in Cell A, Cell B depends on Cell A.

### Determining the Execution Order:
Based on the identified dependencies, the simulator constructs a directed acyclic graph (DAG). Each node in this graph represents a cell, and directed edges represent dependencies—pointing from prerequisite cells to dependent cells.
The simulator then performs a topological sort on this DAG to determine a linear order for cell execution. This sort ensures that any given cell is executed only after all its dependencies have been processed, thus maintaining the integrity and correctness of the data throughout the execution process.

### Execution and Visualization:
With the order determined, the simulator executes the cells sequentially. As it processes each cell, it also dynamically generates graphs that visually map out the dependencies and execution paths. 

### Output in HTML Format:
After executing all cells, the simulator compiles the outputs and the dependency/execution graphs into an HTML file. This file not only presents the results of the computations but also includes the visual graphs, offering an overview of the entire execution process.


## Getting Started

### Clone the Repository

To get started with the Python Notebook Simulator, you'll first need to clone the repository to your local machine. You can do this by opening your terminal or command prompt and running the following command:

```bash
git clone https://github.com/vrtnis/python-notebook-simulator.git
cd python-notebook-simulator
```


### Install Dependencies 

```
pip install -r requirements.txt
```

### Run It!

```
python main.py -i ./examples/testinput.py
```
