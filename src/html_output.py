# src/html_output.py

def save_output_to_html(cells, cell_outputs, execution_order):
    
    html_content = "<html><head>"
    html_content += '''
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
    <style>
        body { max-width: 1000px; margin: auto; }
        pre code { color: white; background: black; padding: 8px; }
        .cell-id { font-weight: bold; margin-bottom: 10px; }
        .cell-container { 
            border: 2px solid #cccccc; 
            border-radius: 12px; 
            padding: 15px; 
            margin: 20px 0; 
            background-color: #f0f0f0; 
        }
    </style>
    '''
    html_content += "</head><body>"

    html_content += '''
    <div>
        <button onclick="showGraph('dependency-graph')">Show Dependency Graph</button>
        <button onclick="showGraph('execution-order-graph')">Show Execution Order</button>
        <div id="dependency-graph" style="display:none;">
            <img src="dependency_graph.png" alt="Dependency Graph">
        </div>
        <div id="execution-order-graph" style="display:none;">
            <img src="execution_order_graph.png" alt="Execution Order Graph">
        </div>
    </div>
    <script>
        function showGraph(graphId) {
            document.getElementById('dependency-graph').style.display = graphId === 'dependency-graph' ? 'block' : 'none';
            document.getElementById('execution-order-graph').style.display = graphId === 'execution-order-graph' ? 'block' : 'none';
        }
    </script>
    '''

    for cell_id, code in cells.items():
        output = cell_outputs.get(cell_id, "No output.")
        html_content += f'''
        <div class="cell-container">
            <div class="cell-id">{cell_id}</div>
            <pre><code class="language-python">{code}</code></pre>
            <strong>Output of {cell_id}:</strong>
            <pre><code class="language-python">{output}</code></pre>
        </div>
        '''

    html_content += '''
    
    </body></html>'''

    output_filepath = "cells_output.html"
    with open(output_filepath, 'w') as html_file:
        html_file.write(html_content)
    print(f"HTML output saved to {output_filepath}. Dependency and execution graph images generated and saved.")
