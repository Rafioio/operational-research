import gurobipy as gp

def create_objective(model, vars, data):
    model.setObjetive(gp.quicksum(vars['x'][i,j] * data['c'][i] for i in data['I'] for j in data['J']))