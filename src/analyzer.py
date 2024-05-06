# src/analyzer.py

import ast

def analyze_dependencies(code):
    
    tree = ast.parse(code)
    used_vars = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Store)}
    defined_vars = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)}
    return {"used": used_vars, "defined": defined_vars}
