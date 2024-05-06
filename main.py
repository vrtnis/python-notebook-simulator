# main.py

import argparse
from src.analyzer import analyze_dependencies
from src.executor import execute_cell
from src.graph_builder import generate_dependency_graph, generate_execution_order_graph
from src.html_output import save_output_to_html

cells = {}
dependencies = {}
graph = {}
execution_context = {}
cell_outputs = {}
execution_order = []

def add_or_update_cells_from_python(input_str):
    """Adds or updates multiple cells from a comment-delimited Python string."""
    cell_blocks = input_str.split("##cell")
    all_defined_vars = {}

    for block in cell_blocks:
        lines = block.strip().splitlines()
        if len(lines) < 2:
            continue
        cell_id = "cell" + lines[0].strip()
        code = '\n'.join(lines[1:])
        cells[cell_id] = code

        analyzed_vars = analyze_dependencies(code)
        dependencies[cell_id] = analyzed_vars["used"]
        all_defined_vars[cell_id] = set(analyzed_vars["defined"])
        graph[cell_id] = set()

    for cell_id, used_vars in dependencies.items():
        for var in used_vars:
            for defining_cell, defines in all_defined_vars.items():
                if var in defines and defining_cell != cell_id:
                    graph[defining_cell].add(cell_id)

    execute_all_cells()

def execute_all_cells():
    """Execute all cells in the correct dependency order."""
    global execution_order
    execution_order = topological_sort(graph)
    if execution_order is None:
        print("Execution aborted due to circular dependencies.")
        return

    print("Execution Order:", execution_order)
    for cell_id in execution_order:
        execute_cell(cell_id, cells, execution_context, cell_outputs)

    generate_dependency_graph(graph)
    generate_execution_order_graph(execution_order)
    save_output_to_html(cells, cell_outputs, execution_order)

def topological_sort(graph):
    """Perform a topological sort on the graph to identify dependency order, handling cycles."""
    in_degree = {cell_id: 0 for cell_id in graph}
    for nodes in graph.values():
        for adjacent in nodes:
            in_degree[adjacent] += 1

    queue = [cell_id for cell_id, degree in in_degree.items() if degree == 0]
    sorted_cells = []

    while queue:
        node = queue.pop(0)
        sorted_cells.append(node)

        for adjacent in graph[node]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0:
                queue.append(adjacent)

    if len(sorted_cells) != len(graph):
        print("Error: Circular dependency detected.")
        return None

    return sorted_cells

def load_python_and_execute(filepath):
    """Load a Python file containing cells and execute them."""
    try:
        with open(filepath, 'r') as file:
            input_str = file.read()
        add_or_update_cells_from_python(input_str)
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    """Main entry point to parse command-line arguments and execute cells from a Python file."""
    parser = argparse.ArgumentParser(description="Process a Python file to analyze and execute cells.")
    parser.add_argument('-i', '--input', required=True, help="Input Python file containing the cells.")
    args = parser.parse_args()
    load_python_and_execute(args.input)

if __name__ == "__main__":
    main()
