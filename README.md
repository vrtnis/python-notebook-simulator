# Python Notebook Simulator

The **Python Notebook Simulator** is a project designed to help learn how deterministic and reproducible execution works in Python-like notebook environments.


You can:

- **Organize:** Arrange your Python code into neatly marked cells for easy execution.
- **Execute:** Analyze dependencies between cells and execute them in the correct order.
- **Visualize:** Automatically generate graphs that show the relationship between your cells.
- **HTML Output:** Save results and graphs to an HTML file for easy sharing.

## How Does It Work? 


1. **Write Your Code:**
   - Mark each cell in your Python file between `##cell` and `##` comments.

2. **Analyze and Execute:**
   - It analyzes dependencies and execute your cells in the right order.

3. **Generate Graphs:**
   - Dependency and execution graphs are automatically created.

4. **Share Results:**
   - Get your results in an HTML file, including both your output and the graphs.


## Getting Started

### Clone the Repository

To get started with the Python Notebook Simulator, you'll first need to clone the repository to your local machine. You can do this by opening your terminal or command prompt and running the following command:

```bash
git clone https://github.com/vrtnis/python-notebook-simulator.git
cd python-notebook-simulator

### Install Dependencies 

pip install -r requirements.txt


### Run 

python main.py -i ./examples/testinput.py
