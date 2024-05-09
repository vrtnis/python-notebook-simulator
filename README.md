### Python Notebook Simulator

The Python Notebook Simulator is a project I created to better understand concepts, such as deterministic and reproducible execution, within Python-like notebook environments. It is an ongoing experiment and is likely to have flaws!

The simulator examines the dependencies between "cells" defined by Python comments (e.g., #cellid) to establish a fixed order in which they should be executed.

Furthermore, the simulator helps visualize dependencies among code cells. This visualization shows how each cell is interconnected, providing insights into the flow of data and the impact of each section of code on subsequent computations. After execution, the simulator generates an HTML file that captures both the output and the visual graphs of cell relationships. 

#### How Does It Work?

To define cells in your Python file, simply start each cell with a `##cell` comment and optionally end it with another comment like `##`. This marks the boundaries of each cell.
It analyzes dependencies and execute your cells in the right order. Dependency and execution graphs are automatically created. Get your results in an HTML file, including both your output and the graphs.

<p align="center">
  <img src="images/test_input.png" alt="Test Input" width="400"/>
  <img src="images/test_output.png" alt="Test Output" width="400"/>
</p>


### Getting Started


[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/vrtnis/python-notebook-simulator)

Opens up a Gitpod, installs all dependencies runs `python main.py -i ./examples/testinput.py` and displays cells_output.html in the Gitpod browser.

<img src="images/simulator_gitpod.png" alt="Join Discord" width="200"/>


### Or run it locally

#### Clone the Repository

To get started, you'll first need to clone the repository to your local machine. You can do this by opening your terminal or command prompt and running the following command:

```bash
git clone https://github.com/vrtnis/python-notebook-simulator.git
cd python-notebook-simulator
```


#### Install Dependencies 

```
pip install -r requirements.txt
```

#### Run It!

```
python main.py -i ./examples/testinput.py

```
#### Community

<a href="https://discord.gg/JE7nhX6mD8" target="_blank">
    <img src="images/Discord-logo.png" alt="Join Discord" width="200"/>
</a>

 
To learn more about concepts such as deterministic and reproducible execution, ask questions and connect with other Python enthusiasts, consider joining the [marimo Discord server](https://discord.gg/JE7nhX6mD8). [marimo](https://github.com/marimo-team/marimo) is an **open-source** project that revolutionizes how we think about Python notebooks. marimo notebooks are reproducible, extremely interactive, designed for collaboration (git-friendly!), deployable as scripts or apps. 



