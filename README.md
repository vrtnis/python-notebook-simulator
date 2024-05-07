# Python Notebook Simulator

The **Python Notebook Simulator** is a project designed to help learn how deterministic and reproducible execution works in Python-like notebook environments.

By organizing Python code into well-defined cells using familiar Python comments (e.g., ##cellid and ##), it enables clear and structured execution. The simulator examines the dependencies between these cells to establish a fixed order in which they should be executed, ensuring that every run of the script yields the same results under identical conditions — this is the essence of deterministic execution.

Furthermore, the simulator enhances learning by visualizing the dependencies among code cells. This visualization shows how each cell is interconnected, providing insights into the flow of data and the impact of each section of code on subsequent computations. After execution, the simulator generates an HTML file that captures both the output and the visual graphs of cell relationships. 

# How Does It Work?

Simply mark each cell in your Python file between ##cell and ## comments. It analyzes dependencies and execute your cells in the right order. Dependency and execution graphs are automatically created. Get your results in an HTML file, including both your output and the graphs.


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
