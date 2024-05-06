# src/executor.py

import io
import sys

def execute_cell(cell_id, cells, context, outputs):
    
    code = cells.get(cell_id)
    if not code:
        print(f"Cell {cell_id} not found")
        return

    
    output_buffer = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = output_buffer

    try:
        
        exec(code, context)
        sys.stdout = original_stdout
        output = output_buffer.getvalue()
        outputs[cell_id] = output if output else "No output."
        print(f"Executed cell {cell_id}\nOutput:\n{output}")
    except Exception as e:
        sys.stdout = original_stdout
        print(f"Error executing cell {cell_id}: {e}")
        outputs[cell_id] = f"Error: {e}"
