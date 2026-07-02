import gurobipy as gp

def create_objective(model, vars, data):
    objetive_funcion = gp.quicksum(vars['x'][i,j] * data['c'][i,j] for i in data['I'] for j in data['J'])
    return objetive_funcion