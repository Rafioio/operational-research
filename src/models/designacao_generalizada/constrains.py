import gurobipy as gp

def add_c1(model, vars, data):
    for i in data['I']:
        model.addConstr(gp.quicksum(vars['x'][i, j] for j in data['J']) <= 1, name=f"c1_{i}")

def add_c2(model, vars, data):
    for j in data['J']:
        model.addConstr(gp.quicksum(data['a'][i,j] * vars['x'][i, j] for i in data['I']) <= data['b'][j], name=f"c2_{j}")

        